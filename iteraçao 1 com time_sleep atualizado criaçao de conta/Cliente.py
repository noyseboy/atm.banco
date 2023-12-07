import time
class Cliente:
    def __init__(self, conta):
        self.conta = conta

    def menu_conta(self):
        while True:
            print("="*30)
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
                print("\nObrigado por usar nossos serviços. Até logo!")
                time.sleep(1)
                break
            else:
                print("\nOpção inválida. Tente novamente.")
                time.sleep(2)

    def depositar(self):
        print("="*30)
        print("Depositar")
        print("="*30)
        valor_str = input("\nDigite o valor a depositar: R$").strip()

        if not valor_str or not valor_str.isdigit():
            print("\nPor favor, insira um valor válido.")
            time.sleep(2)
            return

        valor = float(valor_str)

        if valor > 0:
            self.conta.saldo += valor
            print(f"\nDepósito de R${valor:.2f} realizado com sucesso.")
            time.sleep(2)
        else:
            print("\nValor inválido.")
            time.sleep(2)

    def sacar(self):
        print("="*30)
        print("Sacar")
        print("="*30)
        valor_str = input("\nDigite o valor a sacar: R$").strip()

        if not valor_str or not valor_str.isdigit():
            print("\nPor favor, insira um valor válido.")
            time.sleep(2)
            return

        valor = float(valor_str)

        if 0 < valor <= self.conta.saldo:
            self.conta.saldo -= valor
            print(f"\nSaque de R${valor:.2f} realizado com sucesso.")
            time.sleep(2)
        else:
            print("\nSaldo insuficiente ou valor inválido.")
            time.sleep(2)