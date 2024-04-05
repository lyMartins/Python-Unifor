# n1 = float(input('insira o primeiro número :'))
# n2 = float(input('insira o segundo número :'))
# n3 = float(input('insira o terceiro número :'))
# n4 = float(input('insira o quarto número :'))

# media = (n1+n2+n3+n4) / 4 

# print('a média desses números é ', media)

n = int(input('quantos números quer fazer a média? :'))
i = 1
soma = 0

while i <= n :
    num = float(input(f'insira o número {i} :'))
    i += 1
    soma += num

else :
    media = soma/n
    print(f'a média desses números é {media}')


