while True:
    print('1. Técnico')
    print('2. Gerência')
    print('3. Outro')

    cargo = int(input('Insira o número correspondente ao seu cargo: '))
    salario = float(input('Insira seu salário: '))

    if cargo == 1:
        sal_reajust = salario * 1.5
        print('Seu salário reajustado agora é:', sal_reajust)
        break
    elif cargo == 2:
        sal_reajust = salario * 1.3
        print('Seu salário reajustado agora é:', sal_reajust)
        break
    elif cargo == 3:
        sal_reajust = salario * 1.1
        print('Seu salário reajustado agora é:', sal_reajust)
        break
    else:
        print('Este número não é válido. Por favor, escolha 1, 2 ou 3.')

# (CERTO)
# print('1. Técnico')
# print('2. Gerência')
# print('3. Outro')

# cargo = int(input('Insira o número correspondente ao seu cargo: '))
# salario = float(input('Insira seu salário: '))

# if cargo == 1:
#     sal_reajust = salario * 1.5
#     print('Seu salário reajustado agora é:', sal_reajust)
# elif cargo == 2:
#     sal_reajust = salario * 1.3
#     print('Seu salário reajustado agora é:', sal_reajust)
# elif cargo == 3:
#     sal_reajust = salario * 1.1
#     print('Seu salário reajustado agora é:', sal_reajust)
# else:
#     print('Este número não é válido')

# (ERRADO)
# print('1. Técnico')
# print('2. Gerência')
# print('3. Outro')
# cargo = float(input('insira seu cargo :'))
# salario = input('insira seu salário :')

# if cargo == 1 : 
#     sal_reajust = (salario * 1.5)
#     print('seu salário reajustado agora é ', sal_reajust) 
# elif cargo == 2 : 
#     sal_reajust = salario * 1.3 
#     print('seu salário reajustado agora é ', sal_reajust) 
# elif cargo == 3 :
#     sal_reajust = salario * 1.1
#     print('seu salário reajustado agora é ', sal_reajust) 
# else :
#     print('Este número não é válido')
