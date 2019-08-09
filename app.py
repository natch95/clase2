import suma
import resta
import multiplicar

# suma.sumar(5,1)
# resta.restar(6,3)
# multiplicar.multi(10,20)


lista=[]

while True:
    opcion=int(input("Desea: \n 1.Agregar nombre \n 2.Eliminar nombre\n 3.Salir \n"))
    if opcion == 1:
        nombre=input("Ingrese el nombre: ")
        suma.agregar(nombre)
    elif opcion == 2:
        valor= input("Digite el numero de valor que desea eliminar: ")
        resta.eliminar(valor)
    elif opcion == 3:
        multiplicar.salir()
print(lista)