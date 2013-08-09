'''
Created on 08/08/2013

@author: pperez
'''

class Producto(object):
    '''
    classdocs
    '''


    def __init__(self, id_, rng, peso = None, beneficio = None):
        '''
        Constructor
        '''
        
        self.id = id_
        self.beneficio = beneficio
        
        self.peso = rng.randint(0, 1000) if peso is None else peso # Al azar si no pasa nada
        self.beneficio = rng.randint(0, 500) if beneficio is None else beneficio # Al azar si no pasa nada
    
    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        return 'Producto(nombre = {0}, peso = {1}, beneficio = {2})'.format(self.id, self.peso, self.beneficio)