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
    cant_productos = 40
    capacidad = 8400
    generaciones = 500    
    rnd = random.Random(100)
    
    
    productos = tuple(Producto(i, rnd) for i in range(cant_productos)) # Lista de productos generados aleatoriamente
#     for producto in productos: print producto
    
    pob = Poblacion(productos, rnd, capacidad)
    print "Mejor mochila poblacion inicial:"
    print pob.mejorWilson()
    
    for _ in range(generaciones):
        pob.newGeneration()
    
    print "Mejor mochila despues de {0} años".format(generaciones)
    print pob.mejorWilson()
    
#     # Fuerza bruta!
    mejol = Mochila(0, productos, capacidad, rnd) # Mochila vacia :(
     
    for idx, info in enumerate(itertools.product([True,False], repeat = cant_productos)):
        m = Mochila(idx, productos, capacidad, rnd)
        m.info = info
        if m.beneficio > mejol.beneficio and m.peso <= capacidad: # Solucion mejor
            mejol = m
    print mejol