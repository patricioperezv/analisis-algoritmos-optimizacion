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
        self.productos = productos
        self.capacidad = capacidad
        self.rand = rnd
        self.info = [False] * len(self.productos) # Por defecto no llevamos ningun producto en la mochila!
    
    def __repr__(self):
        return 'Mochila(adn = {1}, peso = {2}, beneficio = {3})'.format(self.id, self.info, self.peso, self.beneficio)
    
    def __str__(self):
        return self.__repr__()
    # Getter para peso
    def __getPeso(self):
        return sum((producto.peso for producto in self.productos if self.info[producto.id])) # Sumamos si efectivamente esta en la mochila
    
    # Getter para beneficio
    def __getBeneficio(self):
        return sum((producto.beneficio for producto in self.productos if self.info[producto.id])) # Sumamos si efectivamente esta en la mochila
    
    # Genera solucion aleatoria
    def aleatorizar(self):
        productos = list(self.productos) # Copio la lista de productos, es desordenable por random.shuffle :)
        self.rand.shuffle(productos)
        
        while productos:
            prod = productos.pop() # Quito el ultimo item, tecnicamente estoy quitando itemes al azar
            
            if prod.peso <= (self.capacidad - self.peso):
                # Cabe, lo agrego a la mochila
                self.info[prod.id] = True
    
    # Repara la solucion si es invalida
    def reparar(self):
        while self.peso > self.capacidad: # Si nos pasamos de peso ...
            idx = self.rand.randrange(0, len(self.productos))
            self.info[idx] = False
    
    # Propertys
    peso = property(fget = __getPeso)
    beneficio = property(fget = __getBeneficio)

# Realiza una 'cruza' de mochilas
def cruza(mochila1, mochila2):
    # Vemos en que posicion cortamos las mochilas, permutamos las mitades y voila! tenemos dos soluciones hijas
    corte = mochila1.rand.randrange(0, len(mochila1.info))
    
    productos = mochila1.productos
    capacidad = mochila1.capacidad
    
    # Construyo las hijas
    hija1 = Mochila(mochila1.id + 1, productos, capacidad, mochila2.rand)
    hija2 = Mochila(mochila2.id + 1, productos, capacidad, mochila1.rand)
    
    # Ahora cruzo los adn
    hija1.info = mochila1.info[:corte] + mochila2.info[corte:]
    hija2.info = mochila2.info[:corte] + mochila1.info[corte:]
    
    # Ahora las reparo ...
    hija1.reparar()
    hija2.reparar() 
    
    return hija1, hija2

# Muta una solucion
def mutar(mochila):
    adn_mutado = mochila.info[:]
    
    hebra = mochila.rand.randrange(0, len(mochila.info)) # Hebra a mutar
    adn_mutado[hebra] = not adn_mutado[hebra] # Si esta activo lo desactiva, si esta inactivo, lo activa
    
    mut = Mochila(mochila.id, mochila.productos, mochila.capacidad, mochila.rand)
    mut.info = adn_mutado
    mut.reparar()
    
    return mut
