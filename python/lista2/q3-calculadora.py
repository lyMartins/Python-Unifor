a = float(input('Insira o primeiro número: '))
b = float(input('Insira o segundo número: '))
soma = a + b
sub = a - b
mult = a * b
div = a / b
exp = a ** b
operador = input('Insira a operação que quer fazer (+ para soma, - para subtração, * para multiplicação, / para divisão, ** para exponenciação): ')

if operador == '+':
    print('Seu resultado é', soma)
elif operador == '-':
    print('Seu resultado deu', sub)
elif operador == '*':
    print('Seu resultado deu', mult)
elif operador == '/':
    print('Seu resultado deu', div)
elif operador == '**':
    print('Seu resultado deu', exp)
else:
    print('Operador inválido.')
    