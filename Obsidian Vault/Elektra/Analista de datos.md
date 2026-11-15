## Contexto y propósito del puesto
Buscamos a una persona que se encargue de la limpieza, carga y pronostico aplicado en retail.
- **Nivel:** Consultor Analista de Datos
- **Rango salarial:** $33,000 a $35,000
- **Modalidad:** Remota
## Responsabilidades

1. **Carga semanal:** recibir los exportes de Tableau, limpiarlos, cargarlos en DuckDB y regenerar los datos de los tableros sin romper la serie histórica.

2. **Cuadre y calidad de datos:** cuadrar inventario total, documentar cada diferencia y su causa.

3. **Reglas de negocio en código:** mantener los filtros y la jerarquía de estatus alineados con las reglas vigentes de Gobierno comercial.

4. **Análisis de ciclo de vida:** explicar qué cambia de estatus en las próximas 4 y 8 semanas, como cambia el comportamiento

del inventario de acuerdo a estacionalidad.

5. **Estimados y supuestos:** revisar los estimados actuales (pronóstico de 13 semanas, inventario sano por SKU, semanas sin venta ).

6. **Pronóstico y riesgo:** construir y validar modelos de venta / demanda y de probabilidad, con métricas claras (MAE, MAPE, precision / recall), y segmentar el inventario (ABC / XYZ, rotación, clusters de SKU y tienda) para decidir qué liquidar, reubicar o dejar de resurtir.

7. **Narrativa ejecutiva:** preparar la Radiografía semanal con hallazgos, variaciones contra la semana anterior y 3 acciones por bloque con responsable.

8. **Insumos para el asistente de IA:** mantener el catálogo de consultas SQL y el contexto de datos, y armar el conjunto de preguntas con respuesta esperada para evaluar al asistente.

9. **Documentación:** diccionario de datos, catálogo de KPIs y bitácora de supuestos actualizados en el repositorio.

  

## Requerimientos técnicos

  

Los indispensables son los que se usan desde la primera semana; los deseables pesan para desempatar.

  

| Competencia | Nivel | Descripción |

| --- | --- | --- |

| SQL analítico (agregaciones, ventanas, CTEs, joins) | Indispensable | Consultas sobre DuckDB, cuadres y catálogo de consultas del asistente |

| Python para datos (pandas o similar, biblioteca estándar, scripts reproducibles) | Indispensable | Limpieza de capas, filtros y generación de datos del tablero |

| Machine Learning (scikit-learn o similar: regresión, clasificación, validación cruzada, ingeniería de variables) | Indispensable | Riesgo de que una tienda-SKU pase a LD, detección de anomalías |

| Pronóstico de demanda (series de tiempo, estacionalidad, modelos jerárquicos por SKU / tienda) | Indispensable | Pronóstico de 12 semanas, Buen Fin y diciembre, cobertura de inventario |

| Segmentación de inventario (ABC / XYZ, rotación, clustering de SKUs y tiendas) | Indispensable | Priorizar qué liquidar, reubicar o dejar de resurtir |

| Manejo de archivos grandes y sucios (CSV de cientos de MB, columnas repetidas, vacíos, tipos) | Indispensable | Exportes semanales de Tableau |

| Estadística aplicada (inferencia, validación de supuestos) | Indispensable | Revisar los estimados del tablero y las alertas Pre-LD |

| Git y trabajo en repositorio | Indispensable | Todo el código y la documentación viven versionados |

| Excel / Tableau a nivel usuario avanzado | Indispensable | Leer los filtros de Tableau y reproducirlos en código |

| Visualización y presentaciones ejecutivas (PowerPoint) | Indispensable | Radiografía semanal |

| DuckDB, SQL Server o un Data Mart | Deseable | Base actual y migración prevista en el SOW |

| Puesta en producción de modelos (versionado, monitoreo de drift) | Deseable | AgentOps / MLOps |

| HTML / JavaScript básico | Deseable | Ajustes en los tableros |

| Uso de LLMs (text-to-SQL, evaluación de respuestas) | Deseable | Asistente del tablero y benchmark de preguntas |

  

## Conocimiento de negocio

  

La experiencia en retail o cadena de suministro es deseable; lo indispensable es aprender rápido estas reglas, porque los cuadres dependen de ellas.

  

## Perfil y ponderación

  

- **Formación:** licenciatura en Actuaría, Matemáticas, Estadística, Economía, Ciencia de Datos, Computación o Ingeniería Industrial.

- **Experiencia:** propuesta de 2 a 4 años en análisis de datos, con al menos un proyecto de reporte recurrente (semanal o mensual) que haya mantenido en producción.

- **Diferenciadores:** experiencia en cadenas de retail multitienda con muchos SKUs, modelos de pronóstico y segmentación de inventario puestos en uso real, haber migrado reportes de Tableau / Excel / PowerBI a código, portafolio en GitHub.

  
  

| Competencia | Peso propuesto (analista) |

| --- | --- |

| Machine Learning y modelos predictivos | 20% |

| SQL / bases de datos | 15% |

| Python / programación | 15% |

| Estadística / matemáticas | 10% |

| Calidad de datos y cuadre (Data Engineering) | 10% |

| Conocimiento de retail e inventario | 10% |

| Comunicación y narrativa ejecutiva | 5% |

| LLM / RAG / agentes | 15% |

| **Total** | **100%** |