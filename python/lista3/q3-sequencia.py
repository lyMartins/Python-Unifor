n = int(input('Insira o tamanho da sequência: '))
i = 1
soma = 0

while i <= n:
    num = int(input(f'Digite o número {i}: '))
    soma += num
    i += 1

print('A soma dos números é:', soma)