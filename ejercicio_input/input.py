from ast import excepthandler
from pickle import FALSE


result=''

def is_valid(value):
    '''
        valida si es un nro y esta dentro del rango 1-10
    '''
    try:
       value=int(value) 
       if value > 0 and value < 11:
          return True
       else:
          return False  
    except Exception as e:
       return False

while not is_valid(result):
    result=input('Como estuvo tu dia (1-10)')

print('Mi dia estuvo de :',result)
