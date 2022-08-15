"""
Instrucciones de tareas:
Solicitar al usuario dos valores, y determinar cual número es el mayor
Solicitar al usuario dos valores:
numero1 (int)
numero2 (int)
Se debe imprimir el mayor de los dos números (la salida debe ser identica a la que sigue):
Proporciona el numero1:
Proporciona el numero2:
El numero mayor es:<numeroMayor>
"""

numero1=int(input('Proporciona el numero 1: '))
numero2=int(input('Proporciona el numero 2: '))
print('El numero mayor es: ', str(numero1) if numero1 > numero2 else str(numero2))