# index es la posicion de la letra asi que no escribimos posicionElemento
# con este cambio ya no es necesario invocar varias veces la variable posicionElemento
# por ende pondemos utilizar append() de forma directa pasando letra como la letra a anexar
def skip_elements(letras):
    new_list = []
    for index, letra in enumerate(letras):
        if index % 2 == 0:
            new_list.append(letra)
    return new_list


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
print(skip_elements(["Orange", "Pineapple", "Strawberry", "Kiwi", "Peach"]))
print(skip_elements([]))
