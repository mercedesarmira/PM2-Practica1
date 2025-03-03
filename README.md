# Práctica 1

*Angela Mercedes Armira Atz, carné: 202003111*

## Descripción
Este proyecto consiste en una función que encuentra el máximo de una lista de números, pruebas unitarias para validar su funcionamiento y una API REST para exponerla.  
  
Esta practica permite aplicar los conocimientos de:  
• Principios de ingeniería de software.  
• Uso de Git y GitHub.  
• Pruebas unitarias en Python.  
• Código limpio y buenas prácticas.  
• Documentación del código con docstrings.  
• Creación y consumo de una API REST con Flask.

## Estructura
- `funcion.py`: Contiene la función *encontrar_maximo*.
-  `pruebas_unitarias.py`: Pruebas unitarias para la función.
- `api.py`: Contiene la API que expone la función.
- `consumir_api.py`: Código para consumir la API.
- `consumir_entrada.py`: Código para consumir la API solicitando la lista de números al usuario.
  
## Desarrollo
- Se diseñó una función que devuelve el máximo de una lista numérica, es decir, el número más grande de la lista. La función toma una lista de números que pueden ser enteros o flotantes y devuelve el más grande.  

- Se escribieron pruebas unitarias con *pytest*. Se validó el funcionamiento adecuado de la función, gracias a las pruebas fueron evidentes algunos detalles de la función que necesitaban mejora.
  
- Se creó una API usando Flask para exponer la función _encontrar_maximo_, se utilizó el método POST. Luego por medio de requests se hizo el consumo de la API.
  - Se puede consumir con el código en *consumir_api.py*. Al consumir devuelve un JSON que contiene la respuesta deseada. Para procesar otras listas, se debe editar el código.
  - También se puede consumir con el código en *consumir_entrada.py*, al correrlo solicita al usurario la lista de números a procesar.
