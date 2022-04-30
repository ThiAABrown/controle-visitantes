#Gerador de CPF

import random


def gerar_cpf():

    # n1 = random.randint(0, 9)
    # n2 = random.randint(0, 9)
    # n3 = random.randint(0, 9)
    # n4 = random.randint(0, 9)
    # n5 = random.randint(0, 9)
    # n6 = random.randint(0, 9)
    # n7 = random.randint(0, 9)
    # n8 = random.randint(0, 9)
    # n9 = random.randint(0, 9)

    # print(n1, n2, n3, n4, n5, n6, n7, n8, n9)
 
    cpf = []
    for n in range(9):
        cpf.append(random.randint(0, 9))
    print(cpf)

    #outra opcao
    # cpf = [random.randint(0, 9) for n in range(9)]
    # print(cpf)
# ------------------------------------------------------------------------
    
    #primeiro digito n10
    # n10 = round(((n1 * 1) + (n2 * 2) + (n3 * 3) + (n4 * 4) + (n5 * 5) + (n6 * 6) + (n7 * 7) + (n8 * 8) + (n9 * 9)) % 11)

    # if n10 < 3 or n10 > 9:
    #     n10 = 0
    # else:
    #     n10

    soma = 0 
    for pos, numero in enumerate(cpf):
        print(f'pos={pos}')

        mult = numero * (pos + 1)
        print(f'multiplicacao={mult}')
        soma = soma + mult
        print(f'soma={soma}\n-------\n')
    n10 = round(soma % 11)
    print(n10)

    if n10 < 3 or n10 > 9:
        n10 = 0

    cpf.append(n10)
        
    print(cpf)   
    #segundo digito n11

    # n11 = round(((n1 * 0) + (n2 * 1) + (n3 * 2) + (n4 * 3) + (n5 * 4) + (n6 * 5) + (n7 * 6) + (n8 * 7) + (n9 * 8) + (n10 * 9)) % 11)

    # if n11 < 3 or n11 > 9:
    #     n11 = 0
    # else:
    #     n11

    # # print(n11)

    # print(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11)

    soma = 0
    for pos, numero in enumerate(cpf):
        print(f'pos={pos}')

        mult = numero * pos
        print(f'multiplicacao={mult}')
        soma = soma + mult
        print(f'soma={soma}\n-------\n')
    n11 = round(soma % 11)
    print(n11)

    if n11 < 3 or n11 > 9:
        n11 = 0

    cpf.append(n11)
            
    print(cpf) 


gerar_cpf()
