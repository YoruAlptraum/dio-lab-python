menu = """===================================================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
===================================================
"""

class conta:
    def __init__(self):
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

    def adicionar_ao_extrato(self, option, val):
        self.extrato += f"{option} : R$ {val:.2f}\n"
    
    def depositar(self):
        try:
            val = float(input("Informe valor do deposito: "))
            if val > 0:
                self.saldo += val
                self.adicionar_ao_extrato("Depósito", val)
                print("Deposito realizado")
            else:
                raise
        except: 
            print("Valor inválido")
    
    def sacar(self):
        try:
            val = float(input("Informe valor do saque: "))
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
        except: 
            print("Valor inválido")
    
    def imprimir_extrato(self):
        print(f"""
===================================================
Extrato: 
===================================================
{"Sem movimentações." if not self.extrato else self.extrato}
Saldo: R$ {self.saldo:.2f}
===================================================
        """)


if __name__ == "__main__":
    acc = conta()
    while True:
        option = input(menu)

        if option == "d":
            acc.depositar()
        elif option == "s":
            acc.sacar()
        elif option == "e":
            acc.imprimir_extrato()
        elif option == "q":
            break
        else:
            print("Opção inválida")
