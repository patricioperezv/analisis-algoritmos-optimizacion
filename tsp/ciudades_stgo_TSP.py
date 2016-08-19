#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Genera un fichero en formato TSPLIB
# Created on 14/06/2013
# @author: pperez

import requests
from bs4 import BeautifulSoup
from geopy import geocoders

# Headers de TSPLIB
tsp = '''NAME: stgo01
TYPE: TSP
COMMENT: 37 locations in Santiago (Pperez)
DIMENSION: 37
EDGE_WEIGHT_TYPE: EUC_2D
NODE_COORD_SECTION
{nodos}
EOF'''

# Codigo pais
country = 'CL'

# Usaremos google maps api v3
mapa = geocoders.GoogleV3()

# Establecer el encoding
encoding = 'utf-8'

# Obtenemos la pagina que lista las ciudades de chile desde wikipedia
r = requests.get('http://es.wikipedia.org/wiki/Santiago_de_Chile')

# Construimos la sopa :)
pagina = BeautifulSoup(r.text)

# Obtenemos la lista de comunas # Hack-ish
# Es la quinta tabla, el primer td, y el primer link no es una comuna
comunas =  pagina.findAll('table')[5].td.findAll('a')[1:]

comunas = [u'{comuna}, {region}'.format(comuna = comuna.getText(), region = 'Santiago Metropolitan Region') for comuna in comunas]

# Keys para el diccionario
keys = ('id', 'latitud', 'longitud')

# Acumula los nodos con su id, latitud y longitud
ac = []

# Iteramos por las comunas, le pedimos a la libreria la latitud y longitud de la comuna
for i, comuna in enumerate(comunas, start = 1):
    try:
        # Armamos una tupla de tipo (id, latitud, longitud). ej: (30, -33.3776308, -70.5621902)
        values = (i,) + mapa.geocode(comuna, region = country)[1] # El valor 0 de la tupla mapa.geocode(...) da el nombre, no es necesario
    except ValueError: # La libreria lanza un ValueError si hizo match a mas de una ciudad, mejor preguntemosle al usuario
        print '-' * 50
        print u'No se encontro {comuna}, por favor ingrese su latitud y longitud separadas por espacio'.format(comuna = comuna)
        s = raw_input()
        values = [i] + s.split() # Separamos el string por espacios
    finally:
        ciudad = dict(zip(keys, values))
        ac.append('{id} {latitud} {longitud}'.format(**ciudad))

print tsp.format(nodos = '\n'.join(ac))
