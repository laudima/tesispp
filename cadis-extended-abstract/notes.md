# Working notes removed from main.tex (not for submission)

Moved out of the manuscript on 2026-09-27. Integrate what is useful into Sections 1-4; the rest stays here.

## Note after Section 2 (was line 82)

```latex
How to connect the causal relations of Rosen as a theorical statement to frame why LLMs are not able to reason causally.
```

## Note in Section 3 (was line 100)

```latex
This are parameters that are used to generate the queries, and they are used to analyze the results. The subtypes are the different types of queries that can be generated from a causal graph, and the graph topology is the structure of the causal graph itself.
```

## Draft sections "Background", "CLADDER", "Experimental Setup" (were lines 119-220)

```latex
\section{Background}


Pearl plantea como partida tres habilidades distintas de la cognición: ver, hacer e imaginar
o hipotetizar/anticipar(Rosen). \cite{pearl2018bookOfWhy}
\begin{itemize}
    \item \textbf{Ver - Imitar} Nos ayuda a percibir regularidades las observaciones. Estas
Rosen las pondría como la identificacion de perceptos. 
    \item \textbf{Hacer - Planear} Predecir los efectos provocados por cierta perturbacion en el ambiente
y tomar una decision para obtener el resultado deseado. Esto incluye la habilidad de
tomar herramientas intencionalmente para lograr el objetivo. 
    \item \textbf{Imaginar - Hipotetizar} Cuando tenemos una teoría de porque funciona una herramienta o cuando no, 
podemos hipotetizar y mejorar estas herramientas para futuros escenarios. 
\end{itemize}

Si una de las intenciones de Turing era intentar definir un agente coginitvo en cuanto a
las preguntas que puede responder. La intencion de Pearl aqui plantea, en cada uno de los 
niveles, distintas dificultades. Para Pearl un sistema que realmente presente cognicion 
deberia ser posible de reproducir estos tres tipos de inferencias causales. 

Los tres puntos anteriores representan entonces, la intuicion por detras de la 
formulacion matematica, de dichas relaciones. 

\begin{itemize}
    \item L1. \textbf{Asociativo}. ¿Que pasa si veo ? ¿Como cambiaria mi creencia en Y viendo X? En ejemplos 
    de la vida real sería que me dice un sintoma acerca de una enfermedad ? que me dice el resultado de una encuesta para predecir 
    el resultado final de las elecciones ? 
    \item L2. \textbf{Intervencion}. Que pasaria si hago \dots ? Como seria Y si hago X ? Como puedo hacer que pasae Y ?
    \item L3. \textbf{Contrafactual}. ¿Si tomo una aspirina, se me quitaria mi migraña ?¿Que pasa si prohibimos los cigarros?
\end{itemize}

¿Que es lo que puede hacer un razonador causal?¿Que puede computar un organismo con un modelo causal, 
a falta de el, que le permite predecir? 

Aqui Rosen diferia, en cuanto a que el proceso de inferencia de un organismo, 
no de depende solo de su estructura causal sino tambien viene desde una idea que 
engloba el completo funcionamiento del organismo, definiendo la coginicion y agencia del 
organismo no solo en la estructura causal del fenomeno que se esta tratando de predecir. 

Uno de los objetivos principales de la version fuerte de IA, es reproducir la inteligencia humana. En lugar
de tener una inteligencia genuina, nos encontramos con habilidades impresionantes. La diferencia recae en la falta 
de un modelo de la realidad. 

Muchos de los sistamas de IA se basan especialmente en la asociacion. Toman una colección gigante de observaciones para 
encajar una funcion de la misma manera que un estadista podria querer encajar una linea para pasar por una 
coleccion de puntos. Esto pone una barrera, para que los sistemas puedan ser capaces de reaccionar a circunstancias fuera del 
dataset. Como en los coches de manejo automatico, ¿que pasa si nos encontramos por accidente una vaca en la carretera, un bache
o un borracho ?¿Como podemos hacer un deduccion generalizada? Esta falta de flexibilidad y adaptacion es ineblitable 
en la primerca jerarquia causal. 

\section{CLADDER}

Causal Inference Engine. 

Data sets are in the form of $D := \{q_i, a_i, e_i \}$, where $q_i$ is a query, $a_i$ is the answer, and $e_i$ is the explanation. The experiment consist in translating the query $q_i$ into a prompt $p_i$ and then sending it to the LLM, $f : q_i \rightarrow p_i$. All the statements contain a Formal part, and a natural language part. 

The LLM will return an answer $a'_i$ and an explanation $e'_i$. The answer $a'_i$ is compared with the ground truth answer $a_i$ to determine if the LLM answered correctly or not. The explanation $e'_i$ is compared with the ground truth explanation $e_i$ to determine if the LLM explained correctly or not. The results are stored in a data frame for further analysis.

All the queries contain statements in the three rungs, and are constructued with binary variables. Each query contain 
three or four nodes to mitigate the lack of mathmatical and large processing mistakes LLMs can make. 

The Causal Cot promt divides the queries in this steps, inspired by 
making a CI engine plugin to aument the LLMs capabilities. The workflow consist in the following steps:

\begin{itemize}
    \item causal graph extration
    \item correct query type interpretation 
    \item symbolic formalization of the query 
    \item semantic parsing to compile the available data
    \item stimand derivation 
    \item arithmetic calculation 
\end{itemize}

As the statements where algorithmically generated, gramatical errors where analyzed using the LanguageTool API, 1.26 grammatical errors per 100 words (98.74\%  accuracy).

Other research effords have focus in checking causality as knowladge, causality as language comprehension, 
and causality as reasioning. 

Other examples of commonsense causality includes 
\begin{itemize}
    \item cause and effect of an agent action 
    \item motivation and emotional reaction in social context 
    \item correspondance of a set of steps with a high level goal
    \item development of a story given a different beginning 
    \item knowladge base for causality 
    \item infer causation from correlation 
\end{itemize}

Remark the importance of causality in policy, desicion making, epidemiology, economics, fairness, and explicability. 

\section{Experimental Setup}

Using Gemma4, Qwen3.6-35B-A3B, Nemotron 3 Super 120B-A12B, Mistral Medium 3.5 128B, DeepSeek-V4-Flash. Open source LLMs, and GPT-4. To compare the performance of the LLMs, we will use the CLADDER benchmark, which contains 10,000 queries in the three rungs of Pearl's ladder. The queries are divided into three levels: L1, L2, and L3. Each level contains a set of queries that test the LLM's ability to reason about causality. 

To mitigate data contamination, we will translate the queries into Spanish, and then back into English using a different LLM. This will ensure that the queries are not present in the training data of the LLMs being tested.  

```
