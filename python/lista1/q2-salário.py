salario = float(input('insira seu salário :'))

if salario <= 500 :
    salario_reajustado = salario * 1.2
    aumento = salario_reajustado - salario
    print(f'o seu salário reajustado agora é {salario_reajustado}, tendo um aumento de {aumento}')
else :
    salario_reajustado = salario * 1.1
    aumento = salario_reajustado - salario
    print(f'o seu salário reajustado agora é {salario_reajustado}, tendo um aumento de {aumento}')