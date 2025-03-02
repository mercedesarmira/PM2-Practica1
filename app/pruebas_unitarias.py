# Pruebas unitarias con pytest

import pytest
from funcion import encontrar_maximo

def test_lista_vacia():
    # Prueba para una lista vacía
    assert encontrar_maximo([]) is None

def test_enteros():
    # Pruebas para listas de números enteros
    assert encontrar_maximo([1, 2, 3]) == 3
    assert encontrar_maximo([-1, -2, -3]) == -1
    assert encontrar_maximo([-1, 1, 2]) == 2

def test_decimales():
    # Pruebas para listas de decimales
    assert encontrar_maximo([1.1, 1.2, 1.3]) == 1.3
    assert encontrar_maximo([-1.1, -1.2, -1.3]) == -1.1
    assert encontrar_maximo([1.1, -1.2, 1.3]) == 1.3

def test_listas_combinadas():
    # Pruebas para listas combinadas
    assert encontrar_maximo([1, 1.1, 2]) == 2
    assert encontrar_maximo([-1, 1.1, 3, -4]) == 3

def test_un_elemento():
    # Prueba para listas de un elemento
    assert encontrar_maximo([1]) == 1

def test_elementos_repetidos():
    # Prueba para listas en las cuales se repiten elementos
    assert encontrar_maximo([2, 1, 3, 3]) == 3
    assert encontrar_maximo([2, 2, 2]) == 2

def test_una_cadena():
    # Prueba para listas con texto:
    with pytest.raises(ValueError, match="Todos los elementos de la lista deben ser números int o float"):
        encontrar_maximo([1, "cadena"])

def test_solo_cadenas():
    # Prueba para listas con solo texto:
    with pytest.raises(ValueError, match="Todos los elementos de la lista deben ser números int o float"):
        encontrar_maximo(["cadena", "prueba"])

def test_otro_caso():
    # Prueba para listas con solo texto:
    with pytest.raises(ValueError, match="Todos los elementos de la lista deben ser números int o float"):
        encontrar_maximo([[1, 3], "prueba"])