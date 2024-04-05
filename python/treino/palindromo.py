print('ALGORITMO PALINDROMO')

palavra = input('insira a palavra que quer analisar :')

def analise(palavra) :
    palavra = palavra.replace(" "," ").lower()

    if palavra[::-1] == palavra:
        return True 
    else :
        return False 

if analise(palavra) :
    print(f'a palavra {palavra} é um palíndromo')
else :
    print(f'a palavra {palavra} não é um palíndromo')
