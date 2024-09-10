def calcularPMT(p:int,r:int,n:int):
    try:
        up = (p*r)*((1+r)**n)
        down = ((1+r)**n) -1
        pmt = up/down

    except ValueError:
        raise ValueError("error en la funcion")
    else:
        pass
    finally:
        return pmt
    
def calcularMontoMaximo(salario:int,pmt:int):
    porcentajeDeuda = 0.4
    Credito = (salario*porcentajeDeuda)/(pmt)*1000000
    return salario


try:

   nombre = input("ingrese su primer nombre: \n. ")
   if nombre.isalpha():
        edad =input("ingrese cuantos años tiene: ")
        if edad.isdigit():
            edad=int(edad)
            if edad >= 18:       
                celular = input("ingrese su numero de celular(debe ser de 10 caracteres): ")
                if len(celular) == 10:
                    salarioMensual = input("ingrese su salario al mes: ")
                    if salarioMensual.isdigit:
                        salarioMensual=int(salarioMensual)
                        if salarioMensual > 0:
                            p = 1000000
                            r = 0.01
                            n = 240
                            pmt = calcularPMT(p,r,n)
                            pmt=int(pmt)
                            montoMaxDeuda = calcularMontoMaximo(salarioMensual,pmt)
                            print(montoMaxDeuda)
                        else:
                            raise ValueError("su salario no tiene un monto valido")
                    else:
                        raise TypeError("su salario no es numerico")
                else:
                    raise ValueError("su celular es erroneo")
            else:
                raise ValueError("su valor es menor a 18 años")
        else:
           raise ValueError("su valor no es numerico")   
   else:
        
    raise TypeError("su nombre tiene caracteres incorrectos")


except TypeError as te:
    print("tiene un error de tipado")
except ValueError as ve:
    print("error de valores")
except Exception as e:
    print("error inesperado")
else:
    print("su codigo anda funcionando")
finally:
    print("fin de codigo")