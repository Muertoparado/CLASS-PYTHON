
""" Construya un algoritmo en Python, que permita ingresar la
información de un empleado e imprima el nombre, los
apellidos y la antigüedad. Los datos que se deben solicitar
son los siguientes:
*Nombre * Teléfono *Año de ingreso a la empresa
*Apellidos *Edad. """

class Personas:
    def __init__(self,nombre,apellido, telefono, ingfecha,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.telefono=telefono
        self.ingfecha=ingfecha
        self.edad=edad

x=input("Desea registrar empleado \n 1. Si \n 2. No \n")
if(x=='2'):
    print("Gracias por ingresar")
else:
        while (x!=2):
            c=0
            c+=1
            nombre= Personas(input("Digite su nombre: \n"))
            apellido=input("Digite los apellidos: \n")
            telefono= input("Digite el telfono: \n")
            ingfecha=int(input("Digite la fecha de ingreso: \n"))
            edad=input("Digite la edad: \n")
            ant=2023-ingfecha
            print(f'empleados registrados # \n {Personas.nombre}\n {Personas.apellido}\n {Personas.telefono} {Personas.ingfecha}\n{Personas.edad}\n antigüedad {ant}')

            x=input("Desea registrar otro empleado \n 1. Si \n 2. No \n")

            break 
        print("Gracias por ingresar")

