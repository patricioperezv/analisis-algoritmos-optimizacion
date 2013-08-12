# -*- coding: utf-8 -*-
'''
Created on 09/08/2013

@author: pperez
'''
import mochila
Mochila = mochila.Mochila

class Poblacion(object):
    # Iniciamos la poblacion aleatoriamente
    def __init__(self, productos, rnd, capacidad, n = 50, Pc = 0.9, Pm = 0.2):
        # productos: tupla de productos
        # rnd: generador de pseudo-azar
        # capacidad: capacidad de la mochila
        # Pc: probabilidad de cruza
        # Pm: probabilidad de mutacion
        # n: tamaño de la poblacion
        
        self.container = []
        self.rand = rnd
        self.Pc = Pc
        self.Pm = Pm
        self.n = n
        
        self.mutaciones = 0
        self.cruzas = 0
        self.generaciones = 0
        
        for i in range(n):
            m = Mochila(i, productos, capacidad, rnd)
            m.aleatorizar()
            self.container.append(m)
        self.container.sort(key = lambda mochila: mochila.beneficio, reverse = True) # Asi deberian salir mas rapidito las mejores soluciones
        # Tambien sirve para irme piteando las peores soluciones
    
    # Esto es para calculos de la ruleta
    def totalBeneficio(self):
        return sum(m.beneficio for m in self.container)
    
    # La famosa ruleta ...
    def ruleta(self):
        total = float(self.totalBeneficio())
        dado = self.rand.random()
        
        suma = 0
        for m in self.container:
            suma += m.beneficio / total
            if suma >= dado: # Llegamos al wilson, the chosen one
                break
        return m # Retornamos la mochila elegida al azar
    
    # Avanza una etapa de evolucion
    def newGeneration(self):
        self.generaciones += 1
        coqueta1 = self.ruleta()
        coqueta2 = self.ruleta()
        
        nos_cruzamos = self.rand.random()
        if nos_cruzamos <= self.Pc: # Se cruzan 1313
            self.cruzas += 1
            h1, h2 = mochila.cruza(coqueta1, coqueta2)
            del self.container[-2:] # Nos piteamos a los dos wilsons mas wilsons de la poblacion
            muta = self.rand.random()
            if muta <= self.Pm: # Mutamos a la hija1
                self.mutaciones += 1
                mochila.mutar(h1)
            muta = self.rand.random()
            if muta <= self.Pm: # Mutamos a la hija2
                self.mutaciones += 1
                mochila.mutar(h2)
            self.container.extend([h1, h2]) # Y agregamos a los hijos recien creados
            self.container.sort(key = lambda mochila: mochila.beneficio, reverse = True) # De nuevo, sorting ...
    
    # Retornamos al mejor wilson de la poblacion
    def mejorWilson(self):
        return self.container[0]
    
    def __repr__(self):
        return 'Poblacion(mochilas: {0}; generaciones: {1}; mutaciones: {2}; cruzas: {3}\nMejor wilson: {4}'.format(self.n, self.generaciones, self.mutaciones, self.cruzas, self.mejorWilson())
    
    def __str__(self):
        return self.__repr__()
