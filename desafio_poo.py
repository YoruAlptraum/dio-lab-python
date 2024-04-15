from abc import ABC, abstractmethod

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

class PessoaFisica:
    def __init__(self, cpf: str, nome: str, data_nascimento):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self._cpf
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def data_nascimento(self):
        return self._data_nascimento    
    
class Cliente(PessoaFisica):
    def __init__(self,*, cpf: str, nome: str, data_nascimento: str, endereco: str):
        super().__init__(cpf, nome, data_nascimento)
        self._endereco = endereco
        self._contas = []
    
    def criar_conta_corrente(self):
        nova_conta = ContaCorrente(self, limite=500)
        contas.append(nova_conta)
        self._contas.append(nova_conta)
        return nova_conta

# class Transacao(ABC):
#     def __init__(self, valor):
#         self._valor = valor
    
#     @property
#     def valor(self):
#         return self._valor

#     @classmethod
#     @abstractmethod
#     def registrar(self, conta):
#         pass
    
# class Saque(Transacao):
#     def registrar(self, conta):
#         sucesso_transacao = conta.sacar(self.valor)

#         if sucesso_transacao:
#             conta.historico.adicionar_transacao(self)

# class Deposito(Transacao):
#     def registrar(self, conta):
#         sucesso_transacao = conta.depositar(self.valor)

#         if sucesso_transacao:
#             conta.historico.adicionar_transacao(self)

class Extrato:
    def __init__(self) -> None:
        self._extrato = ""
    
    def adicionar_transacao(self, option, val):
        self._extrato += f"{option} : R$ {val:.2f}\n"

    @property
    def extrato(self):
        return self._extrato
    
class Conta:
    def __init__(self, usuario):
        self._saldo = 0
        self._agencia = "0001"
        self._numero_conta = len(contas)
        self._usuario = usuario

        self._extrato = Extrato()

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero_conta(self):
        return self._numero_conta

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    def depositar(self, val):
        if val > 0:
            self._saldo += val
            self._extrato.adicionar_transacao("Depósito", val)
            print("Deposito realizado")
        else:
            print("Valor inválido")
    
    def imprimir_extrato(self):
        print(f"""
===================================================
Extrato: 
===================================================
{"Sem movimentações." if not self._extrato.extrato else self._extrato.extrato}
Saldo: R$ {self.saldo:.2f}
===================================================
        """)

class ContaCorrente(Conta):
    def __init__(self, usuario, /, limite: float, LIMITE_SAQUES: int=3):
        super().__init__(usuario)
        self._limite = limite
        self._numero_saques = 0
        self._LIMITE_SAQUES = LIMITE_SAQUES
    
    def sacar(self, *, val):
        if val > self.saldo:
            print("Saldo insuficiente")
        elif val > self.limite:
            print("O valor excede o limite")
        elif self.numero_saques >= self.LIMITE_SAQUES:
            print("Máximo de saques excedido")
        elif val > 0:
            self.saldo -= val
            self._extrato.adicionar_transacao("Saque", val)
            self.numero_saques += 1
            print("Saque realizado")
        else: 
            print("Valor inválido")


def procurar_cpf(cpf):
    for u in usuarios:
        if u.cpf == cpf:
            return u
    return None

def novo_usuario():
    cpf = input("Informe CPF do usuário (apenas números): ")
    if procurar_cpf(cpf):
        return "CPF ja tem cadastro"
    nome = input("Informe nome de usuário: ")
    ddn = input("Informe data de nascimento: ")
    endereco = input("Informe endereço: ")
    usuarios.append(Cliente(cpf=cpf, nome=nome,data_nascimento=ddn,endereco=endereco))
    return "Usuário cadastrado com sucesso"

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
                conta_atual.imprimir_extrato()
            else:
                print("Crie uma conta")
        elif option == "nu":
            print(novo_usuario())
        elif option == "nc":
            cpf = input("Informe CPF do usuário para criar a conta: ")
            u = procurar_cpf(cpf)
            if u:
                conta_atual = u.criar_conta_corrente()
                print("Conta criada")
            else:
                print("CPF não encontrado")
        elif option == "tc":
            print(trocar_conta())
        elif option == "q":
            break
        else:
            print("Opção inválida")
