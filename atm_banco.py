import random

class Conta:
    def __init__(self, nome, cpf, numero_conta, senha, saldo=0.0):
        self.nome = nome
        self.cpf = cpf
        self.numero_conta = numero_conta
        self.senha = senha
        self.saldo = saldo

class Administrador:
    def __init__(self):
        self.nome_usuario = ""
        self.senha = ""
        self.contas = []

    def criar_usuario_senha(self):
        print("="*30)
        print("Criar Usuário e Senha do Administrador")
        print("="*30)
        while True:
            self.nome_usuario = input("Digite o nome de usuário para o administrador: ").strip()
            if self.nome_usuario:
                break
            else:
                print("Nome de usuário não pode ficar vazio. Tente novamente.")

        while True:
            self.senha = input("Digite a senha para o administrador: ").strip()
            if self.senha:
                break
            else:
                print("Senha não pode ficar vazia. Tente novamente.")

        print("\nUsuário e senha do administrador criados com sucesso.")

    def autenticar_admin(self):
        print("\n" + "="*30)
        print("Bem-vindo ao Sistema Bancário!")
        print("="*30)
        nome_usuario = input("Digite o nome de usuário: ").strip()
        senha = input("Digite a senha: ").strip()

        return nome_usuario == self.nome_usuario and senha == self.senha

    def criar_conta(self):
        print("\n" + "="*30)
        print("Criar Nova Conta")
        print("="*30)
        while True:
            nome = input("Digite o nome do cliente: ").strip()
            if nome and nome.replace(" ", "").isalpha():
                break
            else:
                print("Nome não pode ficar vazio e deve conter apenas letras e espaços. Tente novamente.")

        while True:
            cpf = input("Digite o CPF do cliente (11 números): ").strip()
            if cpf and cpf.isdigit() and len(cpf) == 11:
                break
            else:
                print("CPF não pode ficar vazio, deve conter apenas números, e ter 11 caracteres. Tente novamente.")

        for conta in self.contas:
            if conta.cpf == cpf:
                print("Já existe uma conta registrada com este CPF.")
                return

        numero_conta = self.gerar_numero_conta()
        while True:
            senha = input("Digite a senha para a conta: ").strip()
            if senha:
                break
            else:
                print("Senha não pode ficar vazia. Tente novamente.")

        nova_conta = Conta(nome, cpf, numero_conta, senha)
        self.contas.append(nova_conta)
        print("\nConta criada com sucesso!")
        print(f"O número da conta para {nome} é: {numero_conta}")

    def gerar_numero_conta(self):
        return str(random.randint(100000, 999999))

class Cliente:
    def __init__(self, conta, administrador):
        self.conta = conta
        self.administrador = administrador

    def menu_conta(self):
        while True:
            print("\n" + "="*30)
            print(f"Bem-vindo, {self.conta.nome}!")
            print("Número da conta:", self.conta.numero_conta)
            print("="*30)
            print("1. Verificar Saldo")
            print("2. Depositar")
            print("3. Sacar")
            print("4. Transferir")
            print("5. Sair")
            print("="*30)

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
        print("\n" + "="*30)
        print("Verificar Saldo")
        print("="*30)
        print(f"Seu saldo atual é: R${self.conta.saldo:.2f}")

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

    def transferir(self):
        print("\n" + "="*30)
        print("Transferir")
        print("="*30)
        numero_destino = input("Digite o número da conta de destino: ").strip()
        valor_str = input("Digite o valor a transferir: R$").strip()

        if not numero_destino or not valor_str or not valor_str.isdigit():
            print("Por favor, preencha todos os campos corretamente.")
            return

        valor = float(valor_str)

        for conta_destino in self.administrador.contas:
            if conta_destino.numero_conta == numero_destino:
                if 0 < valor <= self.conta.saldo:
                    self.conta.saldo -= valor
                    conta_destino.saldo += valor
                    print(f"\nTransferência de R${valor:.2f} para {conta_destino.nome} realizada com sucesso.")
                else:
                    print("\nSaldo insuficiente ou valor inválido.")
                return

        print("\nConta de destino não encontrada.")

administrador_principal = Administrador()

# Criar usuário e senha para o administrador antes de iniciar o programa
administrador_principal.criar_usuario_senha()

while True:
    print("\n" + "="*30)
    print("Bem-vindo ao Sistema Bancário!")
    print("="*30)
    print("1. Administrador")
    print("2. Cliente")
    print("3. Sair")

    escolha_inicial = input("Escolha uma opção (1-3): ")

    if escolha_inicial == '1':
        if administrador_principal.autenticar_admin():
            while True:
                print("\n" + "="*30)
                print("Bem-vindo, Administrador!")
                print("1. Criar Conta")
                print("2. Voltar para o Menu Inicial")
                print("="*30)

                escolha_admin = input("Escolha uma opção (1-2): ")

                if escolha_admin == '1':
                    administrador_principal.criar_conta()
                elif escolha_admin == '2':
                    print("\nEncerrando sessão de administrador.")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        else:
            print("\nAutenticação de administrador falhou. Tente novamente.")

    elif escolha_inicial == '2':
        if administrador_principal.contas:
            numero_conta_cliente = input("\nDigite o número da sua conta: ").strip()
            senha_cliente = input("Digite sua senha: ").strip()

            for conta_cliente in administrador_principal.contas:
                if conta_cliente.numero_conta == numero_conta_cliente and conta_cliente.senha == senha_cliente:
                    cliente = Cliente(conta_cliente, administrador_principal)
                    cliente.menu_conta()
                    break
            else:
                print("\nConta não encontrada. Verifique o número da conta e a senha.")
        else:
            print("\nNenhuma conta cadastrada. Encerrando o programa.")

    elif escolha_inicial == '3':
        print("\nEncerrando o Sistema Bancário. Até logo!")
        break

    else:
        print("\nOpção inválida. Tente novamente.")
