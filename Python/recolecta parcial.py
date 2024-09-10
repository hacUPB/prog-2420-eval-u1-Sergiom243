objetivo = int(input("ingresar el valor objetivo"))
acum = 0
while acum < objetivo:
    aporte = int(input("ingrese aporte"))
    acum = acum + aporte
    porcent = acum * 100/objetivo
    print(f'el porcentaje acumulado es {porcent}')
    falta = objetivo - acum
    print (f'Faltan ${falta} para llegar al objetivo')
    if porcent >= 100:
        print("se ha alcanzado el 100% del objetivo")
    elif porcent >= 90:
        print("se ha alcanzado el 90% del objetivo")
    elif porcent >=50:
        print("se ha alcanzado el 50% del objetivo")
