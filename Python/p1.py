#funciones de entrada y salida.
#IMC = peso/estatura^2

print('+'*40)
print('Bienvenido a la calculadora de IMC')
print('+'*40)
#int y float int para volverlo entero y float para decimal.
peso = int(input('Por favor ingrese su peso en kg:'))
Estatura = float(input('Por favor ingrese si Estatura en m:'))


IMC= peso/(Estatura*Estatura)

print ('su IMC =',IMC)
