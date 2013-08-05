#!/usr/bin/env pypy
# -*- coding: utf-8 -*- 

'''
Created on 14/06/2013

@author: pperez
'''

import random
import ciudad
from solucion import Solucion
import metodos

# Cuec
Ciudad = ciudad.Ciudad
# Generador de numeros aleatorios
rand = random.Random(10)

# Traemos las 37 comunas de stgo al baile
ciudades = ciudad.from_tsplib('stgo01.tsp')

# Algoritmo estocastico
casos_estocastico = 600

# Algoritmo gradiente decendente
casos_gradiente = 1200

# Algoritmo simulated annealing
casos_sa = 1000000
T = 1000000 # Temperatura inicial
disminucion_SA = 0.0001 # Decenso de temperatura por iteracion

# Identificador de soluciones
id_sol = 0

mejor_solucion = Solucion(id_sol, ciudades, rand) # Solucion inicial, ciudades tal cual

print 'TSP comunas de Santiago de Chile'

# Metodo estocastico
mejor_solucion = metodos.estocastico(casos_estocastico, mejor_solucion, rand)
print 'La mejor solucion (Por metodo estocastico) fue: {0} km'.format(mejor_solucion)

# Metodo gradiente decendente
mejor_solucion = metodos.gradiente_decendente(casos_gradiente, mejor_solucion, rand)
print 'La mejor solucion (Por metodo de gradiente decendente) fue: {0} km'.format(mejor_solucion)

# Metodo de recocido simulado
mejor_solucion = metodos.recocido_simulado(casos_sa, mejor_solucion, T, disminucion_SA, rand)
print 'La mejor solucion (Por metodo de recocido simulado) fue: {0} km'.format(mejor_solucion)
