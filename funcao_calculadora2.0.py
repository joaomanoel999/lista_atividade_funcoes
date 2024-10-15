import os
import time

num1 = int(input("digite um numero: "))
num2 = int(input("digite outro numero: "))
print("digite 1 para somar| 2 para subtrair | 3 para multiplicar | 4 para dividir")
op = int(input("digite o numero da operação: "))


def calculadora2(num1,num2,op):
    

    while True:
        if op == 1:
                resultado = num1 + num2
                print(resultado)
                break
        if op == 2:
                resultado = num1 - num2
                print(resultado)
                break
        if op == 3:
                resultado = num1 * num2
                print(resultado)
                break
        if op == 4:
            resultado = num1 / num2
            print(resultado)
            break
        else:
            print('opção invalida, tente novamente!')
            time.sleep(2)
            os.system('cls')
            print("digite 1 para somar| 2 para subtrair | 3 para multiplicar | 4 para dividir")
            op = int(input("digite o numero da operação: "))



calculadora2(num1,num2,op)