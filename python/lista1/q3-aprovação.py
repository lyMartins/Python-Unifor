nota1 = float(input('Insira a primeira nota :'))
nota2 = float(input('Insira a segunda nota :'))
media = int(input('Insira a média necessária para passar :'))

if nota1 >= 0 and nota2 >= 0 :
    media_aluno = (nota1+nota2)/2
    if media_aluno >= media :
        print('você foi aprovado!!')
    else :
        print('você não atingiu a média necessária para passar')
else: 
    print('insira válores válidos!!')