def menu():
    return """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Cadastrar Cliente
    [n] Cadastrar Conta Corrente
    [q] Sair

    => """

def depositar(saldo, extrato, valor):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, extrato, valor, numero_saques, limite, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastrar_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    clientes[cpf] = {"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco}
    print("Cliente cadastrado com sucesso!")

def cadastrar_conta_corrente(contas, clientes):
    cpf = input("Informe o CPF do cliente: ")
    if cpf in clientes:
        numero_conta = len(contas) + 1
        contas[numero_conta] = {"cpf": cpf, "saldo": 0, "extrato": "", "numero_saques": 0}
        print("Conta corrente cadastrada com sucesso!")
    else:
        print("Cliente não encontrado. Cadastre o cliente primeiro.")

# Inicialização de variáveis
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
clientes = {}
contas = {}

# Loop principal
while True:
    opcao = input(menu())

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, extrato, valor)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(saldo, extrato, valor, numero_saques, limite, LIMITE_SAQUES)

    elif opcao == "e":
        exibir_extrato(saldo, extrato)

    elif opcao == "c":
        cadastrar_cliente(clientes)

    elif opcao == "n":
        cadastrar_conta_corrente(contas, clientes)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
