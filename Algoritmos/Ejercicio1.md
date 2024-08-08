# Problema
saber cuántos años, meses y días tiene actualmente una persona, basándose en su fecha de nacimiento.
Definimos como variable "cantidad de días", "cantidad de años", "cantidad de meses", "Fecha de nacimiento", "dia actual", "Mes actual", "Año actual"
Definimos como constante "edad final", "Día de cumpleaños"
## Pseudocódigo
```
inicio
    Definir "Fecha_de_nacimiento" como "Día_de_cumpleaños"
    Definir n dias como 1 mes según la cantidad de días de ese mes
    Definir 12 meses como 1 año
        Insertar "Fecha_de_nacimiento"
    Leer "fecha de nacimiento"
    Contar los dias según los dias de ese mes desde "fecha_de_nacimiento" hasta n días del mes
    Si la fecha es ≥ a la "fecha_actual"
        entonces si es = "edad_actual" es 1 dias 0 meses 0 años
    si "fecha de nacimiento" > "fecha actual"
        entonces "edad_actual"= Error
    si "fecha de nacimiento" < "fecha actual"
        entonces contar la "cantidad_de_dias", "cantidad_de_meses" y "cantidad_de_años"
    despues de contar Imprimir resultado
    Si resultado="fecha de nacimiento"
        Entonces "felicitar por el cumpleaños"
    Si no resultado es diferente de "fecha de nacimiento"
        Entonces no hacer nada
        fin si
        fin si
        fin si
        fin si 
        fin si
    fin
```
```
inicio
    leer CH
        
        Si CH <=2 el p=5
            entonces si es CH=2 el P=10
        si no 
            entonces p=5
        fin si
        Si
            CH >2<=5 el p=4
                entonces el si CH=3 el p=10+4
        si no
            CH=5 
                entonces el p=22
        fin si
        Si 
            CH >5<=10 el p=3
                entonces si CH=6 el p=22+3
        fin si
        Si
            CH>10 entonces el ct=0 y el p=2 por cada hora
                entonces si CH=12 el p=24
        fin si
    fin
```

        
        
