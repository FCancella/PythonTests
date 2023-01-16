namelist = []
namelist.append('Nome: Felipe Cancella; Idade: 17; Apelido: Cancella')
nome = input("   Ola! Qual é o seu nome?: ")


if (nome.upper() == "FELIPE" or nome.upper() == 'CANCELLA'):
    print ('   Entao quer dizer que voce esta por aqui Cancella?')
    print ('   Seja bem vindo de volta!')
    resposta = input ('   Deseja ver sua ficha, Cancella?: ')
    if (resposta.upper() == "SIM"):
        print (namelist[0])
    else:
        print ('   Tudo bem. Ate a proxima!')
else:
    nome2 = input ('   É um prazer te conhecer {}, como devo te chamar exatamente?: '.format (nome))
    print ("   Seja bem vindo {}".format (nome2))
    respostaficha = input ('   Deseja criar sua ficha?:')
    if (respostaficha.upper() == "SIM"):
        namelist.append('   Nome: {}; Idade: {}; Apelido: {}'.format (nome, input ('   Quantos anos voce tem?: '), nome2))
        resposta = input ('   Informacoes preenchidas! deseja ver sua ficha?: ')
        if (resposta.upper() == "SIM"):
            print(namelist[1])
        else:
            print ('   Tudo bem. Ate a proxima!')
    else:
        print ('   Tudo bem. Ate a proxima!')


#Nova = input ("Você deseja adicionar mais alguem à lista?: ")

#if (Nova.upper () == "SIM" or Nova.upper() == "S"):
    #nome3 = input("   Perfeito! Qual é o seu nome?: ")
    #if (nome3 == nome or name2):
        #print ("Nome já cadastrado. Até a proxima ")
    #else:
        #nome4 = input ('   É um prazer te conhecer {}, como devo te chamar exatamente?: '.format (nome3))
        #namelist.append('   Nome: {}; Idade: {}; Apelido: {}'.format (nome3, input ('   Quantos anos voce tem?: '), nome4))
        #resposta = input ('   Informacoes preenchidas! deseja ver sua ficha?: ')
        #if (resposta.upper() == "SIM"):
            #print(namelist[-1])
        #else:
            #print ('   Tudo bem. Ate a proxima!')
#else:
    #print ('   Tudo bem. Ate a proxima!')
