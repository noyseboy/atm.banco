class Cliente:
    def __init__(self, conta):
        self.conta = conta

    def menu_conta(self):
        while True:
            print("\n" + "="*30)
            print(f"Bem-vindo, {self.conta.nome}!")
            print("Número da conta:", self.conta.numero_conta)
            print("="*30)
            print("1. Depositar")
            print("2. Sacar")
            print("3. Sair")
            print("="*30)
            
            escolha = input("Escolha uma opção (1-3): ")

            if escolha == '1':
                self.depositar()
            elif escolha == '2':
                self.sacar()
            elif escolha == '3':
                print("Obrigado por usar nosso ATM. Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def depositar(self):
        print("\n" + "="*30)
        print("Depositar")
        print("="*30)
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
        print("\n" + "="*30)
        print("Sacar")
        print("="*30)
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