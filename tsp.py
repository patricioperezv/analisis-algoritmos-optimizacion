'''
Created on 14/06/2013

@author: pperez
'''

from random import Random
from ciudad import Ciudad
from solucion import Solucion

rand = Random(90)

cant_ciudades = 100
ciudades = []

# Algoritmo estocastico
n_estocastico = 10000
casos_vecinas = 20000

for i in range(cant_ciudades):
    ciudad = Ciudad(id_ = i, x = rand.randint(0, 1000), y = rand.randint(0, 1000))
    ciudades.append(ciudad)

mejor_solucion = Solucion(0, ciudades) # Solucion inicial, ciudades tal cual

# Metodo estocastico
print '-' * 50
print 'Metodo estocastico'

for i in range(1, n_estocastico + 1):
    ciudades_al_azar = ciudades[:] # Una copia completa sin referencias, igual deberia dar lo mismo, si siempre la desordeno ...
    rand.shuffle(ciudades_al_azar)
    
    # Genero una nueva solucion, esta vez con las ciudades desordenadas
    sol = Solucion(i, ciudades_al_azar)
    
    if sol.fitness() < mejor_solucion.fitness():
        mejor_solucion = sol
        print 'MS: {0}'.format(sol)
    else:
        pass
#         print 'PS: {0}'.format(sol)

print 'La mejor solucion (Por metodo estocastico) fue: {0}'.format(mejor_solucion)

print '-' * 50
print 'Metodo gradiente descendente'

for i in range(n_estocastico + 1, casos_vecinas):
    sol = mejor_solucion.getVecina(i)
  
    if sol.fitness() < mejor_solucion.fitness():
        mejor_solucion = sol
#         print 'MS (vecina): {0}'.format(sol)
    else:
        pass
#         print 'PS (vecina): {0}'.format(sol)

print 'La mejor solucion (Por metodo de gradiente decendente) fue: {0}'.format(mejor_solucion)