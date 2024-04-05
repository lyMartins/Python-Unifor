n = int(input('Insira a quantidade de termos da sequencia de fibonacci que você deseja :'))
a = 0
b = 1

for i in range(1, n + 1) :
    print(f'{a}')
    termo_at = a + b
    a = b
    b = termo_at

# n = int(input('Insira a quantidade de termos da sequência de Fibonacci que você deseja: '))
# a = 0
# b = 1
# fibonacci_sequence = ""

# for i in range(1, n + 1):
#     fibonacci_sequence += str(a) + ", "
#     termo_atual = a + b
#     a = b
#     b = termo_atual

# # Remova a vírgula extra no final da sequência
# fibonacci_sequence = fibonacci_sequence[:-2]

# print(fibonacci_sequence)

