#!/usr/bin/env pypy
# -*- coding: utf-8 -*-

'''
Created on 09/08/2013

@author: pperez
'''

import random
from producto import Producto
from mochila import Mochila

if __name__ == '__main__':
    cant_productos = 10
    disponibilidad_mochila = 2100
    
    rnd = random.Random(100)
    
    productos = tuple(Producto(i, rnd) for i in range(cant_productos)) # Lista de productos generados aleatoriamente
    for producto in productos: print producto
    for _ in range(10):
        m = Mochila(0, productos, disponibilidad_mochila, rnd)
        m.aleatorizar()
        print m
    