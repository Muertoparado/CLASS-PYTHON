""" 8. Escriba un bloque cualquiera de código en Python en donde
utilice 2 condicionales (if) anidados. """

print("-------BIENVENIDO--------\n")
c=input("desea ingresar a la tienda  [s/n]")

if (c=='n'):
        print("----pronto regreso----")
else:
       
        print("productos \n")
        print("1.camisas \n")
        print("2.zapatos \n")
        print("3.carteras \n")
        p=input("digite el numero de la lista del producto a seleccionar ")
        
        if(p=='1'):
            print("a seleccionado camisas")
            x=input("cuantas camisas desea comprar")
            print("----Gracias por la compra------\n ha seleccioado ",x, "camisas")
        elif(p=='2'):
            print("a seleccionado zapatos")
            x=input("cuantos pares zapatos desea comprar")
            print("----Gracias por la compra------\n ha seleccioado ",x, "pares de zapatos")
        elif(p=='3'):
            print("a seleccionado cartera")
            x=input("cuantas carteras desea comprar")
            print("----Gracias por la compra------\n ha seleccioado ",x, "carteras")
