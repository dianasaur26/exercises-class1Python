# -*- coding: utf-8 -*-
"""Copy of Sesión Hack Women- Intro a Python

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xiYr-p23PhU_jztzB9ZHh0Yb3B21Q-Xa

# Introducción a Python

A lo largo de este cuaderno explicaremos algunos conceptos básicos de Python. Los temas específicos que cubriremos en estos cuadernos introductorios son los siguientes:

1. ¿Qué es Python?
2. Objetos avanzados: _Listas_ y _diccionarios_
3. Empaquetando código - _Funciones_

### Planteamiento del problema:

Imagina que queremos crear un directorio que contenga toda la información de los estudiantes de nuestro club. Para ello, necesitaremos construir paso a paso la idea completa del proyecto.

Para ello, necesitamos saber sobre tipos de variables, objetos avanzados como listas y diccionarios, cómo crear funciones para operar algunos valores y cómo crear nuevos objetos.


## ¿Qué es Python?

<center>
    <img width="50%" src="https://www.python.org/static/community_logos/python-logo-generic.svg">
</center>

Python es un lenguaje de programación **interpretado**, lo que significa que un _interpretador_ ejecuta y ejecuta su código línea por línea en lugar de compilarlo. Python tiene una sintaxis elegante que te obliga a **aplicar sangría a tu código para construir bloques de código**, por lo que Python no usa `{}` para bloques de código. No es común usar punto y coma en Python (`;`) al final de cualquier oración. Otra cosa interesante de Python es que no necesita declarar variables, solo las define, y sucede que Python **se escribe dinámicamente**.

### Hola mundo en Python

Usaremos las funciones de entrada y salida de Python para crear nuestro primer hola mundo.

Solo necesita ejecutar la siguiente celda con código presionando el botón _play_ o presionando `Shift + Enter` en su teclado.

## Variables

Python tiene varios tipos de variables de forma nativa. Comenzando con variables numéricas, Python puede trabajar con números enteros, números flotantes y números complejos. También cuenta con cadenas de caracteres para trabajar con texto y otro tipo de variables llamadas booleanos para guardar valores binarios.

La forma en que declaramos las variables es la siguiente:

```python
variable_name = <value>
```

El nombre de una variable no puede tener espacios, debe comenzar con una letra, puede contener letras mayúsculas o números dentro del nombre.

#### Ejemplo:

```python
my_dog = "Mirlo"
```

Para obtener el tipo de una variable, podemos usar la función `type ()` y pasar como parámetro la variable que queremos conocer.

#### Ejemplo:

```python
type(my_dog)
```

Hay varios tipos de variables, ¡incluso números complejos en Python!

#### Ejercicio:

Define e imprime el tipo y valor de las variables denominadas:
- `name`, debe ser un` <str> `que contenga cualquier nombre
- `age`, debe ser un` <int> `que contenga cualquier edad
- `pi`, debe ser un` <float> `que contenga su mejor aproximación a pi
- `modulus_one`, debe ser un `<complex>`que tiene [módulo](https://en.wikipedia.org/wiki/Absolute_value#Complex_numbers) uno

## Control de flujo (condicionales)

Hasta ahora, sabemos cómo definir variables, por lo que podemos crear bloques de código un poco más avanzados. Lo primero que queremos hacer es crear una nueva variable llamada `under_age` y necesitaremos definirla usando una declaración contitional. Para ello, será útil recordar los operadores de comparación (`<, >, <=, >=, ==, !=`).

La idea es la siguiente, si la persona es menor de edad, el valor de esta variable será "Verdadero" y será "Falso" en el otro caso.

Para declarar una declaración condicional, se usa la siguiente sintaxis:

```python
if condition:
    # Block of code for a satisfied condition 
else:
    # Block of code for a non-satisfied condition 
```

#### Ejemplo:
"""

dog_color = "black"
if color == "black":
    print("Indeed, this dog is black.")
else:
    print("Nope, it is not a black dog.")

"""## Bucles (ciclos)

**Iteración** significa ejecutar el mismo bloque de código una y otra vez, potencialmente muchas veces. Una estructura de programación que implementa la iteración se llama **bucle** (o **ciclo**).

Hay dos tipos de iteración:
- **Iteración definida**, en la que el número de repeticiones se especifica explícitamente de antemano
- **Iteración indefinida**, en la que el bloque de código se ejecuta hasta que se cumple alguna condición

En Python, la iteración indefinida se realiza con un ciclo `while` y la iteración definida se realiza con un ciclo `for`.

### Ciclo `while`

Para un ciclo `while` será importante **establecer una condición de parada**. El formato de un ciclo `while` se muestra a continuación:

```python
while condition:
    # Code goes ehre!
```

#### Ejemplo:

"""

n_interation = 1

while n_iteration <= 10:
    print(f"Iteration {n_iteration}.")

"""### Ciclo `for`

Python tiene un **ciclo basado en colecciones** o **ciclo basado en iteradores**. Este tipo de bucle itera sobre una colección de objetos, en lugar de especificar valores numéricos o condiciones:

```python
for i in <collection>:
    <loop body>
```

#### Ejemplo:

Podemos iterar a través de los elementos de una lista:

"""

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]

for month in months:
    print(f"The current month is {month}.")

"""O iterar solo a través de un rango de números:"""

for number in range(10):
    print(f"The current number is {number}.")

"""**Nota:** *¿Todo esto aplica para las tuplas?*

## Diccionarios

Python proporciona otro tipo de datos compuestos llamado **diccionario**, que es similar a una lista en que es una colección de objetos.

Los diccionarios son diferentes de las listas principalmente por cómo acceder a sus elementos:

- Se accede a los elementos de la lista por su posición en la lista, mediante indexación.
- Se accede a los elementos del diccionario mediante llaves o claves (pares clave-valor).
"""

student = {
    "name": "Jesús López",
    "email": "algo@gmail.com"
}

student['email']

student['age']=23

print(student)

student.keys()

for key in student.keys():
  print(student[key])

student.items()

for key, value in student.items():
  print(key,value)

"""## Funciones

Las funciones nos permitirán empaquetar código que puede ser invocado a través de una línea con el nombre de la función.

La estructura básica de una función es como sigue:

```python
def name_of_function(arguments):
    # Code of the function

    return something
```

La nomenclatura de las funciones es consistente con la de las variables.
"""



# Implement the 2nd of the Newton's laws of motion

def F(m,a):
  fuerza = m * a
  return fuerza

print(f"{F(70,9.81)} N (Newton)")

"""#Ejemplo 1
-  Procedimiento CalcularMaxMin: recibe una lista de enteros  y devuelve
el máximo y el mínimo de los números guardados en el vector.
Parámetros de entrada: lista de enteros
Valores de salida: valor máximo y mínimo
"""

# Ejemplo 1

import random 
def CalcularMaxMin(lista):
  return(max(lista),min(lista))
numeros = []
for i in range(10):
  numeros.append(random.randint(1,101))
vmax, vmin = CalcularMaxMin(numeros)
print("El valor maximo es: ", vmax)
print("El valor minimo es: ", vmin)

"""#Ejemplo 2

- Función CalcularAreaPerimetro: recibe el radio de una circunferencia y
devuelve el área y el perímetro.
Parámetros de entrada: radio (real)
Valores de salida: área y perímetro (real)
"""

# Ejemplo 2
import math

def CalcularAreaPerimetro(radio):
  area = math.pi * radio ** 2
  perimetro = 2 * math.pi * radio
  return area,perimetro
radio = float(input("Introduce el radio: "))
area, perimetro = CalcularAreaPerimetro(radio)
print("Area: ", area)
print("Perimetro: ", perimetro)

"""# Ejemplo 3

- Función centrar: Recibe una cadena y la imprime centrada en la pantalla.
"""

#Ejemplo 3
def centrar(cad):
  print("" * int(40 - (len(cad)/2)),cad)
  print("" * int(40 - (len(cad)/2)),"=" * len(cad))

mensaje1 = "HackWomen"
centrar(mensaje1)
mensaje2 = "Skills for Women in Tech"
centrar(mensaje2)

"""# Ejemplo 4

- Función Convertir a  segundos: Recibe una cantidad de horas, minutos y segundos y calcula a cuantos segundos corresponde.
"""

# Ejemplo 4
def Convertir_A_Segundos(h, m, s):
  return h * 3600 + m * 60 + s

def Convertir_A_HMS(seg):
  h = seg/3600 
  seg = seg - h * 3600
  m = seg / 60
  seg = seg -60
  return h,m,seg

while True:
  print("1. Convertir a segundos")
  print("2. Convertir a horas, minutos y segundos")
  print("3. Salir")

  opcion = int(input())
  if opcion == 1:
   hor = int(input("Horas"))
   minu = int(input("Minutos:"))
   seg = int(input("Segundos: "))
   print("Corresponde a ", Convertir_A_Segundos(hor,minu,seg),"segundos")
  elif opcion ==2:
    segund = int(input("Segundos"))
    hor, minu, seg = Convertir_A_HMS(segund)
    print("Corresponde a ", hor,":",minu,":",seg)
  elif opcion == 3:
    break
  else:
    print("opcion correcta")

"""# Ejemplo 5

- Función ValidarFecha: Recibe un día, mes y año correspondiente a una fecha y  devuelve si la fecha es correcta o no.
Simplemente miramos si el día indicado es mayor que 1 y menor que los días del mes. Si introducimos un mes incorrecto, la función DiasDelMes devuelve 0 por lo tanto la fecha va a ser incorrecta.
Parámetros de entrada: día, mes y año
-  Dato devuelto: Valor lógico indicando si es correcta (Verdadero) o no (Falso)
"""

#Ejemplo 5
from datetime import date
from datetime import datetime
from calendar import monthrange
import calendar

while True:
  print("Put the date with numbers")
  dayRead = int(input("Day: "))
  monthRead = int(input("Month: "))
  yearRead = int(input("Year: "))
  if dayRead > 0 and dayRead<=calendar.monthrange(now.year, now.month)[1] and dayRead == today.day:
    if monthRead == today.month:
      if yearRead == today.year:
        now = datetime.now()
        format = now.strftime('Day :%d, Month: %m, Year: %Y')
        print(format)
        break;
  else:
    print("the date that you put it is not correct, try again!")

"""## ¡A resolver el reto!


Vamos a prodecer a crear una lista de diccionarios, esto es, un directorio de estudiantes de SKILLS FOR WOMEN IN TECH que participarán en una edición en línea.

Cada estudiante debe tener los siguientes atributos:
- Nombre <str>
- Edad <int>
- Temas <lista>
- Menores de edad <bool>

Puedes asignar los datos a mano o utilizar funciones aleatorias para llenar los campos.
"""


# All your code goes here!!!
subjects = []
  
print("Welcome to the jungle, you can register here!")
nameRead = input("your awesome Name: ")
ageRead = int(input("your age: "))
subjectRead = input("your favorite programming language: ")
subjects.append(subjectRead)
while True:
  print("Do you want to add other subject?")
  print("press 1 to add other subject")
  print("press enter to finish your process")
  option = input()
  if(option == '1'):
    otherSubject = input("other subject: ")
    subjects.append(otherSubject) 
  elif(option == '') : 
    def under_aged ():
      if(ageRead<18):
        print("Yes! You are younger :)")
      else:
        print("OMG definetely, you can buy your own cocktails")
    thisdict = {
    "name": nameRead,
    "age": ageRead,
    "subjects": subjects,
    
    }
    print(thisdict);
    print(under_aged())
    break
"""--------

> Contenido creado por **Jesús López**  2022. <br>
> Contacto: [@jalopez_garcia](https://www.instagram.com/jalopez_garcia/) & [@jalopez_garcia](https://twitter.com/jalopez_garcia)
"""