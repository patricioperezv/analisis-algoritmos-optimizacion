'''
Created on 14/06/2013

@author: pperez
'''

import random
import ciudad
from solucion import Solucion, rango_id

# Cuec
Ciudad = ciudad.Ciudad
# Generador de numeros aleatorios
rand = random.Random(10)

# Traemos las 37 comunas de stgo al baile
ciudades = ciudad.from_tsplib('stgo01.tsp')

# Algoritmo estocastico
casos_estocastico = 10000

# Algoritmo gradiente decendente
casos_gradiente = 20000

# Identificador de soluciones
id_sol = 0

mejor_solucion = Solucion(id_sol, ciudades) # Solucion inicial, ciudades tal cual

print 'TSP comunas de Santiago de Chile'

# Metodo estocastico
print
print '-' * 50
print 'Metodo estocastico'

for id_sol in rango_id(id_sol, casos_estocastico):
    ciudades_al_azar = ciudades[:] # Una copia completa sin referencias, igual deberia dar lo mismo, si siempre la desordeno ...
    rand.shuffle(ciudades_al_azar)
    
    # Genero una nueva solucion, esta vez con las ciudades desordenadas
    sol = Solucion(id_sol, ciudades_al_azar)
    
    if sol.fitness() < mejor_solucion.fitness():
        mejor_solucion = sol
#         print 'MS: {0}'.format(sol)
    else:
        pass
#         print 'PS: {0}'.format(sol)

print
print 'La mejor solucion (Por metodo estocastico) fue: {0}'.format(mejor_solucion)

print
print '-' * 50
print 'Metodo gradiente descendente'
print

for id_sol in rango_id(id_sol, casos_gradiente):
    sol = mejor_solucion.getVecina(id_sol)
  
    if sol.fitness() < mejor_solucion.fitness():
        mejor_solucion = sol
#         print 'MS (vecina): {0}'.format(sol)
    else:
        pass
#         print 'PS (vecina): {0}'.format(sol)

print 'La mejor solucion (Por metodo de gradiente decendente) fue: {0}'.format(mejor_solucion)
