import os

def limpiar_terminal():
    os.system("cls")

def operacion_anterior(memoria):
    for i in memoria:
        print(i, end="")
