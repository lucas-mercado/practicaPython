'''
Proporciona tu edad:

0-10: La infancia es increíble...
10-20: Muchos cambios y mucho estudio... 
20-30: Amor y comienza el trabajo...

Cualquier otro valor: Etapa de vida no reconocida
'''

edad=int(input('Proporciona tu Edad: '))

if 7 < edad < 11:
    print('La infancia es increible!!!')
elif 10 < edad < 21:
    print('Muchos cambios y mucho estudio!!!') 
elif 20 < edad < 31: 
    print('Amor y comienza el trabajo !!!')
else:
    print('Etapa de la vida no reconocida.')

