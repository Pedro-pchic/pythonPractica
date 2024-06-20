def calculador ():
    digit = 5
    print('el valor es ',digit)
    
digit = 8
calculador()
print(digit)

def calculador ():
    global digit
    digit *= 5
    print('el valor es ',digit)
    
digit = 8
calculador()
print(digit)

def calculador (n):
    print(n)
    n +=7
    print('el valor es ', n)
    
digit = 1
calculador(digit)
print(digit)

print('funciones')
def fewnumbers(number):
    print(number)
    del number[0]

digits = [5,7,9,23]
fewnumbers(digits)#solo tema del primer digito
print(digits)