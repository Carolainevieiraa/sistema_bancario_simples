menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")

def sacar(valor):
    global saldo, numero_saques
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
        return

    if numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
        return

    if valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
        return

    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        return

    saldo -= valor
    numero_saques += 1
    extrato.append(f"Saque: R$ {valor:.2f}")
    print("Saque realizado com sucesso.")

def mostrar_extrato():
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for lancamento in extrato:
            print(lancamento)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: "))
            depositar(valor)
        except ValueError:
            print("Por favor, digite um valor numérico válido.")

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: "))
            sacar(valor)
        except ValueError:
            print("Por favor, digite um valor numérico válido.")

    elif opcao == "e":
        mostrar_extrato()

    elif opcao == "q":
        print("Obrigado por usar nosso sistema bancário!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
