'''
Created on 14/06/2013

@author: pperez
'''

from random import Random

rand = Random(111)

class Solucion:
    def __init__(self, id_, ciudades):
        self.ciudades = []
        self.id = id_
        self.ciudades.extend(ciudades)
    
    def __str__(self):
        return "Solucion(id = %s, f = %s)" % (self.id, self.fitness())
    
    def fitness(self):
        suma = 0
        ciudades = self.ciudades
        for ciudad_a, ciudad_b in zip(ciudades, ciudades[1:]):
            dist = ciudad_a.distanceTo(ciudad_b)
            suma += dist
        return suma
    
    def getVecina(self, id_):
        ciudades = self.ciudades[:]
        r1 = rand.randint(0, len(ciudades) - 1) # Posicion de intercambio
        r2 = rand.randint(0, len(ciudades) - 1) # Posicion de intercambio
        temp = ciudades[r1]
        ciudades[r1] = ciudades[r2]
        ciudades[r2] = temp
        
        return Solucion(id_, ciudades)