import random


class Conta():
    def __init__(self, numConta):
        self.numero = numConta
        self.saldo = 0
        self.bonus = 0

    def deposite(self, valor):
        self.saldo = self.saldo + valor
        self.bonus += valor * 0.01

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
            return True
        else:
            return False
        


class Poupanca(Conta):

    def render(self):
        self.saldo = self.saldo + self.saldo*0.01

#Tarefa 2: Criando Classe ContaBonificada.
class ContaBonificada(Conta):
    def CalculaBonus(self):
      self.saldo += self.bonus #Tarefa 2: bonus de 0.01% sobre o valor do deposito.
    
class Banco():
    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    def getNome(self):
        return self.nome

    def criarConta(self):
        num = random.randint(0, 1000)
        c = Conta(num)
        self.contas.append(c)
        return num

    def criarPoupanca(self):
        num = random.randint(0, 1000)
        p = Poupanca(num)
        self.contas.append(p)
        return num

    #Tarefa 2: Criando novo tipo de conta
    def criarContaBonificada(self):
      num = random.randint(0, 1000)
      b = ContaBonificada(num)
      self.contas.append(b)
      return num

    def consultaSaldo(self, numConta):
        for conta in self.contas:
            if conta.numero == numConta:
                return conta.saldo
        return -1

    def depositar(self, numConta, valor):
        for conta in self.contas:
            if conta.numero == numConta:
                conta.deposite(valor - (valor * 0.01)) #Tarefa 1: Adicionando tarifa de 0.01% 
              
    def sacar(self, numConta, valor):
        for conta in self.contas:
            if conta.numero == numConta:
                return conta.sacar(valor)

    def renderPoupanca(self, numConta):
        for i in self.contas:
            if i.numero == numConta and isinstance(i, Poupanca):
                i.render()
                return True
        return False

    #Tarefa 2: Função Render Bonus
    def renderBonus(self, numConta):
        for i in self.contas:
            if i.numero == numConta and isinstance(i, ContaBonificada):
              i.CalculaBonus()
              return True
        return False