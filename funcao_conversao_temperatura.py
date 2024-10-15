def conversor_temperatura(valor, opc):
    while True:

       if opc == 1:
            fahrenheit = (valor * 1.8) + 32
            print(f'o valor de  Fahrenheit para celsius é {fahrenheit} ')
            break
       if opc == 2:
            celsius = (valor -32) * 1.80
            print(f'o valor de  Fahrenheit para celsius é {celsius} ')
            break
       else:
          print("valor invalido digite novamente!")
          opc = int(input("digite 1 para converter em fahrenheit e 2 para celsius: "))

valor = float(input("digite o valor da temperatura: "))
opc = int(input("digite 1 para converter em fahrenheit e 2 para celsius: "))

conversor_temperatura(valor,opc)


