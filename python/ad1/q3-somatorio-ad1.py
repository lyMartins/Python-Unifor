n = int(input('insira o tamanho da sequencia: '))

if n >= 0:
    soma = 0
    i = 1
    while i <= n :
        num = float(input(f'Insira o número {i}: '))
        soma += num
        i += 1 
    print('a soma dos números é ', soma)
else : 
    print('o número precisa ser positivo ')
# ////////////////////////////////////////////////////////////
# n = int(input('Insira o tamanho da sequência: '))

# if n >= 0:
#     soma = 0
#     i = 1
#     while i <= n:
#         num = float(input(f'Insira o número {i}: '))
#         soma += num
#         i += 1 
#     print('A soma dos números é', soma)
# else:
#     print('O tamanho da sequência deve ser um número não negativo.')