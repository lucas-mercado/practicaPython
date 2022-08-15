"""
Instrucciones de la tarea:
El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
El usuario proporcionará un valor entre 0 y 10.
Si está entre 9 y 10: imprimir una A
Si está entre 8 y menor a 9: imprimir una B
Si está entre 7 y menor a 8: imprimir una C
Si está entre 6 y menor a 7: imprimir una D
Si está entre 0 y menor a 6: imprimir una F
cualquier otro valor debe imprimir: Valor incorrecto
Por ejemplo:
Proporciona un valor entre 0 y 10:
A
"""

nota=int(input('Proporciona un valor entre el 0 y 10 :'))
if 8 < nota < 11:
    print('A')
elif 7 < nota < 9:
    print('B')
elif 6 < nota < 8:
    print('C')
elif 5 < nota < 7:
    print('D')
elif -1 < nota < 6:
    print('F')
else:
    print('Valor Incorrecto')