""" 10. En su casa le solicitan que realice un algoritmo en Python,
que permita calcular el valor a pagar por concepto de
energía eléctrica. Los datos que se conocen son los
siguientes:
- Mes de consumo - Valor kw
-Total kw consumido en el mes - estrato """

def consumo():
    valorkw=2
    pore2=1.2
    pore3=1.4
    pore4=1.5
    pore5=1.7

    q=input("Desea calcular el total a pagar \n 1. Si\n 2.No\n")
    if (q=='2'):
        print("Gracias por ingresar")
    else:
        while(q!=1):
            print("--------Bienvenido------- \n")
            e=input("Digite el estrato:")

            if(e=='1'):
                totalConsumido=int(input("Digite el total Kw consumidos: "))
                mes=input("Mes a facturar: ")
                pagar=float(valorkw*totalConsumido)
                print(f'Mes a facturar{mes}\n Estrato{e}\nValor a pagar : {pagar}')

            elif(e=='2'):
                totalConsumido=int(input("Digite el total Kw consumidos: "))
                mes=input("Mes a facturar: ")
                pagar=float(valorkw*totalConsumido*pore2)
                print(f'Mes a facturar{mes}\n Estrato{e}\nValor a pagar : {pagar}')

            elif(e=='3'):
                totalConsumido=float(input("Digite el total Kw consumidos: "))
                mes=input("Mes a facturar: ")
                pagar=float(valorkw*totalConsumido*pore3)
                print(f'Mes a facturar{mes}\n Estrato{e}\nValor a pagar : {pagar}')

            elif(e=='4'):
                totalConsumido=int(input("Digite el total Kw consumidos: "))
                mes=input("Mes a facturar: ")
                pagar=float(valorkw*totalConsumido*pore4)
                print(f'Mes a facturar{mes}\n Estrato{e}\nValor a pagar : {pagar}')

            elif(e=='5'):
                totalConsumido=int(input("Digite el total Kw consumidos: "))
                mes=input("Mes a facturar: ")
                pagar=float(valorkw*totalConsumido*pore5)
                print(f'Mes a facturar{mes}\n Estrato{e}\nValor a pagar : {pagar}')

            q=input("\n Desea realizar otro calculo \n 1. Si\n 2.No\n")

consumo()