'''
Created on 14/06/2013

@author: pperez
'''

import random
import math
import ciudad
from solucion import Solucion, rango_id

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
print
print '-' * 50
print 'Metodo estocastico'
print '-' * 50
print

for id_sol in rango_id(id_sol, casos_estocastico):
    ciudades_al_azar = ciudades[:] # Una copia completa sin referencias, igual deberia dar lo mismo, si siempre la desordeno ...
    rand.shuffle(ciudades_al_azar)
    
    # Genero una nueva solucion, esta vez con las ciudades desordenadas
    sol = Solucion(id_sol, ciudades_al_azar, rand)
    
    if sol.fitness() < mejor_solucion.fitness():
        mejor_solucion = sol
#         print 'MS: {0}'.format(sol)
    else:
        pass
#         print 'PS: {0}'.format(sol)

print 'La mejor solucion (Por metodo estocastico) fue: {0:.2f} km'.format(mejor_solucion.fitness())

print
print '-' * 50
print 'Metodo gradiente descendente'
print '-' * 50
print

for id_sol in rango_id(id_sol, casos_gradiente):
    vecina = mejor_solucion.getVecina(id_sol)
  
    if vecina.fitness() < mejor_solucion.fitness():
        mejor_solucion = vecina
#         print 'MS (vecina): {0}'.format(sol)
    else:
        pass
#         print 'PS (vecina): {0}'.format(sol)

print 'La mejor solucion (Por metodo de gradiente decendente) fue: {0:.2f} km'.format(mejor_solucion.fitness())

print
print '-' * 50
print 'Metodo de recocido simulado'
print '-' * 50
print

sol = mejor_solucion

for id_sol in rango_id(id_sol, casos_sa):
    vecina = sol.getVecina(id_sol)
    if vecina.fitness() < sol.fitness(): # Si la vecina es mejor, salto altiro po!
        sol = vecina
    else: # Vemos si nos pegamos el salto de vecindad aunque la solucion no sea mejor ... escapar con la vecina aunque no sea tan buena
        diff = vecina.fitness() - sol.fitness()
        prob = math.exp(-1 * diff / T)
        if prob > rand.random():
            sol = vecina
    #print sol.fitness()
        
    if sol.fitness() < mejor_solucion.fitness(): # Finalmente veo si la solucion obtenida es mejor que la que tenia
            mejor_solucion = sol
    T -= T * disminucion_SA

print 'La mejor solucion (Por metodo de recocido simulado) fue: {0:.2f} km'.format(mejor_solucion.fitness())