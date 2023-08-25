## FORMATAÇÃO DE STRING ##

'''
1- string formater que equivale a SYSTEM.OUT.PRINT.F(NO JAVA)
2- :.2f -> decide as casa decimais nesse caso são duas casas

'''
nome = 'levi'
altura = 1.82
peso = 97
imc = peso // altura ** 2 ## DIVISÃO INTEIRA

## SEM O FORMAT ##
print('seu nome e: ',nome,
       ', sua altura e: ',altura, 
       ', seu peso e: ', peso, 
       ',logo, seu IMC e: ', imc)

##COM O FORMAT##

formatado = f'seu nome e: {nome}, sua altura e: {altura:.2f}, seu peso e: {peso:.2f} logo seu IMC e: {imc:.3f}'

print(formatado)
