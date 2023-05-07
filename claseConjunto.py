class Conjunto:
    __listaConjunto = []

    def __init__(self):
        self.__listaConjunto = []

    def __add__(self, otro):
        nuevo = Conjunto()
        nuevo.__listaConjunto = list(set(self.__listaConjunto + otro.__listaConjunto))
        return nuevo

    def __sub__(self, otro):
        nuevo = Conjunto()
        nuevo.__listaConjunto = [x for x in self.__listaConjunto if x not in otro.__listaConjunto]
        return nuevo
    
    def __eq__(self, otro):
        return set(self.__listaConjunto) == set(otro.__listaConjunto)

## funciones
    def cargar (self, n=0):
        for i in range (1, 5):
            self.__listaConjunto.append(i + n)

    def obtenerLista (self):
        return self.__listaConjunto
    
    def obtenerElem (self, indice):
        return self.__listaConjunto[indice]
