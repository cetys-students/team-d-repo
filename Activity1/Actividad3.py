#!/usr/#Importamos math
from math import *
 
#Definimos la funcion
#@ n: numero de x
#@ a y b los intervalos de la integral
#@ f: La funcion a integrar
def definite_integral(sampling_period, lower_limit, upper_limit, samples):
    #calculamos h
    h = (upper_limit -  lower_limit) / sampling_period
    #Inicializamos nuestra varible donde se almacenara las sumas
    suma = 0.0
    #hacemos un ciclo para ir sumando las areas
    for i in range(1, sampling_period):
        #calculamos la x
        #x = a - h + (2 * h * i)
        x =  lower_limit + i * h
        # si es par se multiplica por 4
        if(i % 2 == 0):
            suma = suma + 2 * fx(x, samples)
        #en caso contrario se multiplica por 2
        else:
            suma = suma + 4 * fx(x, samples)
    #sumamos los el primer elemento y el ultimo
    suma = suma + fx( lower_limit, samples) + fx(upper_limit, samples)
    #Multiplicamos por h/3
    rest = suma * (h / 3)
    #Retornamos el resultado
    return (rest)
 
#Funcion que nos ayuda a evaluar las funciones
def fx(x, samples):
    return eval(samples)
 
#valores de ejemplo para la funcion sin(x) con intervalos de
sampling_period = 100
lower_limit = 0.0
upper_limit = 1.0
samples= 'sin(x)'

print(definite_integral(sampling_period, lower_limit, upper_limit, samples))
