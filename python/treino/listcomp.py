input_palavra = input('insira a palavra :')
vogais = [letra for letra in input_palavra if letra.lower() in 'aeiou']
print (vogais)