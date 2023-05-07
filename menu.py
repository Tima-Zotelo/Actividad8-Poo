import os


class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1: self.opc1,
                            2: self.opc2,
                            3: self.opc3,
                            4: self.opc4,
                            0: self.salir
                        }
        
    def opcion(self,op, xA, xB):
        func=self.__switcher.get(op, lambda: print("Opción no válida, intente de nuevo"))
        if op == 1 or op == 2 or op == 3 or op == 4:
            func(xA, xB)
        else:
            func()

    def mostrarMenu(self):
        print("""
---------->Menu Principal<----------

-> 1: Cargar conjuntos con valores por defecto 
-> 2: Realizar Union (1)
-> 3: Realizar diferencia (2)
-> 4: Verificar igualdad (3)
-> 0: Salir del programa
""")

## OPCIONES

    def opc1 (self, xA, xB):
        os.system('cls')
        xA.cargar()
        xB.cargar(2)
        print (f'Conjunto A: {xA.obtenerLista()}')
        print (f'Conjunto B: {xB.obtenerLista()}')

    def opc2 (self, xA, xB):
        os.system('cls')
        print ('---------->Union de conjuntos<----------')
        C = xA + xB
        print (f'conjunto nuevo: {C.obtenerLista()}')

    def opc3 (self, xA, xB):
        os.system('cls')
        print ('---------->Diferencia de conjuntos<----------')
        C = xA - xB
        print (f'conjunto nuevo: {C.obtenerLista()}')
        return
    
    def opc4 (self, xA, xB):
        os.system('cls')
        print ('---------->Igualdad de conjuntos<----------')
        if xA == xB:
            print ('son iguales!')
        else: print ('son diferentes')
    
    def salir (self):
        print ('saliendo...')