def soma(num1,num2):
    resposta = num1 + num2
    return print(f'o valor da soma é {resposta}')

def subtrair(num1,num2):
    resposta = num1 - num2
    return print(f'o valor da subtração é {resposta}')

def multiplicar(num1,num2):
    resposta = num1 * num2
    return print(f'o valor da multiplicação é {resposta}')

def dividir(num1,num2):
    resposta = num1 /num2
    return print(f'o valor da divisão é {resposta}')

num1= int(input("digite um numero: "))
num2 = int(input("digite outro numero: "))

soma(num1,num2)
subtrair(num1,num2)
multiplicar(num1,num2)
dividir(num1,num2)