num = int(input('digite um numero: '))

def sinal_numero(num):
   
    if num < 0 or num == 0:
        return print("N")
    else:
        return print('P')
    
    

sinal_numero(num)