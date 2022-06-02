def condicionales1():
    nota = float(input("Digite una nota de 0.0 a 5.0"))
    if nota > 0 and nota < 5.0:
        if nota >= 4.0:
            print(nota)
            print("Felictaciones por su buena nota")
        print(nota)
    else:
        print("Digito una nota incorrecta")

def condicionales2():
    nota = float(input("Digite una nota de 0.0 a 5.0"))
    if nota > 0 and nota < 5.0:
        if nota >= 3.0:
            print(nota)
            print("Felictaciones ha ganado el curso")
        else:
            print(nota)
            print("Ha perdido el curso")
    else:
        print("Digito una nota incorrecta")

def condicionales3():
    nombre = input("Digite su nombre: ")
    edad = int(input("Digite su edad: "))
    if edad > 18:
        print(f"{nombre} es mayor de edad")
    else:
        print(f"{nombre} es menor de edad")

def condicionales4():
    numero = int(input("Digite un numero: "))
    if numero % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")

def condicionales5():
    numero = float(input("Digite un numero: "))
    if numero > 3.5 and numero <= 7.8:
        print("El numero se encuentra dentro del intervalo (3.5, 7.8]")
    else:
        print("El nuemro no se encuentra dentro del intervalo (3.5, 7.8]")

def condicionales6():
    numero = float(input("Digite un numero: "))
    if numero > 3.5 and numero <= 7.8:
        print("El numero se encuentra dentro del intervalo (3.5, 7.8]")
    elif numero > 4.5 and numero <= 9.3:
        print("El numero se encuentra dentro del intervalo (4.5, 9.3]")
    elif numero >= 23.4 and numero <= 45.3:
        print("El numero se encuentra dentro del intervalo [23.4, 45.3]")
    else:
        print("No se encuentra en ninguno de los rangos")

def condicionales7():
    print("""
    | Carácter | Mensaje a imprimir |
    |----------|--------------------|
    |   'a'    | Android            |
    |   'i'    | IOS                |
    |   otro   | Opción inválida    |
    """)
    caracter = input("Digite un caracter: ")
    if caracter == "a" or caracter == "A":
        print("Android")
    elif caracter == "i" or caracter == "I":
        print("IOS")
    else:
        print("Opcion invalida")

def condicionales8():
    print("""
    | nota     | Mensaje a imprimir |
    |----------|--------------------|
    |  < 3.0   | Insuficiente       |
    |  <= 3.5  | Aceptable          |
    |  <= 4.0  | Sobresaliente      |
    |  <= 5.0  | Excelente          |
    """)
    nota = float(input("Digite la nota: "))
    if nota < 3.0:
        print("Insuficiente")
    elif nota > 3.0 and nota <= 3.5:
        print("Aceptable")
    elif nota > 3.5 and nota <= 4.0:
        print("Sobresaliente")
    elif nota > 4.0 and nota <= 5.0:
        print("Excelente")
    else:
        print("Digite una nota valida")

def condicionales9():
    num1 = int(input("Digite numero: "))
    num2 = int(input("Digite numero: "))
    num3 = int(input("Digite numero: "))
    num4 = int(input("Digite numero: "))
    if num1 > num2 and num1 > num2 and num1 > num4:
        print("El numero mayor es", num1)
    else:
        if num2 > num1 and num2 > num3 and num2 >num4:
            print("El numero mayor es" , num2)
        else:
            if num3 > num1 and num3 > num2 and num3 > num4:
                print("El numero mayor es", num3)
            else:
                print("El numero mayor es", num4)

def condicionales10():
    print("""
    |Estrato|Cargo Fijo|Metro3 consumido|Basuras y alcantarillado|
    |-------|-----|-----|------|
    |1      |$2500|$2200|$5500 |
    |2      |$2800|$2350|$6200 |
    |3      |$3000|$2600|$7400 |
    |4      |$3300|$3400|$8600 |
    |5      |$3700|$3900|$9700 |
    |6      |$4400|$4800|$11000|
    """)
    estrato = input("Digite el estrato: ")
    cantidad = int(input("Digite la cantidad de metros cubicos de agua consumidos: "))
    if estrato == "1":
        pagar = 2500 + 5500 + (cantidad * 2200) 
        print("Debe pagar: ", pagar)
    elif estrato == "2":
        pagar = 2800 + 6200 + (cantidad * 2350) 
        print("Debe pagar: ", pagar)
    elif estrato == "3":
        pagar = 3000 + 7400 + (cantidad * 2600) 
        print("Debe pagar: ", pagar)
    elif estrato == "4":
        pagar = 3300 + 8600 + (cantidad * 3400) 
        print("Debe pagar: ", pagar)
    elif estrato == "5":
        pagar = 3700 + 9700 + (cantidad * 3900) 
        print("Debe pagar: ", pagar)
    elif estrato == "6":
        pagar = 4400 + 11000 + (cantidad * 4800) 
        print("Debe pagar: ", pagar)
    else:
        print("Digito un valor incorrecto")

def condicionales11():
    genero = input("Digite su genero (masculino o femenino)")

    if genero == "femenino":
        estatura = float(input("Digite su estatura: "))
        edad = int(input("Digite su edad: "))
        estado = input("Digite su estado civil: ")
        if estado == "soltero":
            if edad >= 20 and edad <= 25:
                if estatura > 1.65:
                    print("Es apta para ingresar")
                else:
                    print("No es apto para ingresar")
    else:
        estatura = float(input("Digite su estatura: "))
        edad = int(input("Digite su edad: "))
        estado = input("Digite su estado civil: ")
        if estado == "soltero":
            if edad >= 18 and edad <= 24:
                if estatura > 1.65:
                    print("Es apto para ingresar")
                else:
                    print("No es apto para ingresar")
