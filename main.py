import os

menu = '''
DIGITAL INNOVATION BANK

1 - Depositar
2 - Sacar
3 - Extrato
4 - Sair

Escolha uma das opções: 
'''

saldo = 0.00
extrato = "======EXTRATO======\n"
LIMITE_SAQUE = 500
QUANTIDADE_SAQUES = 3
conta_saque = 0

while (True):
  opcao = int(input(menu))

  if (opcao == 1):
    os.system('clear') or None
    deposito = float (input ("Digite o valor a ser depositado: "))
    
    if (deposito > 0): 
      saldo += deposito
      extrato += f"+ R$ {deposito:.2f}\n"
      os.system('clear') or None
      print (f"Depósito de R$ {deposito:.2f} realizado com sucesso!")   
      
    else:
      print ("Valor inválido!")  
      
  elif (opcao == 2):
    os.system('clear') or None
    saque = float (input ("Digite o valor a ser sacado: "))

    saldo_insuficiente = (saque > saldo)
    quantidade_excedida = (conta_saque == QUANTIDADE_SAQUES)
    limite_excedido = (saque > LIMITE_SAQUE)

    if (saque < 0):
      print ("Valor inválido")
    
    elif (quantidade_excedida):
      print (f"Operação falhou! Você já sacou {QUANTIDADE_SAQUES} vezes hoje. Tente novamente amanhã")

    elif (limite_excedido):
      print (f"Operação falhou! Valor máximo para saque: R$ {LIMITE_SAQUE:.2f}")

    elif (saldo_insuficiente):
      print ("Operação falhou! Seu saldo é insuficiente.")

    else:
      saldo -= saque
      extrato += f"- R$ {saque:.2f}\n"
      conta_saque += 1
      os.system('clear') or None
      print (f"Saque de R$ {saque:.2f} realizado com sucesso!")
      
  elif (opcao == 3):
    os.system('clear') or None
    print(extrato + f"\nSaldo: R$ {saldo:.2f}")  
    print(19 * "=")
    
  elif (opcao == 4):
    os.system('clear') or None
    print ("Operação encerrada.\nVolte sempre!")
    break
    
  else:
    os.system('clear') or None
    print ("Opção inválida! Tente novamente.")
    