menu = """===================================================
Conta atual {}
===================================================
[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova conta
[nu] Novo usuário
[tc] Trocar conta atual
[q] Sair
===================================================
"""

class usuario:
    def __init__(self, nome, data_de_nascimento, cpf, endereco):
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.cpf = cpf
        self.endereco = endereco
    
    def criar_conta(self):
        nova_conta = conta(self, 500)
        contas.append(nova_conta)
        return nova_conta

class conta:
    def __init__(self, usuario, limite, saldo=0, numero_saques=0, LIMITE_SAQUES=3):
        self.saldo = saldo
        self.limite = limite
        self.numero_saques = numero_saques
        self.LIMITE_SAQUES = LIMITE_SAQUES

        self.agencia = "0001"
        self.numero_conta = len(contas)
        self.usuario = usuario

        self.extrato = ""

    def adicionar_ao_extrato(self, option, val):
        self.extrato += f"{option} : R$ {val:.2f}\n"
    
    def depositar(self, val, /):
        if val > 0:
            self.saldo += val
            self.adicionar_ao_extrato("Depósito", val)
            print("Deposito realizado")
        else:
            print("Valor inválido")
    
    def sacar(self, *, val):
        if val > self.saldo:
            print("Saldo insuficiente")
        elif val > self.limite:
            print("O valor excede o limite")
        elif self.numero_saques >= self.LIMITE_SAQUES:
            print("Máximo de saques excedido")
        elif val > 0:
            self.saldo -= val
            self.adicionar_ao_extrato("Saque", val)
            self.numero_saques += 1
            print("Saque realizado")
        else: 
            print("Valor inválido")
    
    def imprimir_extrato(self, saldo, /, extrato):
        print(f"""
===================================================
Extrato: 
===================================================
{"Sem movimentações." if not self.extrato else self.extrato}
Saldo: R$ {self.saldo:.2f}
===================================================
        """)

def procurar_cpf(cpf):
    for u in usuarios:
        if u.cpf == cpf:
            return u
    return None

def novo_usuario():
    cpf = input("Informe CPF do usuário (apenas números): ")
    if procurar_cpf(cpf):
        return "CPF ja cadastrado"
    nome = input("Informe nome de usuário: ")
    ddn = input("Informe data de nascimento: ")
    endereco = input("Informe endereço: ")
    usuarios.append(usuario(nome,ddn,cpf,endereco))
    return "Usuário registrado"

def trocar_conta():
    nc = int(input("Informe o número da conta: "))
    for c in contas:
        if c.numero_conta == nc:
            conta_atual = u
            return "Conta alterada"
    return "Conta invalida"

if __name__ == "__main__":
    usuarios = []
    contas = []

    conta_atual = None

    while True:
        option = input(menu.format(conta_atual.numero_conta if conta_atual else "_"))

        if option == "d":
            if conta_atual:
                try:
                    val = float(input("Informe valor do deposito: "))
                    conta_atual.depositar(val)
                except:
                    print("Valor invalido")
            else:
                print("Crie uma conta")
        elif option == "s":
            if conta_atual:
                try:
                    val = float(input("Informe valor do saque: "))
                    conta_atual.sacar(val=val)
                except:
                    print("Valor invalido")
            else:
                print("Crie uma conta")
        elif option == "e":
            if conta_atual:
                conta_atual.imprimir_extrato(conta_atual.saldo, conta_atual.extrato)
            else:
                print("Crie uma conta")
        elif option == "nu":
            novo_usuario()
        elif option == "nc":
            cpf = input("Informe CPF do usuário para criar a conta: ")
            u = procurar_cpf(cpf)
            if u:
                conta_atual = u.criar_conta()
                print("Conta criada")
            else:
                print("CPF não encontrado")
        elif option == "tc":
            print(trocar_conta())
        elif option == "q":
            break
        else:
            print("Opção inválida")
