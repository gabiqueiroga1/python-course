# Collection Data-Types (List, Tuples, Set, Dictionary)

# List  |         | Mutável  | Ordenado      | Coleção
# Tuple |         | Imutável | Ordenado      | Coleção
# Set   | Unica   | Mutável  | Não Ordenado  | Coleção
# Dict  | Mapeada | Mutável  | Ordenaro      | Coleção


# Syntax

empty_list = [] # or list()
# my_list = ['Wall', 'Floor', 'Roof', 'Ceiling']

# Get Single List Item
# print(my_list[2])       # Terceiro item (contando do 0)
# print(my_list[-1])      # Ultimo Item
# print(my_list[-2])      # Segundo ultimo item

# Get Multiple Items (Slice)
my_list = ['Wall', 'Floor', 'Roof', 'Ceiling','Wall', 'Floor', 'Roof', 'Ceiling']
# print(my_list[:2])      # Pegar até o segundo item (excluindo o segundo)
# print(my_list[2:])      # Pegar a partir do segundo item (incluindo)
# print(my_list[1:3])     # Pegar a partir do primeiro(incluindo) até o terceiro (excluindo)
# print(my_list[::2])       # Pegar cada segundo item
# print(my_list[1:6:2])     # Pegar cada segundo item a partir do segundo(incluindo) até o sexto (excluindo)
# print(my_list[::-1])      # Inverte a Lista

# Slicing Use-Case Exemple

# another_list = ['Categorias', 'Maça', 'Banana', 'Uva', 'Melão']

# cabecalho = another_list[0]
# dados = another_list[1:] 
# print(cabecalho)
# print(dados)

# Operadores de associação

# another_list = ['Categorias', 'Maça', 'Banana', 'Uva', 'Melão']

# print('Maça' in another_list)            # True
# print('Bicicleta' in another_list)       # False
# print('Bicicleta' not in another_list)   # True

# Popular Functions with Lists

# another_list = ['Categorias', 'Maça', 'Banana', 'Uva', 'Melão']
# numbers = [21, 20, 50, 40, 30]

# print(len(another_list))        # Retorna numero total de itens dentro da lista
# print(sorted(another_list))     # Retorna a lista ordenada (nesse caso em ordem alfabética)
# print(sorted(numbers)) 
# print(sum(numbers))             # Retorna a soma dos numeros    
# print(min(numbers))             # Retorna o menor numero
# print(max(numbers))             # Retorna o maior nunmero

# List Methods (Built-In Functionality)

another_list = ['Categorias', 'Maça', 'Banana', 'Uva', 'Melão']
list_2 = ['Melancia', 'Pitaya']

# another_list.append('Melancia')             # Adiciona um único item na lista
# another_list += list_2                      # Junta duas listas
# another_list.extend(list_2)                 # Outra forma de juntar duas listas
# another_list.sort()                         # Ordena 
# another_list.remove('Uva')                  # Remove da lista 

print(another_list.count('Maça'))          # Retorna quantos itens 'Maça' tem na lista
print(another_list.index('Banana'))
print(another_list.insert(2, 'Mexerica'))
print(another_list)