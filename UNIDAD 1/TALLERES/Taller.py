def ejercicio1():
    print("")
    print("LAS OPERACIONES PARA LOGRAR LOS OBJETIVOS SON:  ")
    print("")
    print("0 = ", (2 - 2) * 2 * 2 * 2)
    print("1 = ", (2 * (2 - 2) + 2 / 2))
    print("2 = ", (2 * 2 - 2) / 2 * 2)
    print("3 = ", (2 / 2) + (2 -2) + 2)  
    print("4 = ", (2 * (2 - 2) + 2 + 2))
    print("5 = ", (2 * 2 * 2 + 2) / 2)
    print("6 = ", (2 * 2 + 2) + (2 - 2))
    print("7 = ", 2 * 2 * 2 - (2 / 2))
    print("8 = ", (2 * 2 * 2 + 2) - 2)
    print("9 = ", (2 / 2) + (2 * 2 * 2))
    print("10 = ", 2 + 2 + 2 + 2 + 2)

def ejercicio2():
    precio_celular = 420

    precio_iva = (420 / 100) * 20

    precio_iva = precio_celular + precio_iva

    print("El telefono movil al siguinete dia tendra un costo de: ", precio_iva)

def ejercicio3():
    minutos = 640/60

    vueltas = 147 * minutos

    print("EL SPINNER DA LA CANTIDAD DE:", vueltas, "EN", minutos, "MINUTOS")

def ejercicio4():
    total_refresco = 24 * 9

    personas = 56

    cantidad_por_persona = 3 * personas

    latas_sobrantes = total_refresco - cantidad_por_persona

    print("LA CANTIDAD DE LATAS DE REFRESCO QUE SOBRARON ES DE: ", latas_sobrantes)

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
else:
    print("Opcion incorrecta")