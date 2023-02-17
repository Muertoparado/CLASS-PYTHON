""" N atletas han pasado a finales en salto triple en los juegos
olímpicos de 2022.

Diseñe un programa que pida por teclado los nombres de cada
atleta finalista y a su vez, sus marcas del salto en metros.

Informar el nombre de la atleta campeona que se quede
con la medalla de oro y si rompió récord, reportar el pago que
será de 500 millones. El récord esta en 15,50 metros. """

n=int(input("Digite el numero de finalistas "))
record=15.55
dist=0
nomcamp=""
for i in range (n):
    nombre=input("Digite el nombre del competidor: ")
    m=float(input("Digite el numero de metros: "))

    if(m>dist):
        nomcamp=nombre
        dist=m


        if(m>record):
            print(f"{nombre} ha roto el record pago extra 500 millones")
        else:
            print(f"Ganador sin romper record {nombre}")