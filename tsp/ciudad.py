'''
Created on 14/06/2013

@author: pperez
'''

import math

def from_tsplib(fichero):
    head = ('id_', 'x', 'y') # Keys del constructor ciudad
    l = [] # Aqui guardamos las ciudades
    fichero = open(fichero) # Abrimos el archivo, filo con excepciones y blabla
    ciudades = [linea.rstrip() for linea in fichero.readlines()[6:-1]] # Cortamos las lineas innecesarias
    
    for ciudad in ciudades:
        ciudad = dict(zip(head, ciudad.split())) # Construimos una ciudad desde los valores del fichero
        l.append(Ciudad(**ciudad))
    return l

class Ciudad:
    def __init__(self, id_, x, y):
        self.id = id_
        self.x = float(x)
        self.y = float(y)
    
    def __str__(self):
        return 'Ciudad(id = {id}, x = {x}, y = {y})'.format(id = self.id, x = self.x, y = self.y)
    
    def __repr__(self):
        return self.__str__()
    
    def setId(self, id_):
        self.id = id_
    
    def distanceTo(self, ciudad):  # Calcula la distancia euclidiana a otra ciudad
        x1, y1 = self.x, self.y
        x2, y2 = ciudad.x, ciudad.y
        return int(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))
    
    def distanceTo_gps(self, ciudad): # Calcula la distancia [km] entre dos puntos (coordenadas gps) # Haversine
        lat_i, lon_i, lat_f, lon_f = map(math.radians, (self.x, self.y, ciudad.x, ciudad.y))
        
        d_lat = lat_f - lat_i
        d_lon = lon_f - lon_i
        
        a = math.sin(d_lat/2)**2 + math.cos(lat_i) * math.cos(lat_f) * math.sin(d_lon/2)**2
        c = 2 * math.atan2(math.sqrt(a),  math.sqrt(1-a))
        
        return 6371 * c
