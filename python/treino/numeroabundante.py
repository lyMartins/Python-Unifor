# print('ALGORITMO ABUNDANTE')
# n = int(input('insira o tamanho da sequencia que você deseja :'))

# def divisores (n) :
#     def somatorio_div(num) : 
#         soma = 0
#         for i in range(1, num + 1) :
#             if num % i == 0 :
#                 soma += i
#             return soma 
        
#     abundantes = []
#     for num in range(1,n) :
#         if somatorio_div > num :
#             abundantes.append(num) 
#     return abundantes

# print(f'{abundantes}')
def somatorio_div(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma

def numeros_abundantes(n):
    abundantes = []
    for num in range(1, n):
        if somatorio_div(num) > num:
            abundantes.append(num)
    return abundantes

print('ALGORITMO ABUNDANTE')
n = int(input('Insira o tamanho da sequência que você deseja: '))

if n > 0 :
    resultado_somatorio = somatorio_div(n)
    resultado_lista = numeros_abundantes(n)
    print(f'Números abundantes menores que {n}: {resultado_lista}')

else :
    print('insira uma sequencia positiva!!')

