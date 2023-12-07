import random
import time

class Conta:
    def __init__(self, nome, cpf, numero_conta, saldo=0.0):
        self.nome = nome
        self.cpf = cpf
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.senha = None

    def cadastrar_senha(self, senha):
        self.senha = senha
        print("\nSenha cadastrada com sucesso.")
        time.sleep(2)

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
            self.nome_usuario = input("\nDigite o nome de usuário para o administrador: ").strip()
            if self.nome_usuario:
                break
            print("Por favor, insira um nome de usuário válido.")

        while True:
            self.senha = input("Digite a senha para o administrador: ").strip()
            if self.senha:
                break
            print("Por favor, insira uma senha válida.")

        print("\nUsuário e senha do administrador criados com sucesso.")
        time.sleep(2)

    def autenticar_admin(self):
        print("="*30)
        print("Bem-vindo ao ATM Banco!")
        print("="*30)

        while True:
            nome_usuario = input("\nDigite o nome de usuário: ").strip()
            if nome_usuario:
                break
            print("Por favor, insira um nome de usuário válido.")

        while True:
            senha = input("Digite a senha: ").strip()
            if senha:
                break
            print("Por favor, insira uma senha válida.")

        return nome_usuario == self.nome_usuario and senha == self.senha

    def criar_conta(self):
        print("="*30)
        print("Criar Nova Conta")
        print("="*30)

        while True:
            nome = input("\nDigite o nome do cliente: ").strip()
            if nome.replace(" ", "").isalpha():
                break
            print("Por favor, insira um nome válido (apenas letras e espaços).")

        while True:
            cpf = input("Digite o CPF do cliente (apenas números, 11 dígitos): ").strip()
            if cpf.isdigit() and len(cpf) == 11:
                break
            print("Por favor, insira um CPF válido (11 números).")

        for conta in self.contas:
            if conta.cpf == cpf:
                print("\nJá existe uma conta registrada com este CPF.")
                time.sleep(2)
                return

        numero_conta = self.gerar_numero_conta()
        nova_conta = Conta(nome, cpf, numero_conta)
        self.contas.append(nova_conta)

        print("\nConta criada com sucesso!")
        print(f"O número da conta para o cliente {nome} é: {numero_conta}")
        time.sleep(2)

        senha = input("\nDigite a senha para a conta: ").strip()
        nova_conta.cadastrar_senha(senha)

    def gerar_numero_conta(self):
        return str(random.randint(10000, 999999))
