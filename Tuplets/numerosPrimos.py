def nPrimos(numeros):
    "Aqui inicializamos con el primer numero primo"
    factores = 2
    "El bucle se ejecutara hasta que el factor sea mas grande que el numero"
    while factores <= numeros:
        "Validaremos si la division del factor y el numero da 0 c"
        if numeros % factores == 0:
            "Si da cero va a dividir e imprimir los factores"
            print(factores)
            numeros = numeros / factores
        else:
            "Si la division deja residuo se incrementara en 1 el factor"
            factores += 1
    return "Hecho"


nPrimos(1500)

