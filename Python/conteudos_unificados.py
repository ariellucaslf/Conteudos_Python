#Primeiro Programa
'''nome = str(input('Digite seu nome:'))
print(f'Boa vindas {nome} !')
print(type(nome))

#Segundo Programa

numero1 = int(input('digite um numero:'))
numero2 = int(input('digite outro numero:'))
soma = numero1 + numero2

print(f'A soma dos numeros digitados é igual a: {soma}')
print(type(numero1))
'''
#Exercicio

'''
n1 = int(input('digite o ano do seu nascimento:'))
idade = 2024 - n1

print(f'Você tem {idade} de idade.')
'''

#Exercicio 02

'''
n1 = int(input('digite um numero: '))
dobro = n1 * 2

print(f'O dobro do numero {n1} é igual a: {dobro}')
'''

#Exercicio 03
'''
# dolar pra real
v1 = float(input('digite o valor em dolár $ ')) 
conversao = v1 / 5.5

print(f'O valor de $ {v1} em real é igual a: R$ {conversao}')

# real pra dolar
v2 = float(input('digite o valor em real R$ '))
conversao1 = v2 * 5.5

print(f'O valor de R$ {v2} em dolar é igual a: $ {conversao1}')
'''

# Condicionais 
'''
# Media

n1 = float(input("digite um numero qualquer:"))
n2 = float(input("digite outro numero qualquer:"))
n3 = float(input("digite um ultimo numero qualquer:"))
r = ( n1 + n2 + n3 ) / 3 

print(f"sua média é igual a: {r}")

if r >= 70:
  print("aprovado")
else:
  print ("reprovado")
'''

# Verificar idade

'''
ano = int(input('Digite o ano de Nascimento: '))
idade = 2024 - ano

if idade >= 18:
  print(f'Sua idade é {idade}, e você vai ser preso em breve !')
else:
  print(f'Sua idade é {idade}, e por enquanto você ta na paz.')
'''

# Condição para testar num pares e impares

'''
b = int(input("insira um numero qualquer:"))

if (b%2) == 0:
  print(f"O numero {b} é Par")
else:
  print(f"O numero {b} é Impar")
'''

#Exercicio media 

'''
n1 = float(input("Digite a sua primeira nota: "))
n2 = float(input("Digite a sua segunda nota: "))
nota_final = (n1 + n2) / 2

if nota_final >= 7:
    print("Parábens ! Você está aprovado.")
elif nota_final <= 6.9 and nota_final >= 4:
    print("Você está na final. Estude !")
else:
    print("Você está reprovado !")
'''

#Verificar se o numero é divisivel por numeros especificos

'''
num = int(input("Digite um numero um numero inteiro: "))


if num % 9 == 0:
    print(f"O numero {num} é divisivel por 2.")
elif num % 3 == 0 and num % 2 == 0:
    print(f"O numero {num} é divisivel por 3 e por 2.")
elif num % 5 == 0:
    print(f"O numero {num} é divisivel por 5.")
elif num % 6 == 0:
    print(f"O numero {num} é divisivel por 6.")
elif num % 7 == 0:
    print(f"O mumero {num} é divisivel por 7.")
else:
    print(f"O numero {num} não é um numero divisivel por 2, 3, 5, 6 e 7.")
'''

# Verificar dia da semana com numero
'''
dia = int(input("Digite um numero do 1 ao 7: "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda-feira")
elif dia == 3:
    print("Terça-feira")
elif dia == 4:
    print("Quarta-feira")
elif dia == 5:
    print("Quinta-feira")
elif dia == 6:
    print("Sexta-feira")
elif dia == 7:
    print("Sabádo")
else:
    print("Número não reconhecido.")
'''

# Condição de verificar se o num é positivo, negativo ou igual a zero.


'''
n1 = float(input("Digite um numero: "))

if n1 > 0:
    print(f"O numero {n1} é postivo.")
elif n1 < 0:
    print(f"O numero {n1} é negativo.")
else:
    print(f"O numero {n1} é igual a zero. ")
'''


# Calculo IMC

'''
peso = float(input("digite o seu o peso em Kg: "))
altura = float(input("digite a sua altura em metros: "))
imc = peso / ( altura * altura)

if imc <= 18.49:
  print("Abaixo do peso.")
elif imc >= 18.5 or imc <= 24.99:
  print("Peso normal.")
elif imc >= 25 or imc <= 29.99:
  print("Acima do peso.")
elif imc >= 30 or imc <= 34.99:
  print("Obesidade I.")
elif imc >= 35 or imc <= 39.99:
  print("Obesidade II.")


# Operadores logicos: and, or e not
  
# Match / case
  
dia = int(input("digite um numero do 1 ao 7: "))

match dia:
  case 1:
    print("Hoje é Domingo.")
  case 2:
    print('Hoje é Segunda.')
  case 3:
    print('Hoje é Terça.')
  case 4:
    print('Hoje é Quarta.')
  case 5:
    print('Hoje é Quinta.')
  case 6:
    print('Hoje é Sexta.')
  case 7:
    print('Hoje é Sábado.')
  case _:
    print("Numero sem dia correspondente.")
'''

#Laços de repetição (while)
#Multiplacação

'''
numero = int(input('digite um numero inteiro: '))
if numero > 0:
    print(f'A tabuada de multiplicação do {numero} é \n')
    controle = 1
    while controle <= 10:
        multiplicacao = controle * numero 
        print(f'{numero} x {controle} = {multiplicacao}')
        controle += 1
    print('Fim do laço. \nFim do programa.') 
'''

# Exercicio   
# Papagaio

'''
print('digite uma frase: \n')
sentinela = ''
while sentinela != 'sair': # laço de repetição 
  sentinela = input('digite uma frase: \n').lower() # caixa baixa
  if sentinela != 'sair': # condicional
    print(sentinela, '\n')
print('Agradeço a participação na brincadeira.')
'''

#verificação de numeros impares e pares

'''

numero1 = int(input('digite um numero: '))

while (numero1 % 2 == 0 or numero1 % 2 != 0 ) and numero1 != 0:
    if numero1 % 2 == 0:
        print(f'o {numero1} é par.\n')
    else:
        print(f'o {numero1} é impar.\n')
    numero1 = int(input('digite um numero: '))
print(f'voce digitou o numero {numero1}. \nEstou encerrando o programa...')
'''

# repetir o numero regressivamente 
 
'''
numero = int(input("digite um numero: "))

if numero > 0:
  while numero >= 0:
    print(numero)
    numero -= 1 # contador de variavel  
print('fim do programa')
'''
#Laços de repetição (for)


#Listas em python 
#command remove(), append()

'''
coleguinha = [] #lista vazia

for i in range(6):
    nome_coleguinha = input('Digite o nome do coleguinha:')
    coleguinha.append(nome_coleguinha) #adiciona itens a lista


for c in coleguinha:
    print(f'{c} você está convidado para meu passeio no Rio Paraiba. \n')
'''
