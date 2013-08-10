# -*- coding: utf-8 -*-

'''
Created on 09/08/2013

@author: pperez
'''

class Mochila(object):
    def __init__(self, id_, productos, capacidad, rnd):
        # id_: Identificador de la mochila (int)
        # productos: Tupla de productos posibles (tupla)
        # capacidad: Capacidad de la mochila
        # rnd: Generador aleatorio de numeros (ex: random.random(100))
        
        self.id = id_
        self.__productos = productos
        self.capacidad = capacidad
        self.__rand = rnd
        self.__info = [False] * len(self.__productos) # Por defecto no llevamos ningun producto en la mochila!
    
    def __repr__(self):
        return 'Mochila(id = {0}, adn = {1}, peso = {2}, beneficio = {3})'.format(self.id, self.info, self.peso, self.beneficio)
    
    def __str__(self):
        return self.__repr__()
    
    # Setter para info
    def __setInfo(self, info):
        self.__info = info
    
    # Getter para info
    def __getInfo(self):
        return self.__info
    
    # Getter para peso
    def __getPeso(self):
        return sum((producto.peso for producto in self.__productos if self.__info[producto.id])) # Sumamos si efectivamente esta en la mochila
    
    # Getter para beneficio
    def __getBeneficio(self):
        return sum((producto.beneficio for producto in self.__productos if self.__info[producto.id])) # Sumamos si efectivamente esta en la mochila
    
    # Propertys
    info = property(fset = __setInfo, fget = __getInfo)
    peso = property(fget = __getPeso)
    beneficio = property(fget = __getBeneficio)
    
    # Genera solucion aleatoria
    def aleatorizar(self):
        productos = list(self.__productos) # Copio la lista de productos, es desordenable por random.shuffle :)
        self.__rand.shuffle(productos)
        
        while productos:
            prod = productos.pop() # Quito el ultimo item, tecnicamente estoy quitando itemes al azar
            
            if prod.peso <= (self.capacidad - self.peso):
                # Cabe, lo agrego a la mochila
                self.__info[prod.id] = True
    
    # Repara la solucion si es invalida
    def reparar(self):
        while self.peso > self.capacidad: # Si nos pasamos de peso ...
            idx = self.__rand.randrange(0, len(self.__productos))
            self.__info[idx] = False