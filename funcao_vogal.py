def vogal(palavra):
    cont = 0
    for letra in palavra:
        if letra in 'aeiouAEIOU':
            cont += 1
    print(f'A quantidade de vogais é: {cont}')



palavra = str(input("digite uma palavra: "))
vogal(palavra)