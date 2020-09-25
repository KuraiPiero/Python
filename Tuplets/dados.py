import random

Q = str(input("¿Desea tirar los dados?(S/N):"))
while Q == "s":
    dado1 = int(random.random() * 7)
    dado2 = int(random.random() * 7)
    suma = dado1 + dado2
    print(f"Los dados giraron y calleron: {dado1} y {dado2}; su suma es {suma}")
    Q = str(input("¿Desea tirar los dados?(S/N):"))

