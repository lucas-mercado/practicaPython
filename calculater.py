def operacion(op):
    from functools import reduce
    
    def suma(*args):
        return reduce(lambda x,y: x + y, args)

    def resta(*args):
        return reduce(lambda x,y: x - y, args)
    
    if op=='+':
        return suma
    if op=='-':
        return resta
    
operation = operacion('+')
print(operation(1,2,2))

operation = operacion('-')
print(operation(1,2,1))