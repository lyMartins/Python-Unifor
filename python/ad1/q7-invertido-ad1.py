num = int(input('insira um número inteiro positivo :'))

if num >= 0 :
    num_inv = 0
    
    while num > 0  :
            digito = num % 10 
            num_inv = num_inv * 10 + digito 
            num = num // 10 

    else : 
        print(f'o número invertido é {num_inv}')
else :
        print('o número deve ser positivo!!')

