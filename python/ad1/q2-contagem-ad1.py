# n = int(input('insira o número de alunos :'))
# cont = 0
# i = 1

# while i <= n : 
#     nota = float(input(f'Digite a nota do aluno {i} :'))
# if nota >= 50 and nota <= 100 :
#     cont += 1
#     i += 1
# else :
#     print(f'o número de alunos aprovados é {cont}')

n = int(input('Insira o número de alunos: '))
cont = 0

for i in range(1, n + 1):
    nota = float(input(f'Digite a nota {i}: '))
    if nota >= 50 and nota <= 100:
        cont += 1

print('O número de alunos aprovados é:', cont)
