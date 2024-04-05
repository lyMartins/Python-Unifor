n = int(input('Insira o número da série S: '))
S = 0 

for i in range(0, n) :
    numerador = (2 * i) + 1
    denominador = (2 * i) + 2 
    termo_da_serie = numerador / denominador
    S += termo_da_serie
else :
    print(f'a soma da série S é {S}')
