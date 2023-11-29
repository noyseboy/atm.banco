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
        # Método para permitir que um usuário faça login em sua conta
        numero_conta = input("Digite o número da sua conta: ")
        senha = input("Digite sua senha: ")

        for conta in self.contas:
            if conta['numero_conta'] == numero_conta and conta['senha'] == senha:
                self.menu_conta(conta)
                break
        else:
            print("Conta não encontrada. Verifique o número da conta e a senha.")

    def cadastrar_conta(self):
        # Método para permitir que um novo usuário cadastre uma nova conta
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu CPF: ")
        senha = input("Digite sua senha: ")

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
        # Método para gerar um número de conta aleatório
        return str(random.randint(100000, 999999))

    def menu_conta(self, conta):
        # Método para exibir o menu principal da conta e processar as escolhas do usuário
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
                print("Obrigado por usar nossos serviços. Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def verificar_saldo(self, conta):
        # Método para exibir o saldo atual da conta
        print(f"Seu saldo atual é: R${conta['saldo']:.2f}")

    def depositar(self, conta):
        # Método para permitir que o usuário deposite dinheiro em sua conta
        valor = float(input("Digite o valor a depositar: R$"))
        if valor > 0:
            conta['saldo'] += valor
            data_deposito = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            conta['historico'].append(f"Depósito de R${valor:.2f} em {data_deposito}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido.")

    def sacar(self, conta):
        # Método para permitir que o usuário saque dinheiro de sua conta
        valor = float(input("Digite o valor a sacar: R$"))
        if 0 < valor <= conta['saldo']:
            conta['saldo'] -= valor
            data_saque = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            conta['historico'].append(f"Saque de R${valor:.2f} em {data_saque}")
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def transferir(self, conta_origem):
        # Método para permitir que o usuário transfira dinheiro para outra conta
        numero_destino = input("Digite o número da conta de destino: ")
        valor = float(input("Digite o valor a transferir: R$"))

        for conta_destino in self.contas:
            if conta_destino['numero_conta'] == numero_destino:
                if 0 < valor <= conta_origem['saldo']:
                    conta_origem['saldo'] -= valor
                    conta_destino['saldo'] += valor
                    data_transferencia = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    
                    # Registro no histórico da conta de origem
                    nome_destino = conta_destino['nome']
                    conta_origem['historico'].append(f"Transferência de R${valor:.2f} para {nome_destino} ({conta_destino['numero_conta']}) em {data_transferencia}")
                    
                    # Registro no histórico da conta de destino
                    conta_destino['historico'].append(f"Transferência recebida de R${valor:.2f} de {conta_origem['nome']} ({conta_origem['numero_conta']}) em {data_transferencia}")
                    
                    print(f"Transferência de R${valor:.2f} para {nome_destino} realizada com sucesso.")
                else:
                    print("Saldo insuficiente ou valor inválido.")
                return

        print("Conta de destino não encontrada.")

    def imprimir_relatorio(self, conta):
        # Método para imprimir o relatório detalhado da conta, incluindo o histórico de transações
        print("\nRelatório da Conta:")
        print("Nome: {}".format(conta['nome']))
        print("Número da Conta: {}".format(conta['numero_conta']))
        print("CPF: {}".format(conta['cpf']))
        print("Saldo Atual: R${:.2f}".format(conta['saldo']))
        print("\nHistórico:")
        for registro in conta['historico']:
            print(registro)

    def executar(self):
        # Método para iniciar a execução do programa
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
    # Instanciar e executar o ATM
    atm = ATM()
    atm.executar()
