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
        print("="*80)
        print("".center(80, "="))
        print("Criar Usuário e Senha do Administrador".center(80))
        print("".center(80, "="))
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
        print("\n" + "="*80)
        print("".center(80, "="))
        print("Bem-vindo ao ATM BANCO!".center(80))
        print("".center(80, "="))
        nome_usuario = input("Digite o nome de usuário: ").strip()
        senha = input("Digite a senha: ").strip()

        return nome_usuario == self.nome_usuario and senha == self.senha

    def criar_conta(self):
        print("\n" + "="*80)
        print("".center(80, "="))
        print("Criar Nova Conta".center(80))
        print("".center(80, "="))
        while True:
            nome = input("Digite o nome do cliente: ").strip()
            if nome and nome.replace(" ", "").isalpha():
                break
            else:
                print("Nome não pode ficar vazio. Tente novamente.")

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

        # Display account information
        print("\nConta criada com sucesso!")
        print(f"O número da conta para {nome} é: {numero_conta}")

        while True:
            senha = input("Digite a senha para a conta: ").strip()
            if senha:
                break
            else:
                print("Senha não pode ficar vazia. Tente novamente.")

        nova_conta = Conta(nome, cpf, numero_conta, senha)
        self.contas.append(nova_conta)
        print("Senha definida com sucesso.")

    def gerar_numero_conta(self):
        return str(random.randint(100000, 999999))