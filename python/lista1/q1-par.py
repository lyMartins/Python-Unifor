n = int(input('Insira um número inteiro e positivo :'))

if n >= 0 :
    resto = n % 2
    if resto == 0 :
        print(f'o número {n} par')
    else : 
        print(f'o número {n} é impar')
else : 
    print('esté número não é positivo!!')


