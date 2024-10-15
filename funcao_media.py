def media(num):
    soma = 0
    for n in num:
        soma += n
    print(f'a media dos numeros é: {soma / len(num)}')


num = [10,25,5,70,40]

media(num)