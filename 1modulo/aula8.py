##EXERCICIO##


nome_completo = input('QUAL O SEU NOME?: ')
print('OLA '+nome_completo)

idade = (input('QUAL A SUA IDADE?: '))


if idade > 18 :
    print(f'SUA IDADE E: {idade}, VAMOS CONTINUAR')
    print('QUAL SUA ALTURA?')
    altura = input()
    if altura >= 1.6 : 
        print('BOA ALTURA')
    elif altura >=1.8:
        print('TEMOS AQUI UM GIGANTE')
    else:
        print('TAMPINHA')
    
else:print('INFELIZMENTE NÃO PODEMOS CONTINUAR COM ESTA CONVERSA, SUA IDADE É ABAIXO DOS 18 ANOS')


