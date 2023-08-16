#strings podem ser armazenadas em variáveis
nome = 'Pedro'
print(nome)

#concatear strings
nome = 'Pedro'
sobrenome = 'Souza'
print(nome + sobrenome)
print('Olá' + ' ' + nome + ' ' + sobrenome)

#funções para modificar strings
frase = 'frase a ser modificada'
print(frase.upper())
print(frase.lower())
print(frase.captalize())
print(frase.count('o'))

#funções que auxiliam na formatação de strings
nome = input('Qual seu nome?')
sobrenome = input('Qual seu sobrenome?')
print('Olá' + nome.captalize() + ' ' + sobrenome.captalize())

#verificação de substring
#uso do operador in para verificar uma substring
txt = 'Eu moro em araraquara'
x = 'arara' in txt
print(x)
#retorna true

