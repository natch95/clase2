#Cree un software que calcule el IVA. Que le solicite al usuario ingresar un producto 
#y su precio y automáticamente le diga cuanto es el IVA (13%) y el producto

#producto=input ("Producto? \n >")
#precio = float(input("Precio? \n >"))
#IVA=0.13
#porcIVA=(precio*IVA)
#total=porcIVA+precio
#print("El porcentaje es:",porcIVA," del producto:",producto)

#~~~~~~~~~~~~~~~~~~~~~~~~~~
#Cree un software que calcule las cargas sociales (30% patrono, 10% trabajador) y que de el total.

# salario= int(input("Ingrese su salario:\n"))
# patrono= int(float(salario)*0.30)
# trabajador= int(float(salario)*0.10)
# print("El total con cargas sociales es:",(salario+patrono+trabajador))

# while True:
#    try:
#        salario= int(input("Ingrese su salario: "))
#        patrono=salario*0.30
#        trabajador=salario*0.10
#        print("El total con cargas sociales es:",(salario+patrono+trabajador))
#        break
#    except:
#        print("Error: Debe digitar un numero!!")
#        break


#lista=[]
#lista.append("Juan")
#print(lista)

#~~~~~~~~~~~~~~~~~~~~~~~~~~
#Crear un software que le permita al profesor agregar o eliminar nombre (solo nombre) de estudiantes.

# lista=[]
# while True:
#     opcion=int(input("Desea: \n 1.Agregar nombre \n 2.Eliminar nombre\n 3.Salir \n"))
#     if opcion == 1:
#         nombre=input("Ingrese el nombre: ")
#         apellido=input("Ingrese el apellido: ")
#         lista.append(nombre)
#         lista.append(apellido)
#         print("El nombre: ",nombre,apellido," fue correctamente agregado")
#     elif opcion == 2:
#         nombre= input("Digite el nombre que desea eliminar: ")
#         lista.remove(nombre)
#         print("El nombre: ",nombre," fue correctamente eliminado")
#     elif opcion == 3:
#         break
# print(lista)


# lista=[]
# while True:
#     opcion=int(input("Desea: \n 1.Agregar nombre \n 2.Eliminar nombre\n 3. Ver lista \n 4.Salir \n"))
#     if opcion == 1:
#         nombre=input("Ingrese el nombre: ")
#         lista.append(nombre)
#     elif opcion == 2:
#         print(lista)
#         seleccion= int(input("Digite el numero de valor que desea eliminar: ")) 
#         lista.pop(seleccion)
#         #print("El nombre: ",nombre," fue correctamente eliminado")
#     elif opcion == 3:
#         print(lista)
#     elif opcion == 4:
#         break
# print(lista)

#~~~~~~~~~~~~~~~~~~~~~~~~~~
#Crear funcion

# def sumar(a,b):
#     return a+b
# print(sumar(15,40))

#~~~~~~~~~~~~~~~~~~~~~~~~~~
# Bases de Datos

import sqlite3

conn=sqlite3.connect("naty.db")
c = conn.cursor()
#c.execute("CREATE TABLE user(name text, age integer)")
c.execute("INSERT INTO user VALUES ('Naty',08)")
conn.commit()
c.execute("SELECT * FROM user")
print(c.fetchall())
conn.close()
