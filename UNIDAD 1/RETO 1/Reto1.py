def CDT(usuario:str, capital:int, tiempo:int):
    if tiempo > 2:
        valor_interes = (capital * 0.03 * tiempo) / 12
        valor_total = valor_interes + capital
        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}"

    else:
        valor_perder = capital * 0.02
        valor_total = capital - valor_perder
        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}"