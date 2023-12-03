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
        
        # Valide e obtenha o nome de usuário
        while True:
            self.nome_usuario = input("Digite o nome de usuário para o administrador: ").strip()
            if self.nome_usuario:
                break
            print("Por favor, insira um nome de usuário válido.")

        # Valide e obtenha a senha
        while True:
            self.senha = input("Digite a senha para o administrador: ").strip()
            if self.senha:
                break
            print("Por favor, insira uma senha válida.")

        print("\nUsuário e senha do administrador criados com sucesso.")

    def autenticar_admin(self):
        print("\n" + "="*30)
        print("Bem-vindo ao Sistema Bancário!")
        print("="*30)
        
        # Valide e obtenha o nome de usuário
        while True:
            nome_usuario = input("Digite o nome de usuário: ").strip()
            if nome_usuario:
                break
            print("Por favor, insira um nome de usuário válido.")

        # Valide e obtenha a senha
        while True:
            senha = input("Digite a senha: ").strip()
            if senha:
                break
            print("Por favor, insira uma senha válida.")

        return nome_usuario == self.nome_usuario and senha == self.senha

    def criar_conta(self):
        print("\n" + "="*30)
        print("Criar Nova Conta")
        print("="*30)
        
        # Valide e obtenha o nome
        while True:
            nome = input("Digite o nome do cliente: ").strip()
            if nome.replace(" ", "").isalpha():
                break
            print("Por favor, insira um nome válido (apenas letras e espaços).")

        # Valide e obtenha o CPF
        while True:
            cpf = input("Digite o CPF do cliente (apenas números, 11 dígitos): ").strip()
            if cpf.isdigit() and len(cpf) == 11:
                break
            print("Por favor, insira um CPF válido (11 números).")

        # Verifique se a conta com o CPF fornecido já existe
        for conta in self.contas:
            if conta.cpf == cpf:
                print("Já existe uma conta registrada com este CPF.")
                return

        numero_conta = self.gerar_numero_conta()
        senha = input("Digite a senha para a conta: ").strip()

        nova_conta = Conta(nome, cpf, numero_conta, senha)
        self.contas.append(nova_conta)
        
        print("\nConta criada com sucesso!")
        print(f"O número da conta para {nome} é: {numero_conta}")

    def gerar_numero_conta(self):
        return str(random.randint(100000, 999999))
