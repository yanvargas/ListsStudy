#Lista encadeada: [https://www.geeksforgeeks.org/data-structures/linked-list/](https://www.geeksforgeeks.org/data-structures/linked-list/)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

# Exemplo de utilização
linked_list = LinkedList()
linked_list.head = Node(1)
linked_list.head.next = Node(2)
linked_list.head.next.next = Node(3)

#Lista circular: [Tutorials Point - Lista Circular](https://www.tutorialspoint.com/data_structures_algorithms/circular_linked_list_algorithm.htm)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

# Criação de elementos
a = Node(1)
b = Node(2)
c = Node(3)

# Criando a lista circular
a.next = b
b.next = c
c.next = a  # Último elemento aponta para o primeiro (forma um ciclo)

#Pilhas: https://www.geeksforgeeks.org/stack-data-structure/

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

# Exemplo de utilização
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()  # Retirando o elemento 3

#Filas: https://www.tutorialspoint.com/data_structures_algorithms/dsa_queue.htm

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

# Exemplo de utilização
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.dequeue()  # Retirando o elemento 1

#Árvores: https://www.geeksforgeeks.org/binary-tree-data-structure/

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Exemplo de utilização
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

#Busca sequencial: https://www.tutorialspoint.com/data_structures_algorithms/linear_search_algorithm.htm

def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
    
my_list = [3, 5, 2, 8, 9, 1]
print(sequential_search(my_list, 8))  # Retorna o índice onde está o número 8


#Busca binária: https://www.geeksforgeeks.org/binary-search/

my_list = [1, 3, 5, 7, 9, 11, 13]

target = 7
low = 0
high = len(my_list) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if my_list[mid] == target:
        found = True
        break
    elif my_list[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

