"""
Index()(Sencible a mayusculas) Se puede utilizar para dos cosas:
 1) Para saber en que posicion esta un determinado caracter, devuelve la posicion en el que se encuentra el caracter buscado 

 2) Y se utiliza tambien a la inversa, para saber que caracter hay en una posicion determinada

 rindex() = Se le indica a la maquina que busque de izquierda a derecha

"""
"""
texto001 = "Aqui encuentro que letra o que hay en la posicion indicada"
resultado001 = texto001[3]
print(f"en la posicion 4 se encuentra: {resultado001}")

texto002 = "Este es un ejemplo de como se pueden utilizar los numeros negativos"
resultado002 = texto002[-1]
print(f"en la posicion -1 se encuentra: {resultado002}")

texto003 = "Aqui se busca en que posicion hay un caracter en especifico"
# Cuando se busca un caracter que no existe en mi cadena de caracteres, devuelve un error
resultado003 = texto003.index("e")
print(f"Se busca en que posicion esta el caracter e: {resultado003}")

texto004 = "Aqui se ve que sucede cuando se busca una cadena de caracteres"
resultado004 = texto004.index("ve")
print(f"en la posicion 4 se encuentra: {resultado004}")

texto005 = "Aqui se busca en un rango especifico de caracteres"
resultado005 = texto005.index("ca",4,15)
print(f"en la posicion 4 se encuentra: {resultado005}")

texto006 = "Aqui se ve como se puede utilizar para buscar de derecha a izquierda"
resultado006 = texto006.rindex("ve")
print(f"el caracter ve se encuentra en la posicion: {resultado006}")

"""

"""
El sacar una cadena de caracteres de una cadena de caracteres mas grande se llama slicing

texto = "Esta es una cadena de caracteres muy grande"
#No inckuye el caracter en donde termina
extracto = texto[0:4]
print(extracto)

# Tambien se le puede indicar cada cuantos caracteres guardar
texto1 = "Esta es una cadena de caracteres muy grande"
#El tercer valor indica cada cuanto dar un salto
extracto1 = texto1[0:10:2]

Algunos trucos que se pueden hacer son:
texto1[3:], Cuando se deja el segundo valor en blanco la maquina supone que se desea extraer desde 
en este ejemplo el 3 hasta donde termine la cadena
texto1[:3],  Aqui se le indica que extraiga desde el inicio hasta en 3 pero no incluyendolo

texto[::2], dejando el valor de inicio y el valor de final en blanco se le indica a la maquina que busque 
de principio a fin y que extraiga cada 1 caracter

texto[::-1], Si se utiliza un valor negativo extrae los caracteres de atras para adelante,
de derecha a izquierda

print(extracto1)

"""

"""
Acontinuacion voy a escribir algunos metodos de la funcion String:
1) upper() pasa a mayusculas 
2) lower() pasa a minusculas 
3) split() se separa el string en partes y las guarda en una lista
4) join() unir items que fuerons separados por el separadorrr
5) find() encontrar un sub string
6) replace() remplazar un sub-string



# Aqui estoy pasando todos los caracteres a mayuscula
oracion = "Esta es mi oracion putos!!!"
resultado = oracion[-8:-1].upper()
print(resultado)

# Aqui estoy pasando todos los caracteres a minuscula
oracion_dos = "ESTA ES MI SEGUNDA ORACION PUTO!!!"
resultado_dos = oracion_dos.lower()
print(resultado_dos)

# Aqui estoy separando todas las cadenas de caracteres y metiendolos en una lista
oracion_tres = "Esta es mi tercera oracion puto, dejame en paz!!!"
resultado_tres = oracion_tres.split()
print(resultado_tres)

# Tambien se le puede indidar el criterio de separacion
oracion_cuarta = "Esta es mi cuarta oracion puto, dejame en paz!!!"
resultado_cuarta = oracion_cuarta.split("p")
print(resultado_cuarta)

# Aqui uno muchos strings en un string
a = "Dejate"
b = "de"
c = "monerias"
d = "...Puto!!"
e = "++QUINTO++"
listaLetras = [a,b,c,d,e]
# Al inicio le indico con que caracter quiero que separe mi lista de strings
resultado_quinta = " ".join(listaLetras)
print(resultado_quinta)

# Aqui busco un substring en un string
oracion_sexta = " *-*-* S E X T A *-*-* oracion"
# Tambien se puede buscar lineas seguidas de caracteres
resultado_sexta = oracion_sexta.find("X")
print(resultado_sexta) 

# Aqui voy a remplazar una linea de caracteres por otra
oracion_septima = "Esta es la 7 oracion putitos B)"
resultado_septima = oracion_septima.replace("putitos B)","Puton jajaja BP")
print(resultado_septima)


Acontinuacion voy a escribir las propiedades de los strings:
    1) Son inmutables, significa que una vez creados su orden interior no puede ser cambiado ni alterar su contenido
    2) Es multiplicable
    3) Pueden tener mas de una linea
    4) Se pueden buscar substring dentro de los strings
    5) Se puede contar su longitud
Acontinuacion un ejemplo de su multiplicasidad y de que pueden tener mas de una linea
"""

n1 = """Si quiero juegar
con fuego"""

#print(n1 * 10)
# Aqui busco saber si un determinado sub string existe en un string
print("fuego" in n1)
# Aqui busco saber si un substring no existe en un string
print("agua" not in n1)
# Aqui me devuelve el largo de un string
print(len(n1))






