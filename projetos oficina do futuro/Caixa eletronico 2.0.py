from IPython.display import clear_output
import time

versao = 2.0

menu = """
Opções do menu:
1 - Saldo
2 - Depósito
3 - Saque
4 - Transferência
5 - Pagar contas
6 - Recarga de celular
7 - Extrato
0 - Sair
"""

saldo = 500
log = ''

msg = f"|Bem-vindo ao caixa eletrônico v{versao} da oficinal do futuro|"
print(" " + "-" * (len(msg)-2) + "\n" + msg + "\n" + " " + "-" * (len(msg)-2))

while True:
  print(menu)

  op = int(input("O que você deseja fazer? "))

  if 0 <= op <= 6:
    if op == 1:
      print(f"Seu saldo atual é: R$ {saldo:.2f}")

    elif op == 2:
     while True:
        deposito = float(input("Qual o valor do depósito: "))
        if deposito > 0:
            saldo += deposito
            print("Depósito realizado com sucesso.")
            log = log+f'\nDeposito de {deposito}'
            break
        else:
            print('depósito inválido, tente novamente')

    elif op == 3:
     while True:
        saque = float(input("Qual o valor do saque: "))
        if saque <= saldo and saque >= 1:
            saldo -= saque
            print("Saque realizado com sucesso.")
            log = log+f'\nSaque de {saque}'
            break
        else:
            print('saque inválido')
          
    elif op == 4:
      op4 = input('digite para quem voce quer transferir')
      print('transferencia realizada')
      
    elif op == 5:
      conta1 = ['Internet','Energia','Água']
      print(f'''
      1 - {conta1[0]}
      2 - {conta1[1]}
      3 - {conta1[2]}
      ''')
      conta = int(input('Qual conta deseja pagar?'))
      valorconta = int(input('Qual o valor a ser pago?'))
      if  valorconta > saldo:
        print('Saldo indisponível, faça um depósito e tente novamente.')
      elif valorconta <= saldo:
        print(f'você acaba de pagar a conta de {conta1[conta-1]} no valor de {valorconta} reais')
        saldo -= valorconta
      else:
        print('operação inválida.')

    elif op == 6:

      print(f'''
      Escolha a operadora:
      1 - Oi
      2 - Tim
      3 - Vivo
      4 - Claro
      5 - Outro
      ''')
      oper = int(input('Qual operadora? '))
      if oper == 5:
        outro = (input('digite a outra operadora: '))
        outro == oper
      time.sleep(2), clear_output()

      print('''
      1 - 10 R$
      2 - 20 R$
      3 - 50 R$
      4 - Outro
      ''')
      recarga = int(input('escolha uma das opções'))

      time.sleep(2), clear_output()

      if recarga == 4:
        val_rec = float(input('digite o valor da recarga: '))
        val_rec == recarga
        print(f'Parabéns, você acaba de fazer uma recarga na operadora {outro} no valor de {recarga} R$ ')


      if recarga > saldo:
        print('Saldo indisponível, faça um depósito e tente novamente.')

      elif conta == 1 or conta == 2 or conta == 3:
        print('pagamento realizado com sucesso.')
      else:
        print('operação inválida.')


    else:
      print("Até logo.")
      break


  else:
    print("Função não disponível. Tente novamente.")

  time.sleep(3), clear_output()