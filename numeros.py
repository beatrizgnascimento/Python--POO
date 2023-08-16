#deve-se converter números em strings para concatear, não é permitido juntar números e strings
dias_fev = 28
print(str(dias_fev) + 'dias em Fevereiro')

#a funcao input sempre retorna strings
num1 = input('Digite o primeiro numero: ') #5
num2 = input('Digite o segundo numero: ') #6
print(num1 + num2) #56

#para realizar operações
num1 = input('Digite o primeiro número: ') #5
num2 = input('Digite o segundo número: ') #6
print(int(num1) + int(num2)) #11
print(float(num1) + float(num2)) #11.0

#função para gerar numero randomico
import random #importando pacote
print(random.randrange(1, 10))
