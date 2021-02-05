
def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y 

def division(x,y):
    if y == 0: 
        raise ValueError('Cannot divide by 0!')
    return  x / y  