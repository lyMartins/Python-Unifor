n = int(input('Digite um numero inteiro nao-negativo :'))

if n >= 0 :
    fator = 1
    for i in range(1,n + 1) :
        fator *= i
    
    else : 
        print(f'o fatorial de {n} é {fator}')    
    
else :
    print('O valor deve ser maior ou igual a zero!')


