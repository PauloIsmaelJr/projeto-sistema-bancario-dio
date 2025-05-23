print("Bem-vindo ao PJ-Bank \nEscolha uma das opções no menu:")

menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> """

saldo = 0
limite = 500.00
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação não realizada! Favor informar um valor válido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação não realizada! Saldo insuficiênte.")

        elif excedeu_limite:
            print("Operação não realizada! O valor do saque excedeu o limite.")

        elif excedeu_saques:
            print("Operação não realizada! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação não realizada! O valor informado é inválido.")

    elif opcao == "e":
        print("\n====================EXTRATO====================")
        print()
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("===============================================")

    elif opcao == "q":
        print("Obrigado por utilizar nosso sistema!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada!")
