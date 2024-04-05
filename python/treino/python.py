a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
media = float(input('Digite a média desejada: '))

if (a + b) / 2 < media:
    desviomed = media - (a+b)/2
    print('Você não está aprovado, houve um desvio de ',desviomed,' da média da sua instituição')
else:
    print('Você está aprovado.')
