import random
from IPython.display import clear_output
import time
def jogodavelha():
  Logo = ('''
    ----------------------------
          JOGO DA VELHA
    ----------------------------
    ''')
  velha = '''
    1  | 2 | 3
    ---|---|---
    4  | 5 | 6
    ---|---|---
    7  | 8 | 9
    '''
  Lista = ["1","2","3","4","5","6","7","8","9"]
  caracoroa=["X","O"]
  VencedorX=[]
  VencedorO=[]
  primeiro = random.choice(caracoroa)
  caracoroa.remove(primeiro)

  print(Logo)

  print('Como funciona?')
  print(velha)
  print('Cada numero é uma casa')
  print('Vamos lá!')
  print(f'"{primeiro}" vai começar! ')
  while Lista:
    while True:

      pos = input("Digite a posição: ")
      if pos in Lista:
        VencedorX.append(pos)
        velha = velha.replace(pos, primeiro)
        Lista.remove(pos)
        print(velha) 
        print(VencedorX)
        print(f'agora é a vez do "{caracoroa[0]}"')
      else:
        print("movimento inválido, tente novamente")
g

      while True:
        pos = input("Digite a posição: ")
        if pos in Lista:
          VencedorO.append(pos)
          velha = velha.replace(pos, caracoroa[0])
          Lista.remove(pos)
          print(velha)
          print(Lista)
          print(f'agora é a vez do "{primeiro}"')
          break
        else:
          print("movimento inválido, tente novamente")
        if Lista == []:
          break
jogodavelha()