def crear():
    if(g=='1'):
        artemis=[]
    if(g=='2'):
        sputnik=[]

def lista():
    if(g=='1.1'):
       print(artemis)
    if(g=='2.1'):
       print(sputnik)

def agregar():
    if(g=='1.2'):
        nombre=input("Agregar nombre")
        artemis.append(nombre)
        print("Usuario Artemis agregado")
    if(g=='2.2'):
        nombre=input("Agregar nombre")
        sputnik.append(nombre)
        print("Usuario Sputnik agregado")

def eliminar():
    if(g=='1.3'):
        nombre=input("Agregar nombre")
        artemis.remove(nombre)
        print("Usuario Artemis agregado")
    if(g=='2.3'):
        nombre=input("Agregar nombre")
        sputnik.remove(nombre)
        print("Usuario Sputnik agregado")

def ordenar():
    if(g=='1.4'):
        sorted(artemis.split())
        print(f"Lista ordenada Artemis {artemis}")
    if(g=='2.4'):
        sorted(sputnik.split())
        print(f"Lista ordenada Sputnik {sputnik}")

def buscar():
    nom=input("digite el nombre a buscar")
    if(g=='1.5'):
        if(nom in artemis):
            print(f"usuario encontrado {nom}")
    if(g==2.5):
        if(nom in sputnik):
            print(f"usuario encontrado {nom}")

q=1     
while(q!=0):
    g=input("----------MENU-----------\n"
    "1. Crear lista Artemis\n"
    "1.1 Listar camper Artemis\n"
    "1.2 Agregar camper Artemis\n"
    "1.3 Eliminar camper de artemis\n"
    "1.4 Ordenar lista Artemis\n"
    "1.5 Buscar camper lista Artemis\n"
    "2. Crear lista Sputnik\n"
    "2.1 Listar camper Sputnik\n"
    "2.2 Agregar camper Sputnik\n"
    "2.3 Eliminar camper de Sputnik\n"
    "2.4 Ordenar lista Sputnik\n"
    "2.5 Buscar camper lista Sputnik\n")
    if(g=='1'):
        print("A seleccionado Crear lista Artemis ")
        crear()
    if(g=='1.1'):
        print("A seleccionado Listar camper Artemis ")
        lista()
    if(g=='1.2'):
        print("A seleccionado Agregar camper Artemis ")
        agregar()
    if(g=='1.3'):
        print("A seleccionado Eliminar camper de artemis")
        eliminar()
    if(g=='1.4'):
        print("A seleccionado Ordenar lista Artemis")
        ordenar()
    if(g=='1.5'):
        print("A seleccionado Buscar camper lista Artemis")
        ordenar()

    if(g=='2'):
        print("A seleccionado Crear lista Sputnik ")
        crear()
    if(g=='2.1'):
        print("A seleccionado Listar camper Sputnik")
        lista()
    if(g=='2.2'):
        print("A seleccionado Agregar camper Sputnik ")
        agregar()
    if(g=='2.3'):
        print("A seleccionado Eliminar camper de Sputnik")
        eliminar()
    if(g=='2.4'):
        print("A seleccionado Ordenar lista Sputnik")
        ordenar()
    if(g=='2.5'):
        g=2.5
        print("A seleccionado Buscar camper lista Sputnik")
        ordenar()



