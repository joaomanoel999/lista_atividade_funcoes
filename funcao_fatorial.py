def fatorial(num):
    fatorial = 1
    for n in range(1,num+1):
        fatorial *= n
    print(f'o fatorial é: {fatorial}')

while True:
    num = int(input('digite um numero positivo: '))
    if num <= 0:
        print('este numero é negativo ou 0!')
        
    if num > 0:
        break

fatorial(num)