
def ejercicio_1(nombre):
    return f"¡Hola {nombre}!"

print("")

from math import factorial, pi
def ejercicio_2(numero):
    return f"El factorial de {numero} es {(factorial(numero))}"

print("")

def ejercicio_3(cantidad, iva):
    if iva == 0:
        iva = 19
    total = (cantidad / 100) * iva
    total = total + cantidad
    return f"El total a pagar es de: {total}"
    
print("")

def ejercicio_4_circulo(radio):
    area = pi * (radio**2)
    return f"El area del circulo es de: {area}"

print("")

def ejercicio_4_cilindro(altura, area):
    volumen = area * altura
    return f"El volumen del cilinro es de: {volumen}"

print("")

def ejercicio_5(numero):
    sumatoria = (numero(numero+1)) / 2
    return f"La sumatoria es de: {sumatoria}"

print("")

def ejercicio_6(peso, estatura):
    imc = peso / (estatura ** 2)
    return f"Tu índice de masa corporal es {round(imc,2)}"

print("")

def ejercicio_7(payasos, muñecas):
    payasos = payasos * 112
    muñecas = muñecas * 75
    total = payasos + muñecas
    return f"El peso total del paquete es de: {total}"

print("")

def ejercicio_8(barras):
    preciohabitual = barras * 3.49
    descuento = (preciohabitual / 100) * 60
    costefinal = preciohabitual - descuento
    return f"""El precio habitual es de: {preciohabitual}
    El descuento es de: {descuento}
    El coste final es de: {costefinal}"""

print("")

def ejercicio_9(cantidad):
    primeraño = (cantidad/100) * 4
    cantidad1 = cantidad + primeraño

    segundoaño = (cantidad1/100) * 4
    cantidad2 = cantidad1 + primeraño

    terceraño = (cantidad2/100) * 4
    cantidad3 = cantidad2 + primeraño
    return f"""Primer año: {round(cantidad1,2)}
    Segundo año: {round(cantidad2,2)}
    Tercer año: {round(cantidad3,2)}"""

print("")

def ejercicio_10(segundos):
    horas=int(segundos/3600)
    segundos-=horas*3600
    minutos=int(segundos/60)
    segundos-=minutos*60
    return f"Horas: {horas} minutos: {minutos} segundos: {segundos}"