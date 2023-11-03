
#Aqui tengo una lista de strings 
mi_lista = ["a","b","c","d"]
print(type(mi_lista))

# Lista con diferente tipo de datos 
seg_lista = [1,"perro",3.5,]

# Se imprime la candidad de objetos dentro de la lista 
print(len(seg_lista))

# Se imprime la informacion de una posicion de la lista
print(seg_lista[1])

# Se pueden utilizar varias funciones de los strings
# Devuelve un lo que hay en un rango determinado
print(seg_lista[1:2])

# Concatenando
print(mi_lista+seg_lista)

ter_lista = mi_lista + seg_lista
print(ter_lista)
ter_lista[0] = 3.15
print(ter_lista)

# Las listas tienen muchos metodos disponibles para facilitar su uso
ter_lista.append("Aguacate") # Con append se le agrega un nuevo item a nuestra lista
print(ter_lista)

# Con pop se remueve un elemento de la lista, si se deja vacio pop() el sistema elimina el ultimo elemento de la lista por default
ter_lista.pop(2) 
print(ter_lista)

# Tambien puedo guardar el elemento eliminado en otra variable

ele_eliminado = ter_lista.pop()
print(ele_eliminado)

# Aqui se ve el funcionamiento del metodo sort para ordenar los elementos dentro de la lista
lista_desor = ["c", "d", "a", "b"]
print(lista_desor)
print(lista_desor.sort)

# Tambien hay un metodo para ordenar los elementos de la lista de en un order inverso
lista_desor2 = ["c", "d", "a", "b"]
print(lista_desor2)
print(lista_desor2.reverse)
