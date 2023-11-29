import random
from datetime import datetime

class ATM:
    def __init__(self):
        self.contas = []

    def exibir_menu(self):
        print("\nBem-vindo!")
        print("1. Login")
        print("2. Cadastrar Conta")
        print("3. Sair")

    def login(self):
        numero_conta = input("Digite o número da sua conta: ").strip()
        senha = input("Digite sua senha: ").strip()

        if not numero_conta or not senha or not numero_conta.isdigit():
            print("Por favor, preencha todos os campos com números.")
            return

        for conta in self.contas:
            if conta['numero_conta'] == numero_conta and conta['senha'] == senha:
                self.menu_conta(conta)
                break
        else:
            print("Conta não encontrada. Verifique o número da conta e a senha.")

    def cadastrar_conta(self):
        nome = input("Digite seu nome: ").strip()
        cpf = input("Digite seu CPF: ").strip()
        senha = input("Digite sua senha: ").strip()

        if not nome or not cpf or not senha or not cpf.isdigit():
            print("Por favor, preencha todos os campos corretamente.")
            return

        for conta in self.contas:
            if conta['cpf'] == cpf:
                print("Já existe uma conta registrada com este CPF.")
                return

        numero_conta = self.gerar_numero_conta()
        nova_conta = {'nome': nome, 'cpf': cpf, 'numero_conta': numero_conta, 'saldo': 0.0, 'senha': senha, 'historico': []}
        self.contas.append(nova_conta)
        print("Conta cadastrada com sucesso!")
        print(f"Seu número de conta é: {numero_conta}")

        self.menu_conta(nova_conta)

    def gerar_numero_conta(self):
        return str(random.randint(100000, 999999))

    def menu_conta(self, conta):
        while True:
            print("\nBem-vindo, {}!".format(conta['nome']))
            print("Número da conta:", conta['numero_conta'])
            print("1. Verificar Saldo")
            print("2. Depositar")
            print("3. Sacar")
            print("4. Transferir")
            print("5. Imprimir Relatório da Conta")
            print("6. Sair")
            
            escolha = input("Escolha uma opção (1-6): ")

            if escolha == '1':
                self.verificar_saldo(conta)
            elif escolha == '2':
                self.depositar(conta)
            elif escolha == '3':
                self.sacar(conta)
            elif escolha == '4':
                self.transferir(conta)
            elif escolha == '5':
                self.imprimir_relatorio(conta)
            elif escolha == '6':
                print("Obrigado por usar nosso ATM. Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def verificar_saldo(self, conta):
        print(f"Seu saldo atual é: R${conta['saldo']:.2f}")

    def depositar(self, conta):
        valor_str = input("Digite o valor a depositar: R$").strip()

        if not valor_str or not valor_str.isdigit():
            print("Por favor, insira um valor válido.")
            return

        valor = float(valor_str)

        if valor > 0:
            conta['saldo'] += valor
            data_deposito = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            conta['historico'].append(f"Depósito de R${valor:.2f} em {data_deposito}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido.")

    def sacar(self, conta):
        valor_str = input("Digite o valor a sacar: R$").strip()

        if not valor_str or not valor_str.isdigit():
            print("Por favor, insira um valor válido.")
            return

        valor = float(valor_str)

        if 0 < valor <= conta['saldo']:
            conta['saldo'] -= valor
            data_saque = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            conta['historico'].append(f"Saque de R${valor:.2f} em {data_saque}")
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def transferir(self, conta_origem):
        numero_destino = input("Digite o número da conta de destino: ").strip()
        valor_str = input("Digite o valor a transferir: R$").strip()

        if not numero_destino or not valor_str or not valor_str.isdigit():
            print("Por favor, preencha todos os campos corretamente.")
            return

        valor = float(valor_str)

        for conta_destino in self.contas:
            if conta_destino['numero_conta'] == numero_destino:
                if 0 < valor <= conta_origem['saldo']:
                    conta_origem['saldo'] -= valor
                    conta_destino['saldo'] += valor
                    data_transferencia = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    nome_destino = conta_destino['nome']
                    conta_origem['historico'].append(f"Transferência de R${valor:.2f} para {nome_destino} ({conta_destino['numero_conta']}) em {data_transferencia}")
                    conta_destino['historico'].append(f"Transferência recebida de R${valor:.2f} de {conta_origem['nome']} ({conta_origem['numero_conta']}) em {data_transferencia}")

                    print(f"Transferência de R${valor:.2f} para {nome_destino} realizada com sucesso.")
                else:
                    print("Saldo insuficiente ou valor inválido.")
                return

        print("Conta de destino não encontrada.")

    def imprimir_relatorio(self, conta):
        print("\nRelatório da Conta:")
        print("Nome: {}".format(conta['nome']))
        print("Número da Conta: {}".format(conta['numero_conta']))
        print("CPF: {}".format(conta['cpf']))
        print("Saldo Atual: R${:.2f}".format(conta['saldo']))
        print("\nHistórico:")
        for registro in conta['historico']:
            print(registro)

    def executar(self):
        while True:
            self.exibir_menu()
            escolha = input("Escolha uma opção (1-3): ")

            if escolha == '1':
                self.login()
            elif escolha == '2':
                self.cadastrar_conta()
            elif escolha == '3':
                print("Obrigado por usar nossos serviços. Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    atm = ATM()
    atm.executar()
