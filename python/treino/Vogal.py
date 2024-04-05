print('ALGORITMO VOGAL')

palavra = input('insira a palavra desejada :')

def vogal(palavra) : 
    # palavra = list(palavra) // não precisa ser usada, pois o filter atua diretamente na string
    vogais = list(filter(lambda x: x.lower() in 'aeiou',palavra))
    return vogais 

result_vogais = vogal(palavra)
numero_vogais = len(result_vogais)
print(f'a palavra {palavra} tem {numero_vogais} número de vogais que são {result_vogais}')


# # Palavra fornecida pelo usuário
# palavra = input("Digite uma palavra: ")

# # Converter a palavra em uma lista de caracteres
# lista_letras = list(palavra)

# # Imprimir a lista de letras
# print("Lista de letras:", lista_letras)