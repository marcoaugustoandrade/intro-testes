class Conta():

    def __init__(self, numero):
        self.__numero = numero
        self.__saldo = 0.0
        self.__limite = 500.00

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo + self.__limite:
            self.__saldo -= valor

    def saldo(self):
        return self.__saldo