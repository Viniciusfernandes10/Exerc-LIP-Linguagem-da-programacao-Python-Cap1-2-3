def conjunto_numeros():
    numeros = set()  

    for i in range(5):
        valor = int(input())
        numeros.add(valor)

    return numeros

numeros = conjunto_numeros()
print(numeros)