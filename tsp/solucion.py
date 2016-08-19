'''
Created on 14/06/2013

@author: pperez
'''

class Solucion:
    def __init__(self, id_, ciudades, rng):
        self.ciudades = []
        self.id = id_
        self.ciudades.extend(ciudades)
        self.rng = rng # Random number generator
    
    def __str__(self):
        return 'Solucion(id = {id}, d = {d:.2f} km)'.format(id = self.id, d = self.fitness())
    
    def fitness(self):
        suma = 0
        ciudades = self.ciudades
        for ciudad_a, ciudad_b in zip(ciudades, ciudades[1:]):
            dist = ciudad_a.distanceTo_gps(ciudad_b)
            suma += dist
        return suma
    
    def getVecina(self, id_): # Genera una solucion 'vecina', es similar a la solucion original (Intercambia dos ciudades)
        rand = self.rng
        ciudades = self.ciudades[:]
        r1 = rand.randint(0, len(ciudades) - 1) # Posicion de intercambio
        r2 = rand.randint(0, len(ciudades) - 1) # Posicion de intercambio
        temp = ciudades[r1]
        ciudades[r1] = ciudades[r2]
        ciudades[r2] = temp
        
        return Solucion(id_, ciudades, rand)
