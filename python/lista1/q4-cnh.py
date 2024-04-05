idade = int(input('Insira a sua idade :'))

if idade >= 18 :
    print('você tem a idade necessária para tirar sua CNH!')
else :
    anosFaltando = 18 - idade
    if anosFaltando == 1 :
        print('você ainda não tem a idade necessária para tirar sua CNH, faltam ', anosFaltando, ' ano')
    else :
        print('você ainda não tem a idade necessária para tirar sua CNH, faltam ', anosFaltando, ' anos')

