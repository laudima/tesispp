#!/usr/bin/env python3
"""Genera el issue "Tablero de pendientes" a partir de los issues abiertos.

Convenciones que lee de cada issue:
  - Prioridad: etiqueta que empieza con P0, P1, P2 o P3.
  - Área: etiqueta "área:<nombre>".
  - Fecha límite: una línea "**Fecha límite:** AAAA-MM-DD" en el cuerpo.

Uso:
  GITHUB_TOKEN=... GITHUB_REPOSITORY=owner/repo python3 tablero.py
  python3 tablero.py --dry-run --fixture issues.json [--hoy AAAA-MM-DD]
"""
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

API = "https://api.github.com"
ZONA = ZoneInfo("America/Mexico_City")
ETIQUETA_TABLERO = "tablero"
TITULO_TABLERO = "📌 Tablero de pendientes"

# nombre -> (color, descripción)
ETIQUETAS = {
    "P0-urgente": ("b60205", "Vence en 7 días o menos, o bloquea otra cosa"),
    "P1-alta": ("d93f0b", "Importante con fecha este mes, o núcleo de la tesis"),
    "P2-media": ("fbca04", "Importante sin fecha cercana"),
    "P3-baja": ("0e8a16", "Algún día / explorar"),
    "área:tesis": ("5319e7", ""),
    "área:philcomp": ("1d76db", ""),
    "área:cadis": ("0052cc", ""),
    "área:toefl": ("006b75", ""),
    "área:doctorado": ("c5def5", ""),
    ETIQUETA_TABLERO: ("ededed", "Issue generado automáticamente; no editar a mano"),
}
ICONOS = {"P0": "🔴 P0", "P1": "🟠 P1", "P2": "🟡 P2", "P3": "🟢 P3", None: "⚪ —"}
MESES = "ene feb mar abr may jun jul ago sep oct nov dic".split()
DIAS = "lun mar mié jue vie sáb dom".split()
RE_FECHA = re.compile(r"Fecha\s+l[ií]mite[\s:*_]*(\d{4}-\d{2}-\d{2})", re.IGNORECASE)


def api(metodo, ruta, datos=None):
    peticion = urllib.request.Request(
        ruta if ruta.startswith("http") else API + ruta,
        method=metodo,
        data=json.dumps(datos).encode() if datos is not None else None,
        headers={
            "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "tablero-pendientes",
        },
    )
    with urllib.request.urlopen(peticion) as respuesta:
        cuerpo = respuesta.read()
        return json.loads(cuerpo) if cuerpo else None


def issues_abiertos(repo):
    resultado, pagina = [], 1
    while True:
        lote = api("GET", f"/repos/{repo}/issues?state=open&per_page=100&page={pagina}")
        resultado += [i for i in lote if "pull_request" not in i]
        if len(lote) < 100:
            return resultado
        pagina += 1


def asegurar_etiquetas(repo):
    existentes = {}
    pagina = 1
    while True:
        lote = api("GET", f"/repos/{repo}/labels?per_page=100&page={pagina}")
        existentes.update({e["name"]: e for e in lote})
        if len(lote) < 100:
            break
        pagina += 1
    for nombre, (color, descripcion) in ETIQUETAS.items():
        actual = existentes.get(nombre)
        if actual is None:
            api("POST", f"/repos/{repo}/labels",
                {"name": nombre, "color": color, "description": descripcion})
        elif actual["color"].lower() != color or (actual.get("description") or "") != descripcion:
            api("PATCH", f"/repos/{repo}/labels/{urllib.parse.quote(nombre)}",
                {"color": color, "description": descripcion})


def interpretar(issue):
    etiquetas = [e["name"] for e in issue.get("labels", [])]
    prioridad = next((e[:2].upper() for e in etiquetas if re.match(r"(?i)p[0-3]\b", e)), None)
    area = next((e.split(":", 1)[1] for e in etiquetas if e.lower().startswith("área:")), "sin área")
    encontrada = RE_FECHA.search(issue.get("body") or "")
    fecha = None
    if encontrada:
        try:
            fecha = date.fromisoformat(encontrada.group(1))
        except ValueError:
            pass
    return {
        "numero": issue["number"],
        "titulo": issue["title"],
        "url": issue["html_url"],
        "prioridad": prioridad,
        "area": area,
        "fecha": fecha,
    }


def fecha_legible(f):
    return f"{DIAS[f.weekday()]} {f.day} {MESES[f.month - 1]} {f.year}"


def faltan(f, hoy):
    dias = (f - hoy).days
    if dias < 0:
        return f"**venció hace {-dias} d**"
    if dias == 0:
        return "**hoy**"
    if dias == 1:
        return "**mañana**"
    return f"{dias} d"


def orden_prioridad(t):
    return t["prioridad"] or "P9"


def tabla(tareas, hoy):
    filas = ["| Prioridad | Pendiente | Área | Fecha límite | Faltan |", "|---|---|---|---|---|"]
    for t in tareas:
        titulo = t["titulo"].replace("|", "\\|")
        filas.append(
            f"| {ICONOS[t['prioridad']]} | [{titulo}]({t['url']}) #{t['numero']} | {t['area']} | "
            + (f"{fecha_legible(t['fecha'])} | {faltan(t['fecha'], hoy)} |" if t["fecha"] else "sin fecha | — |")
        )
    return "\n".join(filas)


def gantt(tareas, hoy):
    con_fecha = [t for t in tareas if t["fecha"]]
    if not con_fecha:
        return ""
    lineas = ["```mermaid", "gantt", "    dateFormat YYYY-MM-DD", "    axisFormat %d %b",
              "    title Tiempo que queda para cada fecha límite"]
    for area in sorted({t["area"] for t in con_fecha}):
        lineas.append(f"    section {area}")
        for t in sorted((t for t in con_fecha if t["area"] == area), key=lambda t: t["fecha"]):
            nombre = " ".join(re.sub(r"[^\w\s.()-]", " ", t["titulo"]).split())[:60]
            marcas = {"P0": "crit, ", "P1": "active, "}.get(t["prioridad"], "")
            if t["fecha"] <= hoy:
                lineas.append(f"    {nombre} ({t['numero']}) :milestone, crit, {t['fecha']}, 0d")
            else:
                lineas.append(f"    {nombre} ({t['numero']}) :{marcas}{hoy}, {t['fecha']}")
    lineas.append("```")
    return "\n".join(lineas)


def generar(tareas, hoy):
    con_fecha = sorted((t for t in tareas if t["fecha"]), key=lambda t: (t["fecha"], orden_prioridad(t)))
    sin_fecha = sorted((t for t in tareas if not t["fecha"]), key=lambda t: (orden_prioridad(t), t["numero"]))
    grupos = [
        ("🔴 Vencidos", [t for t in con_fecha if t["fecha"] < hoy]),
        ("🟠 Próximos 7 días", [t for t in con_fecha if hoy <= t["fecha"] <= hoy + timedelta(days=7)]),
        ("🟡 Próximos 30 días", [t for t in con_fecha if hoy + timedelta(days=7) < t["fecha"] <= hoy + timedelta(days=30)]),
        ("🟢 Más adelante", [t for t in con_fecha if t["fecha"] > hoy + timedelta(days=30)]),
        ("⚪ Sin fecha límite", sin_fecha),
    ]
    partes = [f"_Actualizado: {fecha_legible(hoy)}. Se regenera solo cada mañana y cada vez que cambia un issue; no lo edites a mano._",
              "",
              f"**{len(tareas)} pendientes abiertos** · " + " · ".join(f"{nombre.split(' ', 1)[1]}: {len(lista)}" for nombre, lista in grupos)]
    for nombre, lista in grupos:
        if lista:
            partes += ["", f"## {nombre}", "", tabla(lista, hoy)]
    avisos = []
    sin_prioridad = [t for t in tareas if not t["prioridad"]]
    if sin_prioridad:
        avisos.append("Sin etiqueta de prioridad: " + ", ".join(f"#{t['numero']}" for t in sin_prioridad))
    urgentes_sin_fecha = [t for t in sin_fecha if t["prioridad"] == "P0"]
    if urgentes_sin_fecha:
        avisos.append("P0 sin fecha límite: " + ", ".join(f"#{t['numero']}" for t in urgentes_sin_fecha))
    por_subir = [t for t in con_fecha if t["prioridad"] not in ("P0",) and hoy <= t["fecha"] <= hoy + timedelta(days=7)]
    if por_subir:
        avisos.append("Vencen en 7 días o menos y no son P0: " + ", ".join(f"#{t['numero']}" for t in por_subir))
    if avisos:
        partes += ["", "## ⚠️ Por revisar", ""] + [f"- {a}" for a in avisos]
    diagrama = gantt(tareas, hoy)
    if diagrama:
        partes += ["", "## Línea de tiempo", "", diagrama]
    partes += ["", "---", "Cómo se lee: prioridad = etiqueta `P0`–`P3`; fecha = línea `**Fecha límite:** AAAA-MM-DD` en el cuerpo del issue. Detalles en `planes/README.md`."]
    return "\n".join(partes) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--fixture")
    parser.add_argument("--hoy")
    args = parser.parse_args()

    hoy = date.fromisoformat(args.hoy) if args.hoy else datetime.now(ZONA).date()
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    if args.fixture:
        with open(args.fixture, encoding="utf-8") as archivo:
            issues = json.load(archivo)
    else:
        issues = issues_abiertos(repo)

    def es_tablero(issue):
        return any(e["name"] == ETIQUETA_TABLERO for e in issue.get("labels", []))

    tableros = [i for i in issues if es_tablero(i)]
    cuerpo = generar([interpretar(i) for i in issues if not es_tablero(i)], hoy)

    if args.dry_run:
        print(cuerpo)
        return
    asegurar_etiquetas(repo)
    if tableros:
        if (tableros[0].get("body") or "").strip() != cuerpo.strip():
            api("PATCH", f"/repos/{repo}/issues/{tableros[0]['number']}", {"body": cuerpo})
            print(f"Tablero actualizado: #{tableros[0]['number']}")
        else:
            print("Tablero sin cambios")
    else:
        nuevo = api("POST", f"/repos/{repo}/issues",
                    {"title": TITULO_TABLERO, "body": cuerpo, "labels": [ETIQUETA_TABLERO]})
        print(f"Tablero creado: #{nuevo['number']}")


if __name__ == "__main__":
    try:
        main()
    except urllib.error.HTTPError as error:
        sys.exit(f"Error de la API de GitHub: {error.code} {error.read().decode(errors='replace')}")
