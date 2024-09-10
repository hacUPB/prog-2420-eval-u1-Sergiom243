
horas = int(input("ingresar número de horas trabajadas"))
valor_hora = int(input("ingrese valor de las horas"))
if horas <=40:
    total = horas*valor_hora
elif horas <=45:
    total = (40*valor_hora)+((horas-40)*2*valor_hora)
elif horas <= 50:
    total = (40*valor_hora)+(5*2*valor_hora)+((hora-45)*3*valor_hora)
else:
    print("no se puede trabajar más de 50 horas")
if horas<=50:
    print("valor total a pagar es:", total)
