def selection_sort(arr, ascendente=True):
    n = len(arr)
    for i in range(n):
        indice_extremo = i
        for j in range(i + 1, n):
            if ascendente:
                if arr[j] < arr[indice_extremo]:
                    indice_extremo = j
            else:
                if arr[j] > arr[indice_extremo]:
                    indice_extremo = j
        arr[i], arr[indice_extremo] = arr[indice_extremo], arr[i]
    return arr
