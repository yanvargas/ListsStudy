# Lista encadeada:

É uma coleção de elementos, onde cada elemento tem um valor e uma referência para o próximo elemento da lista.
Exemplo:
    
    elemento1 = 5
    
    elemento2 = 8
    
    elemento3 = 12
    
    elemento1 -> elemento2 -> elemento3 -> None

# Lista circular:

Similar à lista encadeada, mas o último elemento tem uma referência para o primeiro, formando um ciclo.
Exemplo:

    elemento1 = 3
    
    elemento2 = 6
    
    elemento3 = 9
    
    elemento1 -> elemento2 -> elemento3 -> elemento1

# Pilhas:

Uma estrutura de dados onde o último elemento inserido é o primeiro a ser removido (LIFO - Last In, First Out).
Exemplo:

    pilha = [2, 5, 7]
    
    pilha.pop()  #Retira o número 7 (último adicionado)

# Filas:

Similar a uma fila do supermercado: o primeiro elemento inserido é o primeiro a ser removido (FIFO - First In, First Out).
Exemplo:

    fila = [4, 6, 1]
    
    fila.pop(0)  # Remove o número 4 (primeiro adicionado)

# Árvores:

Uma estrutura hierárquica onde cada elemento tem um pai e zero ou mais filhos.
Exemplo:

    raiz = 7
    
    galho_esquerdo = 3
    
    galho_direito = 9
    
    galho_esquerdo_esquerdo = 2
    
    galho_esquerdo_direito = 5

# Busca sequencial:

Procura por um elemento percorrendo a lista de um por um até encontrar o que procura.
Exemplo:

    lista = [2, 6, 8, 4, 1]
    
    procurado = 8
    
    encontrado = False
    
    for item in lista:
        if item == procurado:
            encontrado = True
            break

# Busca binária:

Procura por um elemento dividindo a lista pela metade repetidamente até encontrar o que procura.
Exemplo: 

    lista_ordenada = [1, 3, 5, 7, 9]
    
    procurado = 5
    
    encontrado = False
    
    início = 0
    
    fim = 4
    
    while início <= fim:
        meio = (início + fim) // 2
        if lista_ordenada[meio] == procurado:
            encontrado = True
            break
        elif lista_ordenada[meio] < procurado:
            início = meio + 1
        else:
            fim = meio - 1
