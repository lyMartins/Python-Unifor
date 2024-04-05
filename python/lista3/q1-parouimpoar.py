n = int(input('Insira um número inteiro: '))

while n <= 0:
    print('Por favor, insira um número inteiro positivo.')
    n = int(input('Insira um número inteiro: '))

if n % 2 == 0:
    print('Seu número', n, 'é par.')
else:
    print('Seu número', n, 'é ímpar.')


# n = int(input('Insira o número : '))  

# while n % 2 == 0 : 
#    if n >=0 :
#         print ('seu número,',n,'é par')
#         break
# else : 
#     print('seu número é impar')
                    

