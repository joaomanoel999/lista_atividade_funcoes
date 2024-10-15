def usuario(email):
    cont = 0
    for letra in email:
        if letra in '@':
            cont += 1
    if cont > 0:
        print('existe @')
    else:
        print("não tem @")


email = str(input("digite o email: "))
usuario(email)