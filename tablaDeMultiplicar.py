def multiplication_table(number):
    "Este es el multiplicador, obviamente el primero es 1"
    multiplier = 0
    "Este es la condicion, por ejemplo si lo queremos multiplicar hasta por 10"
    for i in range(0, 100):
        result = number * multiplier
        "Este es opcional"
        if result % 7 != 0:
            pass
        elif result > 100:
            break
        print(str(result))
        "Este sera el numero a iterar toda la operacion hasta cumplicar la condicion"
        multiplier += 1


multiplication_table(7)
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

