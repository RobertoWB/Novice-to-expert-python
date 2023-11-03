# Para sacar las comillas simples utilizar el siguiente comando: alt + 39
# Para sacar los parentesis cuadrados utilizar el siguiente comando: alt + 91 apertura - alt + 93 cierre  
# Acontinuacion voy a codear unos cuantos ejemplos del uso que se le puede dar a un diccionario

# Importante: La informacion de los diccionarios se encierra en las comillas asi: {} y las listas entre comillas cuadradas []

#Primer ejemplo 
diccionario = {'c1':'Puto', 'c2':'Puta'}
print(diccionario['c1'])

puta = diccionario['c2']
print(puta)

#Segundo ejemplo
persona = {'nombre':'Pedro', 'apellido':'Asenjo','edad':39,'estatura':1.82}
print(persona)

edad = persona['edad']
print(edad)

#Tercer ejemplo
dic_lista = {'c1':{'v1':10,'v2':20,'v3':30},'c2':[1.60,1.70,1.80,1.90]}
print(dic_lista['c2'][2])
# No imprime el 0 de una decimal que termine con 0, pero si imprime 1.0
print(dic_lista['c1']['v2'])

# Reto Numero 1: Imprimir la letra e en mayuscula
dic_reto = {'c1':['a','b','c'],'c2':['d','e','f']}
print(dic_reto['c2'][1].upper())

#Cuarto ejemplo
dic_cua = {1:'a',2:'b'}
print(dic_cua)
dic_cua[3] = 'c'
print(dic_cua)
#Tambien se puede sobrescribir un valor 
dic_cua[1] = 'A'
print(dic_cua)

#Los diccionarios tienen muchos metodos que uno puede utilizar, por ejemplo el siguiente 
#IMPORTANTE: No olvidar que cuando se quiere utilizar un metodo siempre su nombre tiene un parentesis () al final
print(dic_cua.keys())
print(dic_cua.values())
print(dic_cua.items())
