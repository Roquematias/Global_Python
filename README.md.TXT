Detector y Manipulador de ADN
Este programa permite trabajar con matrices de ADN representadas en formato de cadenas de texto. Puedes verificar si el ADN contiene mutaciones, aplicar mutaciones específicas o sanarlo, generando una nueva matriz sin mutaciones.

Requisitos
Python 3.7 o superior.
Ninguna biblioteca adicional requerida (se usan tipos de datos nativos).
Estructura del repositorio
El repositorio contiene los siguientes archivos:
.
├── clases.py      # Clases principales: Detector, Mutador, Radiacion, Virus, Sanador.
├── ejecutable.py  # Archivo principal para ejecutar el programa.
├── README.md      # Explicación del funcionamiento y ejemplos de uso.

Como ejecutar el programa
1)Clona el repositorio en tu máquina local:
git clone <URL-del-repositorio>
cd <nombre-del-repositorio>

2)Ejecuta el archivo ejecutable.py con Python:
python ejecutable.py

3)Sigue las instrucciones que aparecen en pantalla.

Instrucciones de uso
1. Selección de la matriz inicial
El programa inicia preguntándote cómo deseas definir la matriz de ADN inicial. Tienes dos opciones:

Ingresar la matriz manualmente: Se te pedirá escribir las filas del ADN (6 filas de 6 bases cada una: A, T, C o G).
Generar la matriz aleatoriamente: El programa generará una matriz de ADN válida automáticamente.
2. Opciones principales del menú
Después de definir la matriz inicial, el programa muestra un menú con estas opciones:

1. Detectar mutaciones
El programa verifica si el ADN contiene mutaciones horizontales, verticales o diagonales (repetición de 4 bases consecutivas). Imprime el resultado y el ADN actual.

2. Aplicar una mutación
Permite introducir mutaciones en el ADN. Se solicitan los siguientes datos:

Tipo de mutación:
"H" para mutaciones horizontales.
"V" para mutaciones verticales.
"D" para mutaciones diagonales.
Base nitrogenada: La base a repetir (A, T, C o G).
Posición inicial: Formato fila,columna (por ejemplo, 0,2).
El programa aplica la mutación en la matriz de ADN y muestra el resultado.

3. Sanar mutaciones
El programa detecta si hay mutaciones en el ADN. Si las encuentra:

Genera un nuevo ADN aleatorio que no contenga mutaciones.
Reemplaza la matriz actual por la nueva.
El ADN actualizado se imprime en pantalla.

4. Salir
Finaliza el programa. Antes de salir, muestra el ADN final y un mensaje de despedida.

Ejemplo de ejecución
Entrada:
Seleccione cómo desea obtener la matriz de ADN:
1. Ingresar manualmente
2. Generar aleatoriamente
Ingrese 1 o 2: 2

Salida:
Matriz de ADN generada aleatoriamente:
AGCTTA
TACGAT
CGTAGC
GTATCG
ATGCTA
CAGTAC

Opciones:
1. Detectar mutaciones
2. Aplicar una mutación
3. Sanar mutaciones
4. Salir
Seleccione una opción (1, 2, 3 o 4): 1

El ADN no contiene mutaciones:
AGCTTA
TACGAT
CGTAGC
GTATCG
ATGCTA
CAGTAC

Buenas prácticas aplicadas
 Código modular: Se separaron las funciones principales para mejorar la legibilidad.
 Documentación: Cada función y clase incluye docstrings explicativos.
 Optimización: Se emplean listas de comprensión y validaciones simples para asegurar una ejecución eficiente.
 Manejo de errores: Las mutaciones incluyen bloques try-except para evitar interrupciones por datos inválidos.

ALUMNO: ROQUE MATIAS MERCADO


