'''
Angel Geovanny Ordon Colchaj
201905741
Tarea 1
'''

import os
import subprocess, sys
#clear = lambda: os.system('clear')

#opener = "open" if sys.platform == "darwin" else "xdg-open"

def clear():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        subprocess.call('clear', shell=True)

def open_file(filename):
    if sys.platform == 'win32':
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

print("Bienvenido")
print("Graphviz")
print("")

def menu():
    print("(1) Datos del programador")
    print("(2) Generar grafo")
    print("(3) Salir del programa")
    entrada = str(input("Ingrese una opcion: "))
    return entrada

def crearNodo(identificador, nombre, shape, color):
    return identificador + "[label=\"" + nombre + "\", shape=" + shape + ", style=filled, fillcolor = " + color + "]\n"

def unirNodo(nodoA, nodoB):
    return nodoA + "->" + nodoB + "\n"

def crearGrafo():
    file = open("grafo.dot", "w")
    file.write("digraph G{\n")
    file.write(crearNodo("A", "Tarea 1", "Mdiamond", "darkseagreen1"))
    file.write(crearNodo("B", "201905741", "ellipse", "gold"))
    file.write(crearNodo("C", "Angel Geovanny", "ellipse", "lemonchiffon2"))
    file.write(crearNodo("D", "Ordon Colchaj", "ellipse", "lemonchiffon2"))
    file.write(crearNodo("F", "Lenguajes Formales y de Programacion", "house", "snow2"))
    file.write(crearNodo("G", "B-", "Msquare", "paleturquoise1"))
    file.write(crearNodo("H", "A", "Mcircle", "paleturquoise1"))
    file.write(unirNodo("A", "B"))
    file.write(unirNodo("B", "C"))
    file.write(unirNodo("B", "D"))

    #file.write(unirNodo("C", "D"))

    file.write(unirNodo("C", "F"))
    file.write(unirNodo("D", "F"))

    file.write(unirNodo("F", "G"))
    file.write(unirNodo("G", "H"))
    file.write("}")
    file.close()
    os.system('dot -Tpng grafo.dot -o grafo.png')
    open_file("grafo.png")
    #subprocess.call([opener, "grafo.png"])
    #os.startfile("grafo.png")

ciclo = True
while(ciclo):
    entrada = menu()
    if entrada == "1":
        print("")
        print("- Carnet:")
        print("201905741")
        print("- Nombres:")
        print("Angel Geovanny")
        print("- Apellidos:")
        print("Ordon Colchaj")
        print("- Curso:")
        print("Lenguajes Formales y de Programacion")
        print("- Seccion Magistral:")
        print("B-")
        print("- Grupo Laboratorio:")
        print("A")
        print("")
        raw_input("")
    elif entrada == "2":
        print("")
        crearGrafo()
        print("")
        raw_input("")
    elif entrada == "3":
        print("")
        print("Gracias por utilizar el programa")
        print("")
        raw_input("")
        ciclo = False
    else:
        print("Ingrese una opcion valida")
        raw_input("")
    clear()