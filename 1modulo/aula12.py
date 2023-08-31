## INPUT ##

#QUANDO O USUÁRIO DIGITAR O NOME, A INFORMAÇÃO VAI PARA A VARIÁVEL NO TIPO STR
# nome = input('Digite o seu : ')
# print(f'Olá, {nome}')


nome_completo = input('QUAL O SEU NOME?: ')                       
print('OLA ', nome_completo)

idade = int(input('QUAL A SUA IDADE?: '))


if idade > 18 :
    print(f'SUA IDADE E: {idade}, VAMOS CONTINUAR')


    altura = float(input('QUAL A SUA ALTURA?: '))
    if altura > 1.60 and altura <= 1.70 : 
        print('BOA ALTURA')
    elif altura >=1.80:
        print('TEMOS AQUI UM GIGANTE')
    else:
        print('TAMPINHA')
    
else:print('INFELIZMENTE NÃO PODEMOS CONTINUAR COM ESTA CONVERSA,SUA IDADE É ABAIXO DOS 18 ANOS')
