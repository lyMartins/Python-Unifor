n = int(input('insira o tamanho da contagem :'))
multiplo = int(input('insira os multiplos que você deseja :'))

for i in range(1,n + 1) :
    if i % multiplo == 0 :
        print(i)