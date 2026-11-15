Versión: v0.1  
Estado: MVP funcional en validación  
Prioridad: Alta  
Owner actual: Mauricio (implementación inicial)  
Responsable técnico solicitado: Lau

---

# 1. Objetivo

Este documento tiene como objetivo transferir el contexto técnico completo del MVP de RAI Diagnostic 360 para que Lau pueda revisarlo, validar la arquitectura y apoyar en su consolidación.

Esta implementación la desarrollé personalmente para acelerar la validación del servicio y no detener el avance del proyecto. Sin embargo, este componente debe pasar a una arquitectura mantenible y delegable.

No buscamos reconstruir el trabajo.

Buscamos revisar, fortalecer y preparar el sistema para operación continua.

---

# 2. ¿Por qué es importante?

Diagnostic 360 será uno de los componentes centrales de RAI.

No es solamente un formulario ni una minuta.

Es el punto de entrada del conocimiento comercial.

A partir de una sesión queremos generar automáticamente conocimiento reutilizable para toda la organización.

Este flujo conecta directamente con:

- Ventas
    
- Delivery
    
- Knowledge Base
    
- Inteligencia Comercial
    
- Talento
    
- Innovation Tracker
    
- Productos futuros
    
- Automatizaciones
    
- Agentes
    

Si esta pieza queda sólida, reducimos muchísimo trabajo manual.

---

# 3. Objetivo operativo

Cada sesión debería convertirse automáticamente en información útil.

Flujo esperado:

Agenda una sesión

↓

  

Se realiza el Diagnostic 360

  

↓

  

Gemini genera la minuta

  

↓

  

La minuta llega automáticamente

  

↓

  

Apps Script detecta nueva minuta

  

↓

  

Reader

  

↓

  

Extractor

  

↓

  

Gemini

  

↓

  

Database

  

↓

  

Master Database

  

↓

  

Información reutilizable

Posteriormente esa información alimentará:

- CRM
    
- Knowledge Base
    
- Analytics
    
- IA
    
- Automatizaciones
    
- Agentes
    

---

# 4. Arquitectura actual

Actualmente existen dos proyectos distintos de Apps Script.

## Proyecto 1

### RAI Diagnostic Session Processor MVP

Responsabilidad:

Procesar completamente una minuta.

Incluye:

- lectura
    
- extracción base
    
- extracción con Gemini
    
- escritura en Master Database
    
- control de procesados
    

Proyecto:

https://script.google.com/u/5/home/projects/1YwByRUfdZWEf1Q0gpwX3n93p4T8K33aZUrTBqPf-mCLLqz6D5G8Om14s/edit

---

## Proyecto 2

### Automation

Responsabilidad actual:

Automatizar el flujo previo al processor.

Actualmente este proyecto intenta encargarse de detectar la nueva minuta y dejarla lista para procesamiento.

Proyecto:

https://script.google.com/u/5/home/projects/1jG_LH5ABdsqBMhk1FCjGMs6SVz4eFBCdYe4cKqCtLyrtlf65zbHhP6NY/edit?hl=es-419

Este flujo todavía necesita revisión porque durante las pruebas detectamos comportamientos inconsistentes.

---

# 5. Componentes principales

El processor actualmente está dividido aproximadamente así:

config.gs

  

setup.gs

  

reader.gs

  

extractor.gs

  

gemini.gs

  

database.gs

  

processor.gs

La separación ha funcionado bien para el MVP.

Sin embargo queremos validar si esta arquitectura sigue siendo la adecuada para producción.

---

# 6. Recursos involucrados

## Master Database

https://docs.google.com/spreadsheets/d/1O0ngo1_tfVlFcXueen5XFgzE9kNs7K5FgQXC7cxqODQ/edit

Contiene:

- SESIONES
    
- TALENTO
    
- INSIGHTS_DIAGNOSTICO
    
- MERCADO_VENTAS
    

---

## Folder Diagnostic 360

https://drive.google.com/drive/u/5/folders/1cm78iMCWU9tWhMsDe0yRqecrCz0Tj9Vy

Aquí terminan las minutas utilizadas por el processor.

---

## Calendario de sesiones

https://calendar.google.com/calendar/u/0/appointments/schedules/AcZssZ2xfsXWuuvt6p8E4_OX2BziCwZN3Ef62_WGSy9MYM09sCyVJ9hlm_SXM3nLmNo1-vlOzut42vKa

Es el calendario utilizado para agendar las sesiones de Diagnostic 360.

---

## Web App

https://360-diagnostic.vercel.app/

Actualmente sirve como experiencia inicial para el cliente antes de la sesión.

---

# 7. Flujo técnico actual

Cliente agenda

  

↓

  

Calendar

  

↓

  

Meet

  

↓

  

Gemini genera la minuta

  

↓

  

Automation

  

↓

  

Folder Diagnostic

  

↓

  

Processor

  

↓

  

Reader

  

↓

  

Extractor Base

  

↓

  

Gemini

  

↓

  

Database

  

↓

  

Master Database

---

# 8. Estado actual

El MVP ya logró completar exitosamente un flujo end-to-end.

Durante la última prueba se consiguió:

- detectar una minuta nueva;
    
- leer completamente el documento;
    
- ejecutar Gemini;
    
- estructurar la información;
    
- registrar correctamente en la Master Database;
    
- marcar la minuta como procesada.
    

El pipeline ya funciona.

Ahora necesitamos endurecerlo.

---

# 9. Problemas encontrados

Durante las pruebas aparecieron varios puntos importantes.

## 1. Movimiento de minutas

No siempre fue consistente.

Necesitamos revisar si la estrategia actual es la correcta.

---

## 2. Idioma

Google cambió automáticamente:

Notes by Gemini

por

Notas de Gemini

Eso rompió inicialmente el filtro.

Ya se corrigió parcialmente.

Queremos revisar una estrategia menos frágil.

---

## 3. Participante

Actualmente el nombre depende mucho del filename.

En una prueba:

Prueba Real

se convirtió en el participante.

Necesitamos una estrategia más robusta.

---

## 4. Calidad semántica

Gemini funciona.

Pero todavía:

- sobreinfiere algunas cosas;
    
- mezcla contexto de RAI con contexto del cliente;
    
- interpreta algunos presupuestos incorrectamente;
    
- propone next steps que no siempre corresponden.
    

Necesitamos endurecer el prompt y probablemente agregar validaciones posteriores.

---

## 5. Separación TEST / PROD

Durante una prueba escribimos accidentalmente en la base de producción.

Necesitamos una estrategia clara para manejar ambientes.

---

## 6. Idempotencia

Actualmente funciona mediante transcript.

Queremos validar que sea suficientemente robusta.

---

# 10. Lo que NO buscamos

No queremos rehacer todo.

No queremos cambiar tecnología por cambiarla.

No queremos introducir automatizaciones adicionales todavía.

La intención es fortalecer la base existente.

---

# 11. Qué necesitamos de Lau

Necesitamos una revisión técnica completa.

Esperamos que pueda responder, como mínimo:

## Arquitectura

¿La separación actual tiene sentido?

¿Qué conservarías?

¿Qué cambiarías?

---

## Riesgos

¿Qué riesgos técnicos ves?

¿Qué puede romperse?

¿Qué estamos dejando de considerar?

---

## Calidad

¿Qué mejorarías para que el pipeline sea más robusto?

---

## Automatización

¿Cambiarías el flujo?

¿Separarías responsabilidades de otra manera?

---

## Movimiento de minutas

¿La estrategia actual es correcta?

¿Hay una alternativa mejor?

---

## Extracción

¿Qué mejorarías del prompt?

¿Qué validaciones agregarías?

---

## Base de datos

¿Modificarías la estructura?

¿Agregarías llaves técnicas?

¿Cambiarías Session ID?

---

## Escalabilidad

Si mañana procesamos:

- 20 sesiones
    
- 100 sesiones
    
- 1000 sesiones
    

¿Dónde estarán los cuellos de botella?

---

## Seguridad

¿Qué debemos cuidar?

- permisos
    
- APIs
    
- Drive
    
- Sheets
    
- propiedades
    
- triggers
    

---

## Estimación

Si tú tomaras este proyecto:

¿Cuánto tiempo estimas para dejarlo listo para operación?

Separar por:

- revisión
    
- ajustes
    
- pruebas
    
- estabilización
    

---

# 12. Qué esperamos recibir

No necesitamos código inmediatamente.

Primero queremos un diagnóstico técnico.

Idealmente:

1. Qué dejar igual.
    
2. Qué cambiar.
    
3. Qué priorizar.
    
4. Riesgos.
    
5. Estimación.
    
6. Dependencias.
    
7. Recomendación final.
    
8. GO / NO-GO para operación.
    

---

# 13. ¿Por qué esto es prioritario?

Porque este pipeline será la base para:

- centralizar el conocimiento generado en cada sesión;
    
- reducir captura manual de información;
    
- estandarizar el proceso comercial;
    
- alimentar automáticamente la base de conocimiento;
    
- identificar oportunidades comerciales;
    
- detectar talento;
    
- generar inteligencia reutilizable;
    
- habilitar futuras automatizaciones y agentes.
    

En términos operativos, este componente permitirá ahorrar tiempo, reducir errores, disminuir trabajo repetitivo y facilitar la delegación del proceso, alineándose con la forma de trabajo de RAI: primero ordenar y estandarizar, después automatizar.

  