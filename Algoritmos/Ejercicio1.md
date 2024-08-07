# Problema
saber cuántos años, meses y días tiene actualmente una persona, basándose en su fecha de nacimiento.
Definimos como variable "cantidad de días", "cantidad de años", "cantidad de meses", "Fecha de nacimiento", "dia actual", "Mes actual", "Año actual"
Definimos como constante "edad final", "Día de cumpleaños"
## Pseudocódigo
```
inicio
    Definir como constante "Día_de_cumpleaños" 
    Definir como variable "cantidad_de_dias"
    Definir como variable "cantidad_de_años"
    Definir como variable "cantidad_de_meses"
    Definir como variable "Fecha_de_nacimiento"
    definir como variable "Fecha_actual"  
    Definir como variable "edad_actual"
    Definir "Fecha_de_nacimiento" como "Día_de_cumpleaños"
    Definir n dias como 1 mes según la cantidad de días de ese mes
    Definir 12 meses como 1 año
        Insertar "Fecha_de_nacimiento"
    Leer "fecha de nacimiento"
    Contar los dias según los dias de ese mes desde 1 hasta n días del mes
    Si la fecha es ≥ a la "fecha_actual"
        entonces si es = "edad_actual" es 1 dias 0 meses 0 años
    si "fecha de nacimiento" > "fecha actual"
        entonces "edad_actual"= Error
    si "fecha de nacimiento" < "fecha actual"
        entonces contar la "cantidad_de_dias", "cantidad_de_meses" y "cantidad_de_años"
    despues de contar Imprimir resultado
    Si resultado="fecha de nacimiento"
        Entonces "felicitar por el cumpleaños"
    Si resultado es diferente de "fecha de nacimiento"
        Entonces no hacer nada
        fin si
        fin si
        fin si
        fin si 
        fin si
```

