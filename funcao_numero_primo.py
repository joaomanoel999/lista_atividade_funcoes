def primo(num):
    primo = 0
    primo_existe = False
    for n in range(1,num+1):
        if num % n == 0:
            primo += 1
    
    if primo == 2:
        primo_existe = True
        print('este numero é primo')
        
    else:
        print('este numero não é primo')
    

num = int(input("digite um numero: "))

primo(num)
