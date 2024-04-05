import time
a = int(input('insira a área do algoritmo :'))
objeto = 'teste'
espaco = (" " * a)
for i in range(len(espaco)):
    if i % 2 == 0:  # Se i for par
        print(espaco[:i] + objeto)
    else:
        print(espaco[:len(espaco) - i] + objeto)
    time.sleep(0.1)





















# import time

# objeto = 'teste'
# espaco = " " * 30
# posicao_par = espaco % 2
# 0 == espaco % 2 

# for i in range(len(espaco)):                                                                    
#     if i == posicao_par:                                                                  
#         print(espaco[:i] + objeto)
#         time.sleep(0.1)
#     else :
#         print(espaco[:-i] + objeto)
#         time.sleep(0.1)