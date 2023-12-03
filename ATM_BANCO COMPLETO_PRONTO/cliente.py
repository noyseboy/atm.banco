class Cliente:
    def __init__(self, conta, administrador):
        self.conta = conta
        self.administrador = administrador

    def menu_conta(self):
        while True:
            print("\n" + "="*80)
            print(f"Bem-vindo, {self.conta.nome}!".center(80))
            print(f"Número da conta: {self.conta.numero_conta}".center(80))
            print("="*80)
            print("1. Verificar Saldo")
            print("2. Depositar")
            print("3. Sacar")
            print("4. Transferir")
            print("5. Sair")
            print("="*80)

            escolha = input("Escolha uma opção (1-5): ")

            if escolha == '1':
                self.verificar_saldo()
            elif escolha == '2':
                self.depositar()
            elif escolha == '3':
                self.sacar()
            elif escolha == '4':
                self.transferir()
            elif escolha == '5':
                print("Obrigado por usar nosso ATM. Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def verificar_saldo(self):
        print("\n" + "="*80)
        print("Verificar Saldo".center(80))
        print("="*80)
        print(f"Seu saldo atual é: R${self.conta.saldo:.2f}".center(80))

    def depositar(self):
        print("\n" + "="*80)
        print("Depositar".center(80))
        print("="*80)
        valor_str = input("Digite o valor a depositar: R$").strip()

        if not valor_str or not valor_str.isdigit():
            print("Por favor, insira um valor válido.")
            return

        valor = float(valor_str)

        if valor > 0:
            self.conta.saldo += valor
            print(f"\nDepósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("\nValor inválido.")

    def sacar(self):
        print("\n" + "="*80)
        print("Sacar".center(80))
        print("="*80)
        valor_str = input("Digite o valor a sacar: R$").strip()

        if not valor_str or not valor_str.isdigit():
            print("Por favor, insira um valor válido.")
            return

        valor = float(valor_str)

        if 0 < valor <= self.conta.saldo:
            self.conta.saldo -= valor
            print(f"\nSaque de R${valor:.2f} realizado com sucesso.")
        else:
            print("\nSaldo insuficiente ou valor inválido.")

    def transferir(self):
        print("\n" + "="*80)
        print("Transferir".center(80))
        print("="*80)
        numero_destino = input("Digite o número da conta de destino: ").strip()

        # Check if the destination account exists
        conta_destino = self.encontrar_conta(numero_destino)

        # Check if the destination account is not the same as the source account
        if conta_destino and conta_destino.numero_conta != self.conta.numero_conta:
            print(f"Destinatário: {conta_destino.nome}")
            valor_str = input("Digite o valor a transferir: R$").strip()

            if not valor_str or not valor_str.isdigit():
                print("Por favor, insira um valor válido.")
                return

            valor = float(valor_str)

            if 0 < valor <= self.conta.saldo:
                self.conta.saldo -= valor
                conta_destino.saldo += valor
                print(f"\nTransferência de R${valor:.2f} para {conta_destino.nome} realizada com sucesso.")
            else:
                print("\nSaldo insuficiente ou valor inválido.")
        elif conta_destino:
            print("\nVocê não pode transferir dinheiro para a mesma conta.")
        else:
            print("\nConta de destino não encontrada.")

    def encontrar_conta(self, numero_conta):
        for conta in self.administrador.contas:
            if conta.numero_conta == numero_conta:
                return conta
        return None