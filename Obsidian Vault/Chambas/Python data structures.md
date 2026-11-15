### 1. Listas (`list`)

Colección ordenada y mutable.

python

```python
lista = [1, 2, 3]
```

- `append(x)` – agrega un elemento al final
- `insert(i, x)` – inserta en una posición específica
- `remove(x)` – elimina la primera coincidencia de un valor
- `pop(i)` – elimina y retorna el elemento en índice `i` (por defecto el último)
- `extend(iterable)` – añade varios elementos de otra secuencia
- `sort(key=, reverse=)` – ordena la lista in-place
- `sorted(lista)` – retorna una nueva lista ordenada
- `reverse()` – invierte el orden in-place
- `index(x)` – retorna el índice de la primera coincidencia
- `count(x)` – cuenta ocurrencias de un valor
- Slicing: `lista[1:3]`, `lista[::-1]`
- Comprehensions: `[x**2 for x in lista]`

### 2. Tuplas (`tuple`)

Colección ordenada e inmutable.

python

```python
tupla = (1, 2, 3)
```

- `count(x)` – cuenta ocurrencias
- `index(x)` – encuentra el índice de un valor
- Desempaquetado: `a, b, c = tupla`
- Útiles para claves de diccionario o valores inmutables que no deben cambiar

### 3. Diccionarios (`dict`)

Colección de pares clave-valor.

python

```python
diccionario = {"a": 1, "b": 2}
```

- `get(k, default)` – obtiene valor sin lanzar error si no existe
- `keys()`, `values()`, `items()` – iterar sobre claves, valores o pares
- `update(otro_dict)` – fusiona diccionarios
- `pop(k, default)` – elimina y retorna un valor
- `setdefault(k, default)` – obtiene o inicializa un valor
- Comprehensions: `{k: v for k, v in items}`
- `dict.fromkeys(iterable, valor)` – crea diccionario con claves dadas

### 4. Conjuntos (`set`)

Colección no ordenada de elementos únicos.

python

```python
conjunto = {1, 2, 3}
```

- `add(x)` – agrega un elemento
- `remove(x)` / `discard(x)` – elimina (remove lanza error si no existe, discard no)
- `union(otro)` o `|` – unión de conjuntos
- `intersection(otro)` o `&` – intersección
- `difference(otro)` o `-` – diferencia
- `symmetric_difference(otro)` o `^` – diferencia simétrica
- `issubset()`, `issuperset()` – verificar relaciones de contención
- Muy útil para eliminar duplicados: `set(lista)`

### 5. Cadenas (`str`)

Inmutables, pero con muchos métodos útiles.

- `split(sep)` – divide en lista
- `join(iterable)` – une elementos con la cadena como separador
- `strip()`, `lstrip()`, `rstrip()` – eliminar espacios/caracteres
- `replace(a, b)` – reemplazar subcadenas
- `find(x)` / `index(x)` – buscar subcadena
- `format()` / f-strings – formateo de texto
- `upper()`, `lower()`, `capitalize()`
- `startswith()`, `endswith()`

### 6. Estructuras del módulo `collections`

Muy útiles para casos avanzados:

- `deque` – lista doblemente enlazada, ideal para colas (`appendleft`, `popleft` en O(1))
- `Counter` – cuenta elementos automáticamente (`Counter(lista).most_common(3)`)
- `defaultdict(tipo)` – diccionario con valor por defecto automático
- `namedtuple` – tuplas con campos nombrados
- `OrderedDict` – diccionario que recuerda el orden de inserción (menos necesario desde Python 3.7+)

### 7. Otras estructuras útiles

- `heapq` – implementa una cola de prioridad (min-heap) sobre listas: `heappush`, `heappop`
- `array` (módulo `array`) – arreglos tipados, más eficientes en memoria que listas para números