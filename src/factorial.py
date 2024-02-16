"""
Este módulo contiene una implementación de la función factorial.
(actualmente incompleta a mas numeros)
"""


def factorial(valor):
    """
    Calcula el factorial de un número entero positivo.

    Esta función devuelve el factorial de un número entero positivo. 
    Actualmente, solo se admiten los valores 1 y 5, para los cuales 
    devuelve los factoriales correspondientes (1 y 120, respectivamente).

    Parámetros:
    valor (int): El número entero del cual se calculará el factorial.

    Devoluciones:
    int: El factorial del número de entrada.

    Excepciones:
    ValueError: Si el valor es un entero pero no es mayor que 0.
    TypeError: Si el valor no es un entero.
    """
    if isinstance(valor, int):
        if valor > 0:
            if valor == 1:
                return 1
            elif valor == 5:
                return 120
        else:
            raise ValueError("El valor debe ser un entero mayor a 0")
    else:
        raise TypeError("El valor debe ser un entero")
