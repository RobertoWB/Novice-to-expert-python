"""
string(str)
integer(int)
floating(float)
listas(lst) = tienen orden y es cambiable
diccionarios(dic) = la informacion se guarda de una manera desordenada 
sets(set) = solo guardan elementos unicos y innerepetibles 
booleanos(bool) true,false

++Para sacar el cocientede una division, la manera de  
hacerlo es por ejemplo 7//2 que da como resultado 3 en vez de 3.0

++Para sacar el modulo(El modulo de una division es lo que sobre de ella) de una division
se hace por ejemplo asi: 7%2 que da como resultado 1 

++Para elevar un numero se hace de la siguiente manera: x**y donde "x" es el numero a elevar y la "y" el cuanto lo quiero elevar

++round() se utiliza para redondear numeros, round(#,#) donde el segundo numero es la cantidad de decimales que quiero que muestre

"""

nombre = input("Escriba su nombre: ")
valor = float(input("Digite el valor de la venta: "))
comision = round(valor*0.13,4)
if(comision < 1000):
    print(f"Oraleeee!! {nombre} mi chavo, tu comision es de: {comision} puto")
elif (comision > 1000 and comision < 2000):
    print(f"Hola {nombre}, tu comision es de: {comision} ")
elif (comision > 2000):
    print(f"Hola {nombre}, FELICITACIONES!!! su comision es de : {comision} !!!!")
