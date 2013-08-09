#!/usr/bin/env pypy
# -*- coding: utf-8 -*-

'''
Created on 09/08/2013

@author: pperez
'''

from producto import Producto
from solucion import Solucion
import random

if __name__ == '__main__':
    cant_productos = 10
    disponibilidad_mochila = 2100
    
    rnd = random.Random(10)
    
    productos = [Producto(i, rnd) for i in range(cant_productos)] # Lista de productos generados aleatoriamente
    
    sol = Solucion(productos, rnd, disponibilidad_mochila)
    sol.genAleatoria()