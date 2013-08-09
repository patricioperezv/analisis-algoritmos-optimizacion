'''
Created on 08/08/2013

@author: pperez
'''

class Solucion(object):
    '''
    classdocs
    '''


    def __init__(self, productos, rng, disponible):
        '''
        Constructor
        '''
        self.productos = productos[:] # Copia de la lista productos
        self.rng = rng
        self.disponible = disponible
        self.lollevo = [False] * len(productos) # Por defecto mi mochila esta vacia
        self.peso = 0
        self.beneficio = 0
    
#     def __getBeneficio(self):
#         count = 0
#         for idx, llevar in enumerate(self.lollevo):
#             if llevar: # El producto se agrega a la mochila
#                 count += self.productos[idx].beneficio
#         return count
#     
#     def __getPeso(self):
#         count = 0
#         for idx, llevar in enumerate(self.lollevo):
#             if llevar: # El producto se agrega a la mochila
#                 count += self.productos[idx].peso
#         return count
#     
#     beneficio = property(fget = __getBeneficio)
#     peso = property(fget = __getPeso)
#     
    def genAleatoria(self):
        while self.disponible > self.peso: # Mientras tengamos espacio en la mochila
            prods = [producto for producto, lollevo in zip(self.productos, self.lollevo) if not lollevo] # Productos que no estan en la mochila, –am
            candidato = self.rng.choice(prods) # Elegimos aleatoriamente un producto que no estaba en la mochila
            if (self.peso +  candidato.peso) <= self.disponible: # Cabe en la mochila!
                self.lollevo[candidato.id] = True # Llevamos el item en la mochila
                self.disponible -= candidato.peso # Descontamos el peso del item del disponible en la mochila
                self.peso += candidato.peso
                self.beneficio += candidato.beneficio

def genAleatoria(id_, productos, rng, disponible):
    lollevo = [False] * len(productos) # Aun no llevo ningun producto en mi mochila
    