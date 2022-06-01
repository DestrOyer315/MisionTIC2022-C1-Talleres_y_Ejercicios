def ejercicio1():
    operacion = (6/2 *(1+2))
    print (f"El resultado correcto de la operación es: {operacion}")
    print(" En alguna calculadoras da como resultado 1 debido a que se confunden y dividien el 6 al producto 2(2+1) y esto da 1")

def ejercicio2():
    precio_pernil = 5.95 

    precio_final = precio_pernil * 10

    print(precio_final)
    print("Esta incorrecto el precio que dio el vendedor de 29,75 porque en realidad un kilo de pernil cuesta: ", precio_final)

def ejercicio3():
    peces_rojos = 284
    peces_azules = 163

    print("El total de peces dentro del acuario es de: ", (peces_rojos + peces_azules))

def ejercicio4():
    dinero_carmen = 23
    dinero_gastado = dinero_carmen - 12.75 

    print("Carmen gasto en total: ", dinero_gastado)

def ejercicio5():
    precio_ordenador = 660

    precio_final = (precio_ordenador * 10) / 100

    print("El precio que debe pagar al final con el descuento es de: ", (precio_ordenador - precio_final))

def ejercicio6():
    precio_sin_descuento = (100 * 34) / 85
    print("Lo spantalones sin el descuento costaban: ", precio_sin_descuento)

print("")
print("Escriba que ejercicio desea observar: ")
print("""
1).
2).
3).
4).
5).
6).
""")

opcion = input("-> ")

if opcion == "1":
    ejercicio1() 
elif opcion == "2":
    ejercicio2()
elif opcion == "3":
    ejercicio3()
elif opcion == "4":
    ejercicio4()
elif opcion == "5":
    ejercicio5()
elif opcion == "6":
    ejercicio6()
else:
    print("Opcion incorrecta")