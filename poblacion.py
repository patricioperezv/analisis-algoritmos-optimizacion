# -*- coding: utf-8 -*-
'''
Created on 09/08/2013

@author: pperez
'''

from mochila import Mochila

class Poblacion(object):
    # Iniciamos la poblacion aleatoriamente
    def __init__(self, productos, rnd, capacidad, n = 50):
        self.container = []
        self.rand = rnd
        
        for i in range(n):
            m = Mochila(i, productos, capacidad, rnd)
            m.aleatorizar()
            self.container.append(m)
        self.container.sort(key = lambda mochila: mochila.beneficio, reverse = True)
    
    # Esto es para calculos de la ruleta
    def totalBeneficio(self):
        return sum(m.beneficio for m in self.container)
    
    # La famosa ruleta ...
    def ruleta(self):
        total = self.totalBeneficio()
        dado = self.rand.random()
        
        suma = 0
        for mochila in self.container:
            suma += mochila.beneficio / total
            if suma >= dado: # Llegamos al wilson, the chosen one
                break
        return mochila # Retornamos la mochila elegida al azar