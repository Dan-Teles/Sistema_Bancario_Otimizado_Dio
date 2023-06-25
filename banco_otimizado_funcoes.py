    # Desafio Sistema Bancario Otimizado DIO
    # Daniel Teles da Silva
import os
#import textwrap
#return input(textwrap.dedent(op))

# parametro(cpf,[nome,data_nascimento,endereco])
# parametro.addend

def menu():
    op = """
      [d]\tDepositar
      [s]\tSacar
      [e]\tExtrato
      [cc]\tCriar Conta
      [lc]\tListar Conta
      [cu]\tCadastrar Usuário
      [lu]\tListar Usuário
      [q]\tSair

      => """
    opcao = input(op)
    return opcao       
#cadastrar novo usuario se nao existir outro igual  
def cadastrar_usuario(usuarios):
    cpf = int(input("CPF: "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
      print("CPF JA CADASTRADO!")
      os.system("pause")
      return
    else:
      nome = input("Nome completo: ")
      data_nascimento = input("Data de nascimento: dd/mm/aaaa: ")
      endereco = input("Endereço: ")

      usuarios.append({"nome": nome, "data_nascimento": data_nascimento,"cpf": cpf,"endereco": endereco})
      print("Usuario cadastrado com sucesso!")
      os.system("pause")
#retorna usuario existente ou vazio
def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
#criar conta por cpf
def criar_conta(agencia, numero_conta, usuarios):
    cpf = int(input("Informe CPF do usuário: "))
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
      print("Conta criada com sucesso!")
      #retornar dados
      return {"agencia": agencia, "numero_conta": numero_conta,"usuario": usuario}
    
    print("Usuário não encontrado! Conta não criada!")
#listar cliente
def listar_cliente(usuarios):
   for usuario in usuarios:
      printar = f"""
        Nome: \t{usuario["nome"]}
        CPF: \t{usuario["cpf"]}
        Data de Nascimento: \t{usuario["data_nascimento"]}
        Endereço: \t{usuario["endereco"]}
      """
      print(printar)
      os.system("pause")
#listar conta
def listar_conta(contas):
    # percorrer pelo VETOR (n_deposito)
    for conta in contas:
      printar = f"""
          Agência: \t{conta["agencia"]}
          Numero Conta: \t{conta["numero_conta"]}
          Titular: \t{conta["usuario"]["nome"]}
      """
      print(printar)
      os.system("pause")
# saque por kwd
def sacar(*, saldo,extrato, limite, numero_saques):
    valor = float(input("Digite o valor do saque: "))
  # se saque disponivel
    if saldo > valor and numero_saques < 3:
        while(valor > limite):
            valor = float(input("Digite o valor do saque menor que 500: "))
        saldo -= valor
        extrato += f"Saque:\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
  # se n° saque atingiu limite
    elif numero_saques == 3:
        print("Limite de saque diários alcançado!")
        os.system("pause")
  # se saque > saldo
    else:
        print("Não será possível sacar por falta de saldo!")
        os.system("pause")
    return saldo,extrato
#depositar apenas por posição
def depositar(saldo,extrato, /):
    valor = float(input("Digite o valor a depositar: "))
    while valor <= 0:
      valor = float(input("Digite o valor a depositar maior que 0: "))
    saldo += valor
    extrato += f"Deposito:\tR$ {valor:.2f}\n"
    print("Deposito Realizado com sucesso!")
    os.system("pause")
    return saldo,extrato
#percorrer pelo vetor para mostrar
def imprimir_extrato (saldo,/,*,extrato):
    #se existe extrato
    print("Nao foram realizadas mais transações!\n" if not extrato else extrato)
    print(f"Saldo:\tR$ {saldo:.2f}")
    os.system("pause")
#Iniciar atributos e chamar metodos 
def main():
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    numero_saques = 0
    usuarios = []
    contas = []
    extrato = ""
  
    while True:
      opcao = menu()
      os.system("cls")
    #Depositar = saldo + extrato
      if opcao == 'd':
        print("Depósito")
        saldo,extrato = depositar(saldo,extrato)  
    #Sacar = tudo menos valor 
      elif opcao == 's':
        print("Saque")
        saldo,extrato = sacar(
          saldo = saldo,
          extrato = extrato,
          numero_saques= numero_saques,
          limite = limite
        )
    #Imprimir_extrato = saldo + extrato 
      elif opcao == 'e':
        print("Extrato")
        imprimir_extrato(saldo,extrato=extrato)
    #Cadastrar_usuario = usuarios
      elif opcao == 'cu':
        print("Cadastrar Usuario")
        cadastrar_usuario(usuarios)
    #Criar_conta = mandar tudo menos valor  
      elif opcao == 'cc':
        print("Criar Conta Corrente")
        #acrescentar +1 conta
        numero_conta = len(contas) + 1
        new_conta = criar_conta(AGENCIA,numero_conta,usuarios)
        if new_conta:
          contas.append(new_conta)
    #Listar_Usuario = apenas usuarios
      elif opcao == 'lu':
         listar_cliente(usuarios)
    #Lista Conta = apenas contas
      elif opcao == 'lc':
        listar_conta(contas)
    #Sair = termina o laço
      elif opcao == 'q':
        break
    #Operação Invalida
      else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")    

#chamar main
main()
