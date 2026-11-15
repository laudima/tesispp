 **1.⁠ ⁠Alcance: ¿Está claro lo que vamos a construir? ¿Hay algo que debamos agregar, ajustar o excluir?**
 
Una plataforma web que englobe todo el proceso de Oferta Educativa, la plataforma guía al usuario paso a paso y pone checkpoints para que también existan las sesiones persona a persona. 

*Que podemos agregar*: segunda fase incluiría las integraciones con IA para hacer un match más preciso entre el usuario y la oferta educativa, agentes que realicen web scrapping para agregar ofertas educativas, si logramos incorporar test psícometricos propios o bajo una licencia la plataforma se podría vender a empresas como un kit en el proceso de contratación. 

*Excluir*: delimitar por fases, primero poniendo los enlaces a los test externos, asegurándonos que el flujo básico del MVP se cumpla, y podamos tener bien definidos los roles y los usuarios en la base de datos. 

 **2.⁠ ⁠Arquitectura: ¿Qué tecnologías recomiendan y qué podemos aprovechar de lo que ya existe?**

El stack de la aplicación lo definirá Diego, se puede integrar un servicio de transcripción open source. Para que todo el procesamiento de las sesiones se hagan de manera local. 

 **3.⁠ ⁠Desarrollo: ¿Cómo dividirían el proyecto en etapas y cuánto tiempo estiman para cada una?**

Fase 1: Definir el prototipo que se va a implementar, este puede cambiar en diseño conforme a las sesiones con el owner de Neoma. Flujo básico con integraciones, las sesiones se siguen llevando en google meet, el archivo de la transcripción solo se sube como un pdf, los test psícometricos se redirigir con un enlace. 

 **4.⁠ ⁠Responsabilidades: ¿Quién se encargaría de cada componente y qué apoyo adicional necesitaríamos?**

Laura: enlace entre Neoma y Diego para establecer los requerimientos de la plataforma. 
Mauricio: Aprobación de los avances, pruebas manuales de usuario, enlace con el owner del proyecto. Proveedor de los servicios de hosting, correo, y repo donde vive la aplicación. 
Diego: desarrollador de toda la aplicación. 

 **5.⁠ ⁠Integraciones: ¿Qué necesitamos para conectar la aplicación con los sistemas actuales y migrar la información?**
 
 * de Airtable a un cvs con la se pobla la base de datos. 
 * conexión con la api de google para agendar las sesiones
 * podemos ocupar otras integraciones para el login 
 
 **6.⁠ ⁠Inteligencia artificial: ¿Es viable implementar los módulos de transcripción local, perfiles psicométricos y matching como están planteados? ¿Qué habría que validar primero?**

* primero implementar la transcripción local. 
* después de migrar la BD va a ser importante saber cuantos datos tenemos para crear los clusters, algo que se puede hacer un vector para el usuario. y un vector para las ofertas, determinar bajo criterios paramétricos que opciones tienen mas afinidad con el perfil. 

 **7.⁠ ⁠Pruebas: ¿Cómo comprobaríamos que los cuatro roles y las siete fases funcionan correctamente?**

* Test del backend, unit test for all api calls, and writes in the bd
* Test del frontend, podemos ocupar playwright para establecer los casos funcionales que hace la aplicación y automatizarlos. 
 
 **8.⁠ ⁠Operación: ¿Qué infraestructura, mantenimiento y soporte necesitaría la plataforma una vez entregada?**

* Nuevas funciones
* Posibles bugs menores, de los se abrirán issues en el repo, y después se hará el cambio. 
 
 **9.⁠ ⁠Riesgos: ¿Qué podría complicar el desarrollo o modificar los tiempos estimados?**

 Si se quiere integrar los test desde la primera fase los tiempos pueden cambiar considerablemente. 
  Si se quiere integrar una api de algún LLM para un proceso, es importante pensar de que manera podemos automatizar este proceso sin usarlo, para mitigar los costos de uso. 
  La seguridad de la base de datos, log in, y otras vulnerabilidades que comprometan los datos personales, posiblemente podemos contratar en las ultimas semanas a un pen tester para identificarlas. 
  
**10.⁠ ⁠Recomendación final: ¿Qué cambiarían o mejorarían antes de comprometernos con el alcance definitivo?**
