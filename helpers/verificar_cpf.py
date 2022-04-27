def validar_cpf(cpf): 
    
    cpf_vali = cpf[0:9]

    soma1 = 0 
    for pos, numero in enumerate(cpf_vali):
    
        mult = numero * (pos + 1)
        soma1 = soma1 + mult

        primeiro_digito = round(soma1 % 11)

    if primeiro_digito != cpf[9]:
        print("CPF INVÁLIDO")
                
    else:
        cpf_vali.append(primeiro_digito)
        
    soma2 = 0
    for pos, numero in enumerate(cpf_vali):

        mult = numero * pos
        soma2 = soma2 + mult
        segundo_digito = round(soma2 % 11)

    if segundo_digito != cpf[10]:
        print("CPF INVÁLIDO")
    else:
        cpf_vali.append(segundo_digito)
        print("CPF VÁLIDO")
