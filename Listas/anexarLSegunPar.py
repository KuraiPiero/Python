## python analiza a i dividido 2 y su residuo, si este da 0 entonces procede, la logica detras de esto es
# usar el metodo de comprobar si es par o no para saltarse 1 elemento, y adicionalmente element puede
# tener nombre el objetivo aqui es tomar ese elemento y luego enexarlo con c que tiene el parametro i que
# i indica la posicion del elemento
def skip_elements(letras):
    new_list = []
    posicionElemento = 0
    for letra in letras:
        if posicionElemento % 2 == 0:
            letraAnexar = letras[posicionElemento]
            new_list.append(letraAnexar)
        posicionElemento += 1
    return new_list


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
print(skip_elements(["Orange", "Pineapple", "Strawberry", "Kiwi", "Peach"]))
print(skip_elements([]))

