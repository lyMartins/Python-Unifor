print('algoritmo texto')

texto = input('insira um texto :')
print(texto)

def analise_texto(texto) :
    palavras = texto.split()
    contagem = {}
    
    for palavras in palavras :
        if palavras in contagem :
            contagem[palavras] += 1
        else :
            contagem[palavras] = 1

    return contagem 

relatorio = analise_texto(texto)


print("Contagem de termos:")
for palavra, frequencia in relatorio.items():
    print(f'{palavra}: {frequencia}')
# print(f'No texto, o termo "{texto}" aparece {relatorio} vezes.')

