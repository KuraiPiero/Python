def sum_divisors(n):
    "Se inicializan las variables Suma y C del contador"
    sums = 0
    c = 1
    "Comparamos n para que este sea mayor a 0 para no entrar en bucle, y el bucle finalizara cuando n sea menor a c"
    while (n > 0) and (c < n):
        "si la division de c y n no da residuo se sumara la Suma y C"
        if n % c == 0:
            sums += c
        "aumentaremos c en 1 hasta cumplir la condicion, este sera nuestro break"
        c += 1

    return sums


print(sum_divisors(6))  # prints 6
print(sum_divisors(12))  # prints 16
print(sum_divisors(0))
# 0
print(sum_divisors(3))  # Should sum of 1
# 1
print(sum_divisors(36))  # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102))  # Should be sum of 2+3+6+17+34+51
# 114
