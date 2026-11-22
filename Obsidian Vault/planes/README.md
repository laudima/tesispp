# Planeación: pendientes, prioridades y fechas límite

Cómo funciona el sistema que conecta `Obsidian Vault/Pendientes.md`, los issues de este repo, el proyecto de GitHub, Google Calendar y el resumen diario de Claude.

## Flujo

1. **Captura** en `Obsidian Vault/Pendientes.md`, como siempre, sin formato.
2. **Issue**: cada pendiente académico (tesis, Philcomp, CADIS, TOEFL, doctorados) es un issue con prioridad y fecha. Lo personal, la búsqueda de trabajo y el trabajo actual no van a GitHub porque el repo es público; viven en Google Calendar y en el resumen diario.
3. **Tablero**: el workflow `.github/workflows/tablero.yml` mantiene el issue "📌 Tablero de pendientes" con todo ordenado por fecha y prioridad, avisos y una línea de tiempo. Se regenera cada mañana y cada vez que cambia un issue.
4. **Calendario**: cada fecha límite es un evento de todo el día en Google Calendar con el prefijo `⏰ Fecha límite:` y el enlace al issue.
5. **Resumen diario**: Claude lee el calendario, los issues y `Pendientes.md` cada mañana y manda el plan del día.

## Convenciones de un issue

- **Fecha límite**: primera línea del cuerpo, `**Fecha límite:** AAAA-MM-DD` (o `sin fecha`). Es la fecha en que el trabajo tiene que estar terminado, no la del evento.
- **Prioridad**: una sola etiqueta.

| Etiqueta | Cuándo usarla |
|---|---|
| `P0-urgente` | Vence en 7 días o menos, o bloquea otra cosa |
| `P1-alta` | Tiene fecha este mes, o es núcleo de la tesis |
| `P2-media` | Importante, sin fecha cercana |
| `P3-baja` | Algún día / explorar |

- **Área**: `área:tesis`, `área:philcomp`, `área:cadis`, `área:toefl`, `área:doctorado`.
- Al terminar, cerrar el issue; desaparece del tablero.

Regla para decidir: primero la fecha (lo que vence pronto sube), después el costo de no hacerlo (lo que cierra una puerta, como una convocatoria, sube), y al final lo que desbloquea otras tareas. Un pendiente sin fecha nunca es P0: o se le pone fecha o baja de prioridad.

## Plan 2027

Solo lo que ya está anotado; cada renglón se vuelve un issue con fecha en cuanto se conozca.

| Periodo | Plan |
|---|---|
| Ene–Mar | Resultados de la tesis con los LLMs privados sobre todo el dataset (#4). Arranca el seminario quincenal de Philcomp. Fijar fechas de Aspire (#7) y de las convocatorias de BCBL y Goethe (#9). |
| Abr–Jun | Aplicaciones a doctorado e internships de investigación según las fechas encontradas. |
| Jul–Sep | Materiales del Max Planck CIS Internship listos (#8). Revisar voluntariado de NeurIPS 2027 (#10). |
| Oct–Dic | Max Planck CIS: enviar antes del 1 de noviembre para inicio mayo–agosto de 2028. |
