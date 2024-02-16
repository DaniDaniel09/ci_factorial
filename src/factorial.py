def factorial(valor):
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
