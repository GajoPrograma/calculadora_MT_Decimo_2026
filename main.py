import operaciones
import interfaz

interfaz.limpiar_terminal()
memoria = []
# leer primer número sin necesidad de presionar Enter
num1 = interfaz.leer_numero_sin_enter(" ")
interfaz.limpiar_terminal()
memoria.append(num1)
i = "si"
resultado = 0
while (i == "si"):
    interfaz.operacion_anterior(memoria)
    operacion = interfaz.leer_operacion_sin_enter(" ")
    print(operacion)
    memoria.append(operacion)
    interfaz.limpiar_terminal()
    if operacion == "=":
        break
    interfaz.operacion_anterior(memoria)
    num2 = interfaz.leer_numero_sin_enter(" ")
    interfaz.limpiar_terminal()
    if operacion == "+":
        resultado =operaciones.sumar(num1,num2)
    elif operacion == "-":
        resultado =operaciones.restar(num1,num2)
    elif operacion == "*":
        resultado =operaciones.multiplicar(num1,num2)
    elif operacion == "^":
            resultado =operaciones.radicacion(num1,num2)
    elif operacion == "!":
            resultado =operaciones.potenciacion(num1,num2)
    elif operacion == "%":
            resultado =operaciones.porcentaje(num1,num2)
    elif operacion == "Log":
            resultado =operaciones.logaritmacion(num1,num2)
    elif operacion == "/":
        if num2 == 0:
            print("opcion invalida")
        else:
            resultado =operaciones.dividir(num1,num2)
    else:
        print("opción no valida")
      
    
    memoria.append(num2)
    num1=resultado
       
for i in memoria:
    
    print(i, end="")

print("=", resultado)
