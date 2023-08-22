##EXERCICIO##

print('QUAL SEU NOME')
nome_completo = input()
print('OLA '+nome_completo)

print('QUAL A SUA IDADE')
age = input()
idade = int(age)
if idade > 18 :
    print('SUA IDADE E:', idade ,', VAMOS CONTINUAR')
    print('QUAL SUA ALTURA?')
    altura = input()
    if altura >= 1.6 : 
        print('BOA ALTURA')
    elif altura >=1.8:
        print('TEMOS AQUI UM GIGANTE')
    else:
        print('TAMPINHA')
    
else:print('INFELIZMENTE NÃO PODEMOS CONTINUAR COM ESTA CONVERSA, SUA IDADE É ABAIXO DOS 18 ANOS')


