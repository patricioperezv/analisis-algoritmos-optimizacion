'''
Created on 04/08/2013

@author: pperez
'''

import math
from solucion import Solucion

def rango_id(id_sol, casos):
    return range(id_sol + 1, id_sol + casos + 1)

def header(nombre, n, s0):
    print
    print
    print '.-.' * 50
    print 'Metodo {0} ({1} soluciones, s0: {2})'.format(nombre, n, s0)
    print '.-.' * 50
    print

def estocastico(n, s0, rand):
    # n: cantidad de soluciones a generar por estocastico
    # s0: solucion inicial
    
    header(estocastico.__name__, n, s0)
    
    mejor = s0
    
    for id_sol in rango_id(s0.id, n):
        ciudades = s0.ciudades[:] # Sacamos una copia, para no modificar a s0
        rand.shuffle(ciudades) # Desordenamos las ciudades, para generar una nueva solucion
        
        sol = Solucion(id_sol, ciudades, rand)
        
        if sol.fitness() < mejor.fitness():
            mejor = sol
        else:
            pass
    return mejor


def gradiente_decendente(n, s0, rand):
    # n: cantidad de soluciones a generar por gradiente
    # s0: solucion inicial
    
    header(gradiente_decendente.__name__, n, s0)
    
    mejor = s0
    
    for id_sol in rango_id(s0.id, n):
        vecina = mejor.getVecina(id_sol)
        if vecina.fitness() < mejor.fitness():
            mejor = vecina
        else:
            pass
    return mejor

def recocido_simulado(n, s0, T, decenso_T, rand):
    # n: cantidad de soluciones a generar por SA
    # s0: solucion inicial
    
    header(recocido_simulado.__name__, n, s0)
    
    mejor = s0
    sol = mejor
    
    for id_sol in rango_id(s0.id, n):
        vecina = sol.getVecina(id_sol)
        
        if vecina.fitness() < sol.fitness(): # Si la vecina es mejor, salto altiro po!
            sol = vecina
        else: # Veamos si nos escapamos con la vecina aunque no sea tan buena ...
            diff = vecina.fitness() - sol.fitness()
            prob = math.exp(-1 * diff / T)
            
            if prob > rand.random(): # Si el azar lo dice saltamos
                sol = vecina
        
        if sol.fitness() < mejor.fitness(): # Finalmente veo si la solucion obtenida es mejor que la que tenia
            mejor = sol
        T -= T * decenso_T
    return mejor
