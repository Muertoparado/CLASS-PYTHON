""" En pocos días comienza la vuelta a España y la federación
colombiana de ciclismo, como incentivo ha determinado pagar
un valor adicional. El programa pedirá por teclado el sueldo
básico por kilometro recorrido, el número de kilómetros
recorridos durante toda la vuelta, numero de kilómetros
recorridos con la camiseta de líder.
Calcular el valor a pagar total, si se sabe que si recorre en la
bici más de 1800 kilómetros con la camiseta de líder, esos
kilómetros se consideran especiales y tendrán un recargo de
25%.
El total de kilómetros por recorrer durante toda la vuelta serán
3.277 kilómetros,el ganador de la vuelta a España recibirá 700
millones de pesos. """

class Federacion:
    def __init__(self,sueldo,numkm1,numkmlider):
        self.sueldo=sueldo
        self.numkm1=numkm1
        self.numkmlider=numkmlider

c=0
esp=1800
tope=3277
pagoganador=700
pagoesp=0
pago=0
while(c!=1):
        sueldo=float(input("Digite su sueldo básico por kilometro recorrido: "))
        numkm1=float(input("\nDigite número de kilómetros recorridos durante toda la vuelta: "))
        numkmlider=float(input("\nDigite el numero de kilómetros recorridos con la camiseta de líder: "))

        asignacion= Federacion (sueldo,numkm1,numkmlider)
        if(numkmlider>esp):
            pagoesp=(numkmlider-esp)*1,25

        if(numkm1>tope):
            pago=pagoganador
            print("A ganado la vuelta espana")
        
        print(f"----pago total-----\n"
        f"pago kilometros especiales {pagoesp}\n"
        f"pago kilometros normales{sueldo*numkm1}\n"
        f"pago ganador {pago}\n"
        f"------Total :{pagoesp+(sueldo*numkm1)+pago}" )
           
        c=int(input("1.salir\n 2. continuar\n"))
