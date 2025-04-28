def selection_sort(lista_ordenar, ascendente=True):
    """
    Esta es una funcion que ordena por seleccion, es decir, intercambia elementos segun su posicion para
    ordernar la lista que se le mande.

    :param lista_ordenar: Lista a ser ordenada con la funcion
    :param ascendente: Este se utiliza para definir si la lista debe ordenarse de menor a mayor o viceversa.
    :return: Este retorna la lista ordenada
    """

    n = len(lista_ordenar)
    for i in range(n):
        indice_extremo = i
        for j in range(i + 1, n):
            if ascendente:
                if lista_ordenar[j] < lista_ordenar[indice_extremo]:
                    indice_extremo = j
            else:
                if lista_ordenar[j] > lista_ordenar[indice_extremo]:
                    indice_extremo = j
        lista_ordenar[i], lista_ordenar[indice_extremo] = lista_ordenar[indice_extremo], lista_ordenar[i]
    return lista_ordenar
