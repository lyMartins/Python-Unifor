# nota = 0
# soma = 0
# quant = 0

# while nota >= 0 :
#     nota = float(input('insira as notas(uma nota negativa encerrará o algoritmo) :'))
#     if soma >= 0:        
#         soma += nota
#     quant += 1
    
# else :  quant > 0 
# media = soma / (quant - 1)
# print(f'foram lidas {quant - 1} notas e a média delas é {media}')

nota = 0
soma = 0
quant = 0

while nota >= 0:
    nota = float(input('Insira as notas (uma nota negativa encerrará o algoritmo): '))
    if nota >= 0:
        soma += nota
        quant += 1

if quant > 0:
    media = soma / quant
    print(f'Foram lidas {quant} notas e a média delas é {media:.2f}')