import os
from menu import Menu
from claseConjunto import Conjunto


if __name__ == '__main__':
    A = Conjunto()
    B = Conjunto()
    bandera = False
    menu = Menu()
    os.system('cls')
    while not bandera:
        menu.mostrarMenu()
        opcion = int (input("Su opcion: "))
        menu.opcion(opcion, A, B)
        if opcion == 0:
            bandera = True
        os.system('pause')
        os.system('cls')
    os.system('exit')