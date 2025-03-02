# Función que procesa una lista de datos numéricos

def encontrar_maximo(lista_de_numeros):
    """
    Encuentra el máximo de una lista de números, es decir, devuelve el número más grande de la lista.

    Parameters
    ----------
    lista_de_numeros : list[int|float]
        Lista de datos numéricos
    
    Returns
    -------
    int o float
        El número más grande de la lista. Si la lista está vacía, devuelve None.
    
    Raises
    ------
    ValueError
        Indica si la lista tiene elementos no aceptables.

    Examples
    --------
    >>> encontrar_maximo([3, 2, 5])
    5
    >>> encontrar_maximo([1, 1])
    1
    >>> encontrar_maximo([])
    None
    """
    if not lista_de_numeros: 
        return None
    try:
        return max(lista_de_numeros)
    except TypeError:
        raise ValueError("Todos los elementos de la lista deben ser números int o float")
        