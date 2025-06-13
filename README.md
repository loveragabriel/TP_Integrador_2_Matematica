# Trabajo Integrador 2: Matemática y Programación en Python

## Introducción

Este es el código para el Trabajo Integrador 2, donde integramos matemática con programación usando Python. La idea fue trabajar con conjuntos y lógica, aplicando operaciones con conjuntos basados en los DNI de los integrantes del grupo.

Además, cumplimos con las consignas de manipular dígitos, hacer cálculos con ellos y evaluar condiciones lógicas para mostrar resultados que reflejen esas operaciones matemáticas.

---

## Cómo funciona el programa

1. **Ingreso de datos:**  
   Se piden dos DNIs sin puntos. Cada DNI se procesa para extraer los dígitos únicos y crear conjuntos.

2. **Operaciones con conjuntos:**  
   Se calcula la unión, intersección, diferencias (en ambos sentidos) y diferencia simétrica entre los conjuntos formados.

3. **Frecuencia de dígitos:**  
   Se cuenta cuántas veces aparece cada dígito dentro de cada DNI y se muestra por pantalla.

4. **Suma de dígitos:**  
   Se suman todos los dígitos de cada DNI.

5. **Evaluación de condiciones lógicas:**  
   El programa verifica si hay dígitos compartidos entre los conjuntos y si alguno tiene alta diversidad numérica (más de 6 elementos).

---

## Cómo ejecutar el programa

1. Ubicarse en la carpeta del archivo conjunto.py o anios.py
2. Abrir terminal  
3. Ejecutar programa de conjuntos
   ```bash
   python3 conjunto.py
2. Ejecutar programa de años:
   ```bash
   python3 anios.py
---


## 👤 Gabriel Lovera

**Tareas realizadas:**
- Investigación bibliográfica para el contenido del trabajo.
- Desarrollo de función union_conjuntos en Python, que permite calcular la unión de varios conjuntos a partir de los dígitos de los DNI ingresados, segurando que no haya elementos duplicados.
- Presentación de Operaciones de Conjuntos (unión, intersección, diferencia, diferencia simétrica y Lógica Proposicional).

---

## 👤 Juan Cruz

**Tareas realizadas:**
- [Especificar tareas]
> Elaboración y explicación del marco teórico de conectores lógicos.
> Desarrollo y explicación de operaciones de conjuntos y lógica proposicional
> Desarrollo de la función `diferencia_conjuntos()` en Python.
- [Especificar tareas]
> En el análisis de lógica proposicional se abordamos conectores fundamentales como la conjunción (∧), disyunción (∨), negación (¬) e implicación (→), estableciendo su paralelismo con estructuras condicionales en Python como and, or, not e instrucciones if.
> En el desarrollo de la función diferencia_conjuntos, se implementé una lógica booleana que evalúa si una condición se cumple en uno o varios conjuntos.  
> Por ejemplo: La expresión if numero in conjuntos[i] actúa como una proposición lógica: si se cumple, se interpreta como verdadera.
> La verificación de que un número no pertenece a ningún otro conjunto se asimila a una conjunción de negaciones (¬P ∧ ¬Q ∧ ¬R...), lo cual justifica su inclusión en el resultado.
> Combiné estructuras condicionales e iterativas para simular la operación de diferencia entre conjuntos (A - B), aplicando de forma práctica los conceptos teóricos abordados en la materia.



---

## 👤 Fabricio Lopez

**Tareas realizadas:**
- Desarollo de la funcion interseccion de conjuntos 
- Aportes y correcciones de funciones general 
- Diagrama de venn

---

## 👤 Gastón Lell

**Tareas realizadas:**
- Investigación bibliográfica para el contenido del trabajo.
- Estructura general del proyecto
- Modularización y abstracción de funciones
- Con relación a la materia Matematica realizó las siguientes funciones:
   > Funcionalidad **Producto cartesiano**: La función recibe los conjuntos con los que realizara el producto cartesiano
   y a través de iteraciónes realizadas con el bucle for a cada conjunto devuelve el resultado
   > Funcionalidad **Diferencia simétrica de conjuntos**: La función recibe los conjuntos con los que realizara la diferencia simétrica y a través de diferentes iteraciones evaluará cuales son los elementos que se repiten, descartando esos elementos y devolviendo un conjunto con los elementos no repetidos entre conjuntos.


## 🛠️ Tecnologías principales

- Python
