#!/usr/bin/env pypy
# -*- coding: utf-8 -*-

'''
Created on 09/08/2013

@author: pperez
'''

import random
import itertools
from producto import Producto
from poblacion import Poblacion
from mochila import Mochila

if __name__ == '__main__':
    cant_productos = 20
    capacidad = 4200
    generaciones = 100
    
    # Para este caso la mejor mochila es: Mochila(adn = (True, True, False, False, True, True, False, True, True, True), peso = 1744, beneficio = 1921)
    # Obtenido por fuerza bruta
    
    rnd = random.Random(100)
    
    print "Productos:"
    print "-" * 50
    print
    productos = tuple(Producto(i, rnd) for i in range(cant_productos)) # Lista de productos generados aleatoriamente
#     for producto in productos: print producto
    
    pob = Poblacion(productos, rnd, capacidad)
    print pob.mejorWilson()
    
    for _ in range(generaciones):
        pob.newGeneration()
#         print pob.mejorWilson()
    print pob.mejorWilson()
    
#     # Fuerza bruta!
    mejol = Mochila(0, productos, capacidad, rnd) # Mochila vacia :(
     
    for idx, info in enumerate(itertools.product([True,False], repeat = cant_productos)):
        m = Mochila(idx, productos, capacidad, rnd)
        m.info = info
        if m.beneficio > mejol.beneficio and m.peso <= capacidad: # Solucion mejor
            mejol = m
    print mejol