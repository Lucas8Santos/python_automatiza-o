'''
Escreva um programa que, ao iniciar gere um valor  aleatorio  de 1 a 10 e permite que o usuário   chute um 
número até que o valor aleatório  gerado no início do programa seja chutado corretamente
'''

import random

valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
  chute = int(input('chute um valor de 1 a 10: '))
  if chute > valor_aleatorio:
    print ('valor aleatorio foi maior que valor gerado ')
  elif chute < valor_aleatorio:
    print('chute foi menor que gerar valor gerado')
  elif chute == valor_aleatorio:
    acertou = True
    print('acertou')
