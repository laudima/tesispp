# La imposibilidad de comprimir la realidad: una crítica computacional a la promesa tecnocientífica

## Resumen

En esta ponencia, propongo una crítica desde la teoría de la computación y la epistemología científica al entusiasmo tecnocientífico que coloca a la inteligencia artificial como motor revolucionario del conocimiento. A partir del teorema de incompletitud de Gödel, el número Ω de Chaitin y la teoría de la complejidad computacional, argumento que existen límites inherentes a lo que las máquinas pueden comprender, predecir o descubrir, incluso con modelos de inteligencia artificial avanzada. Reviso brevemente algunos modelos de IA aplicados a la ciencia (como AlphaFold de Google o AI4Science de Microsoft) y cuestiono si estos realmente representan un avance hacia la comprensión o simplemente una sofisticación en la predicción. Concluyo que, frente a estos límites, debemos volver a preguntarnos por el sentido, el significado y el rol de la ciencia como búsqueda y no sólo como herramienta predictiva. Esta reflexión se inscribe dentro de los debates actuales sobre la tecnopolítica del conocimiento en el siglo XXI.

## Abstract

In this essay, I critique the idea that AI will revolutionize science. First, I present some of the limitations of computation given by Gödel's Incompleteness Theorem and the complexity of Chaitin's number Ω, as presented in his article _The Limits of Reason_; after that, I present a brief notion of computational complexity in relation to the limits of what we can know. In the next section, I describe some of the computational models built to do science and briefly summarize the current advances in AI-driven science.

---

## 1. Motivación

En la búsqueda de la verdad, de la comprensión de los patrones y de las leyes universales que nos rigen, buscamos encontrar reglas consistentes y verdades objetivas. ¿Cuáles son los límites de la computación para expresar las leyes de la naturaleza? ¿Cómo podemos utilizar herramientas computacionales para desarrollar ciencia, no sólo con fines utilitarios o prácticos, sino para encontrar modelos que encapsulen nuestro entendimiento de la realidad? ¿Podemos llevar a cabo un programa para un desarrollo de la ciencia posthumanista o transhumanista?

Si incorporamos la inteligencia artificial como herramienta o guía a nuevos descubrimientos, ¿qué intentamos perseguir en la búsqueda de la verdad? ¿Podemos encontrar un método eficiente de verificabilidad para estos algoritmos? Cuando la ciencia utiliza datos para construir modelos predictivos, ¿qué significa encontrar un descubrimiento, un nuevo teorema o un nuevo patrón? ¿Estamos construyendo una forma automatizada de la intuición? Y si es así, ¿cuáles son las consecuencias de desarrollar una forma automatizada de ciencia?

> Who of us would not be glad to lift the veil behind which the future lies hidden; to cast a glance at the next advances of our science and the secrets of its development during future centuries? (Hilbert, 1902, p. 437)

## 2. Los límites de la computación y de la razón

Las matemáticas se fundamentan en axiomas para construir teoremas a partir de deducciones lógicas, que a su vez dan pie a nuevos resultados, todo bajo un lenguaje formal. Este proceso, que quiere ser independiente de la subjetividad de quien lo lleve a cabo, le da a las matemáticas su sentido de universalidad y verdad.

Hilbert (1902) buscaba tener una teoría del todo matemática que respondiera al problema de encontrar la verdad o falsedad de cualquier proposición lógica (_das Entscheidungsproblem_). El trabajo de Gödel (1931), Turing (1936) y Church (1936) mostró la incompletitud de las matemáticas y definió las nociones de cómputo e incomputabilidad, mismas que se relacionan con el concepto de decidibilidad de un lenguaje, o de manera equivalente, con mostrar si una proposición es falsa o verdadera.

Para Chaitin (2006), el teorema de la incompletitud es solo la punta del iceberg. A partir de su descubrimiento del número Ω, demostró que existe un número infinito de problemas incomputables e indemostrables a partir de un sistema de axiomas finito. La conexión importante entre Chaitin y su número Ω, para el propósito de este ensayo, se centra en la relación de complejidad dentro de los modelos computacionales y en cómo estos podrían o no encapsular a las leyes naturales.

En el _Discurso de Metafísica_ de Leibniz (1989), en su sección VI, se distingue entre los hechos regulares e irregulares que podemos observar: escribe sobre la ley perfecta que Dios puso en el universo, y sobre la abstracción como herramienta para comprender los hechos regulares (patrones) como leyes naturales que nos ayuden a comprimir su comportamiento para acercarnos al conocimiento. De alguna manera, entender los patrones del mundo exterior, abstraerlos a fórmulas y comprimirlos a modelos más concisos es, para él, nuestra manera de acercarnos al entendimiento de la realidad.

Chaitin (2006) retoma esta noción de compresión desde la teoría algorítmica de la información para hablar de la relación entre el tamaño de un programa y su salida, y la relaciona con los modelos científicos:

> The basic insight is a software view of science: a scientific theory is like a computer program that predicts our observations, the experimental data [...]. A useful theory is a compression of the data; comprehension is compression. You compress things into computer programs, into concise algorithmic descriptions. The simpler the theory, the better you understand something. (Chaitin, 2006, p. 77)

La importancia de Ω es que su comportamiento aleatorio lo hace incomprimible: para calcular N bits de Ω se necesita al menos un programa de N bits de tamaño. Pensando en la idea de Leibniz, esto, para mí, es un límite no solo hacia lo que podemos calcular o demostrar, sino también hacia nuestro entendimiento de la realidad; al menos, esto demuestra la complejidad infinita de las matemáticas y que nuestro entendimiento de ellas nunca será completo, ni siquiera al agregar nuevos axiomas.

> "God plays dice not only in quantum mechanics but also in the foundations of mathematics." (Chaitin, 2012, p. 116)

No solo existen problemas incomputables y hechos incomprimibles: si quisiéramos simular la deducción de un resultado a partir de ciertas hipótesis, o demostrar un problema a partir de ciertos axiomas, también nos encontramos con los límites marcados por la complejidad computacional. La teoría de la complejidad computacional se divide principalmente en dos ejes, la memoria y el tiempo. Existen problemas conceptualmente fáciles, como saber si existe o no un camino de tamaño K para alguna gráfica, o resolver un sudoku; ambos pertenecen a la clase de complejidad NP-completo, lo que implica que un sudoku lo suficientemente grande —algo así como de 50×50— no podría resolverse a lo largo de toda nuestra vida. Formalmente, que un problema sea NP (tiempo polinomial no determinista) implica que su solución es fácil de verificar, pero que el algoritmo que lo resuelve no es polinomial; es decir, el tiempo para encontrar una solución crece exponencialmente. Existe toda una jerarquía de clasificaciones de complejidad, pero por ahora enfoquémonos en cuáles son las consecuencias de que un algoritmo tenga complejidad en tiempo exponencial. Por ejemplo, pensemos en un problema de entrada _n_, con una complejidad de O(2ⁿ); digamos que tenemos una computadora que hace 10⁸ operaciones por segundo, y que el universo tiene aproximadamente 10¹⁸ segundos existiendo. Si corriéramos una computadora actual desde el inicio del universo hasta ahora, haría 10²⁶ operaciones; nos bastaría con que n = 100 para sobrepasar el número de operaciones que una computadora corriendo desde el inicio del universo podría hacer.

Es un hecho que los problemas que se pueden solucionar en el tiempo de nuestra existencia —los problemas de la clase P (resolubles en tiempo polinomial)— son un subconjunto de los NP; es decir, son una cantidad mucho menor que la de las otras clases de complejidad que están por encima de NP. Así que si queremos encontrar algoritmos para simular métodos científicos, estos tienen que ser eficientes. Es extraño pensar que en algún momento podremos descubrir la solución a muchas preguntas científicas conceptualmente más difíciles, si existen problemas simples para los que todavía no encontramos una solución eficiente.

Pensar que existe una cantidad infinita de problemas no computables, y que los problemas que podemos resolver eficientemente son considerablemente menos, no ha sido un obstáculo para suponer que cualquier proceso se puede simular en una computadora (incluso el universo). Deutsch (1985), uno de los principales promotores de un modelo computacional para el universo, argumenta que las leyes matemáticas rigen el comportamiento de la física y que estas serían computables (Piccinini, 2011). Para otros —como Hilary Putnam, David Chalmers o Daniel Dennett— la mente se podría ver como un modelo de cómputo; esta idea se conoce como computacionalismo y ha sido una de las ramas filosóficas con algunas aportaciones al desarrollo de la inteligencia artificial.[^horst]

Si para algunos la mente y el universo son en sí mismos modelos computables, no es extraño pensar en juntar ambas ideas; es decir, en juntar nuestra capacidad cognitiva —que nos ha permitido desarrollar ciencia y explorar una versión codificada del universo— con un programa que pueda establecer hipótesis y construir modelos científicos a partir de ella.

En la siguiente sección, mostraré algunos de los intentos que se han hecho para realizar programas orientados a descubrimientos científicos.

## 3. El desarrollo de la ciencia computacional

Existen modelos científicos que corresponden a nuestra comprensión de la realidad; un ejemplo es el desarrollo de la física, donde las matemáticas juegan un papel crucial. Dichos modelos pueden interpretarse mediante lenguaje, matemáticas, diagramas, iconos, etc., pero se basan en una teoría formal para explicar su consistencia y verdad, fundamentada en la lógica y en la semántica formal.

Muchos de los modelos computacionales actuales que simulan descubrimientos científicos no se basan en pruebas formales, sino que utilizan principalmente heurísticas; es decir, métodos de aproximación estadística. Además, buscan "approximate methods for attempting to cut through data complexity and find patterns" [aproximar métodos para intentar superar la complejidad de los datos y encontrar patrones] (Thagard, 2004, p. 2).

Thagard (2004) hace un interesante resumen de diferentes modelos computacionales creados para intentar simular y contribuir al pensamiento científico desde dos perspectivas diferentes: primero, expone los modelos cognitivos que intentan modelar el pensamiento científico a partir de modelos conexionistas; segundo, habla de modelos de ingeniería de inteligencia artificial, en donde se utilizan algoritmos de manera similar a la minería de datos para encontrar patrones dentro de observaciones numéricas o cadenas de palabras que codifican hipótesis.

Al hablar de modelos cognitivos del pensamiento científico, Thagard se centra en cómo se puede simular la generación de leyes numéricas, la formación de conceptos teóricos, la abducción y la analogía, propiedades que para él son elementos clave en nuestro pensamiento científico. Su modelo, ECHO, utiliza un enfoque conexionista para establecer un vínculo por coherencia (_coherence_) entre hipótesis y evidencias, ambas modeladas como proposiciones lógicas. Thagard (1992) utiliza este modelo para evidenciar la adopción de teorías más consistentes con las observaciones (simulando revoluciones científicas); como ejemplo, modela la coherencia en las proposiciones del modelo de Lavoisier a favor de la teoría del oxígeno.

Por otra parte, se discuten los modelos de inteligencia artificial desarrollados principalmente a partir de algoritmos de aprendizaje automatizado (_machine learning_); este tema es analizado por Thagard (2004) con proyectos de la década de 1990, aunque se han desarrollado muchos más desde entonces. Uno de los ejemplos más famosos es AlphaFold, desarrollado por Google después de la creación de AlphaGo, un proyecto centrado en el desdoblamiento de proteínas con grandes expectativas de aportar nuevos avances en medicina y biología.

Por otra parte, Microsoft tiene un campo de investigación abierto dedicado a realizar descubrimientos científicos con IA (AI4Science), y afirma que su uso potenciará el quinto paradigma del descubrimiento científico: siendo el primer paradigma la observación, el segundo la concepción de una teoría de modelos naturales —como la _Philosophiæ Naturalis Principia Mathematica_ de Newton—, el tercero la computación numérica para verificar las ecuaciones de los modelos, y el cuarto el descubrimiento científico intensivo basado en análisis de datos (Bishop, 2022).

El principal pilar para intentar potenciar la ciencia con inteligencia artificial ha sido simular los siguientes elementos: la formación de hipótesis, el diseño experimental, y la recopilación y análisis de datos. La reciente adopción de la IA en la ciencia ha aportado contribuciones como, por ejemplo: el mejoramiento del pronóstico del tiempo, la optimización del diseño de baterías, el control magnético de reactores de fusión nuclear, la planificación de rutas de síntesis química, solucionadores neuronales de ecuaciones diferenciales, la planificación de ubicación de centrales hidroeléctricas, la generación de registros médicos electrónicos sintéticos, la selección de eventos en colisiones de partículas, el modelado de lenguaje para secuencias biomédicas, y más (Wang et al., 2023).

> In AI-driven scientific discovery, scientific knowledge can be incorporated into AI models using appropriate inductive biases, which are assumptions representing structure, symmetry, constraints and prior knowledge as compact mathematical statements. However, applying these laws can lead to equations that are too complex for humans to solve, even with traditional numerical methods. (Wang et al., 2023, p. 48)

Hago uso de la cita anterior para evidenciar que, incluso en la incorporación actual de la inteligencia artificial, estos modelos no logran comprimir del todo las observaciones científicas a modelos más simples que podamos entender. Retomando la manera en que Leibniz (1989) lo expresa: si derramamos tinta en una hoja y obtenemos puntos arbitrarios, podremos encontrar una expresión matemática —dígase una función, utilizando métodos numéricos— que exprese el comportamiento de dichos puntos. Con esto estaríamos encontrando una "ley natural" que, en realidad, no expresa nada. Una función que, si bien predice los puntos que encontremos, deja de lado el significado dentro de ella.

Aaronson (2011), en el capítulo siete de su artículo, "PAC-Learning and the Problem of Induction", retoma el problema de la inducción de David Hume y la navaja de Occam. Creo que es interesante plantear el problema de la inducción al hablar de modelos predictivos: incluso si encontramos un algoritmo que predice con corrección observaciones de uno, dos o tres años, ¿cómo podemos garantizar que haga lo mismo en el siguiente siglo? La otra idea es que los modelos de IA utilizan grandes expresiones matemáticas para predecir sus hipótesis, lo cual contradice la idea de la navaja de Occam, que básicamente dice que las explicaciones más simples son mejores. Aunque este no es un principio probado, en cierto modo es similar a la idea de Chaitin y Leibniz sobre que las leyes naturales tienen que ser simples. En el resto del capítulo, Aaronson (2011) explica una aproximación matemático-formal al principio de la navaja de Occam utilizando el _PAC (Probabilistically Approximately Correct) Learning_ de Leslie Valiant.

Volviendo a Thagard (2004): en su artículo hace una distinción entre simular un descubrimiento y encontrar evaluaciones consistentes del modelo, es decir, tratar de justificar la corrección de los modelos; y al final, habla sobre el límite que nos impone la complejidad computacional, y da una interesante analogía entre la teoría del aprendizaje formal y los modelos científicos como programas de software:

> Scientific discovery can be viewed as a problem in formal-learning theory, in which the goal is to identify a language given a string of inputs (Gold 1968). Analogously, a scientist can be thought of as a function that takes as input a sequence of formulas representing observations of the environment and produces as output a set of formulas that represent the structure of the world (Jain, Osherson, Royer, & Sharma 1999; Kelly & Glymour 1989; Martin & Osherson 1998; Osherson & Weinstein 1989). (Thagard, 2004, p. 2)

Contrario a esta analogía entre un programa y un modelo científico, podríamos decir que encontrar un modelo que encaje en el mundo corresponde a una codificación y decodificación de la realidad a partir de un sistema formal, pero este sistema podría no ser necesariamente computable. Esta idea corresponde con la epistemología de Rosen (1987) y con sus trabajos posteriores, donde escribe sobre cómo tratar de encontrar un modelo que represente a la vida. En pocas palabras, Rosen (1991) utiliza el formalismo de la teoría de categorías y da un modelo relacional para entender la vida; su modelo utiliza algunas propiedades autorreferenciales que lo hacen no computable.

## 4. ¿Seguimos buscando significado o predictibilidad?

_Esta sección está en forma de esquema/notas de lectura en el original y no se desarrolló como texto corrido; la dejo tal cual para que decidas cómo redactarla, en vez de inventar el argumento por ti:_

- The end of philosophy, Heidegger
- Toward a critical social theory of AI: Knowledge, information, and intelligence in the later works of André Gorz
- La revolución tecnocientífica
- The wisdom of ancients (De Sapientia Veterum), Francis Bacon
- El problema de la caja negra y la explicabilidad de la inteligencia artificial (_Explainable AI_)
- Teoría de modelos epistémicos de Robert Rosen en el concepto de modelos explicativos para la ciencia
- La inteligencia artificial o el desafío del siglo, Eric Sadin
- Aunque la IA no sea solo una reducción instrumentalista de la cognición, las propiedades emergentes que pudieran existir en una red neuronal no implican cognición: el problema del significado y de la construcción de la semántica en una máquina abstracta sigue sin resolverse. Fuente: _Instrumental Reason, Algorithmic Capitalism, and the Incomputable_ (Parisi, 2015) y _Minds, Brains, and Programs_ (Searle, 1980).

## 5. Conclusiones

Desde mi punto de vista, existe la esperanza de que la IA nos ayude a responder las grandes preguntas sin respuesta de la ciencia, como el origen de la vida, la teoría del todo para la física, el entendimiento de nuestro propio pensamiento, o preguntas dentro de la misma computación, como ¿NP = P? Creo que las expectativas hacia la IA rebasan sus límites, y que su uso sigue siendo una manera optimista de pensar que la tecnología solucionará otros problemas sociales, como el cambio climático, la salud, la reducción del uso de energía y la distribución de los recursos naturales. Espero que, en las próximas décadas, se siga persiguiendo un entendimiento del mundo en lugar de buscar un modelo predictivo que solo eficientice procesos. Existen problemas irresolubles dentro del poder de una máquina; me parece extraño pensar, con optimista ilusión, que solo es cuestión de tiempo para desarrollar una inteligencia artificial general que nos ayude a entender nuestra consciencia, el universo o la vida. Tratar de entender estos tres ha sido uno de los motores del desarrollo de la ciencia; sería una lástima olvidarlo en el camino de tratar de ajustar una curva a puntos arbitrarios en una hoja de papel.

---

## Bibliografía

Aaronson, S. (2011). _Why philosophers should care about computational complexity_. Preprint para _Computability: Turing, Gödel, Church, and beyond_. MIT Press.

Bishop, C. (2022). _AI4Science to empower the fifth paradigm of scientific discovery_. Microsoft Research. https://www.microsoft.com/en-us/research/blog/ai4science-to-empower-the-fifth-paradigm-of-scientific-discovery/

Buckner, C., & Garson, J. (2019). Connectionism. En E. N. Zalta (ed.), _The Stanford Encyclopedia of Philosophy_ (edición de otoño de 2019). https://plato.stanford.edu/archives/fall2019/entries/connectionism/

Chaitin, G. (2006). The limits of reason. _Scientific American, 294_(3), 74–81.

Chaitin, G. (2012). _Conversations with a mathematician: Math, art, science and the limits of reason_. Springer.

Church, A. (1936). A note on the Entscheidungsproblem. _Journal of Symbolic Logic, 1_, 40–41.

Deutsch, D. (1985). Quantum theory, the Church-Turing principle and the universal quantum computer. _Proceedings of the Royal Society of London, Series A, Mathematical and Physical Sciences, 400_(1818), 97–117. https://doi.org/10.1098/rspa.1985.0070

Dong, Q., Dong, L., Xu, K., Zhou, G., Hao, Y., Sui, Z., & Wei, F. (2023). _Large language model for science: A study on P vs. NP_. arXiv preprint arXiv:2309.05689.

Gödel, K. (1931). Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I. _Monatshefte für Mathematik und Physik, 38_(1), 173–198.

Hilbert, D. (1902). Mathematical problems. _Bulletin of the American Mathematical Society, 8_(10), 437–479.

Leibniz, G. W. (1989). _Discourse on metaphysics: 1686_ (pp. 303–330). Springer Netherlands.

Piccinini, G. (2011). The physical Church–Turing thesis: Modest or bold? _The British Journal for the Philosophy of Science, 62_(4), 733–769.

Rescorla, M. (2020). The computational theory of mind. En E. N. Zalta (ed.), _The Stanford Encyclopedia of Philosophy_ (edición de otoño de 2020). https://plato.stanford.edu/archives/fall2020/entries/computational-mind/

Rosen, R. (1987). Some epistemological issues in physics and biology. En B. J. Hiley & F. D. Peat (eds.), _Quantum implications: Essays in honour of David Bohm_ (pp. 314–327). Routledge.

Rosen, R. (1991). _Life itself: A comprehensive inquiry into the nature, origin, and fabrication of life_. Columbia University Press.

Searle, J. R. (1980). Minds, brains, and programs. _Behavioral and Brain Sciences, 3_(3), 417–457.

Sipser, M. (2005). _Introduction to the theory of computation_ (2a ed.). Course Technology.

Soto-Astorga, E. F. (2022). _Sistemas de metabolismo-reparación: Una implementación exploratoria en programación orientada a objetos_.

Thagard, P. (1992). _Conceptual revolutions_. Princeton University Press.

Thagard, P. (2004). Computing in the philosophy of science. En L. Floridi (ed.), _The Blackwell guide to the philosophy of computing and information_ (pp. 307–317).

Turing, A. M. (1936). On computable numbers, with an application to the Entscheidungsproblem. _Proceedings of the London Mathematical Society, 42_(2), 230–265.

Wang, H., Fu, T., Du, Y., et al. (2023). Scientific discovery in the age of artificial intelligence. _Nature, 620_, 47–60. https://doi.org/10.1038/s41586-023-06221-2

[^horst]: En el original citas aquí a "Horst, 2015" para el computacionalismo, pero esa referencia no aparece en la bibliografía y no la pude verificar. ¿Es posible que te refirieras a Rescorla (2020), "The Computational Theory of Mind", que sí está en tu bibliografía y trata exactamente este tema? Revísalo y complétalo con la fuente correcta.