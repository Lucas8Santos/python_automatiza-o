'''
# Faça um programa que leia uma entrada de um número inteiro e devolva o seu resultado em fatorial
'''

numero = int(input('Escreva um numero: '))
if numero > 0 :
  fatorial = 1
  for item in range(1 ,numero +1 ):
    fatorial = fatorial * item

  print(fatorial)