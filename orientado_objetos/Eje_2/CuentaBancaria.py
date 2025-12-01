class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo, fecha_apertura, tipo_cuenta):
        self.__numero_cuenta = numero_cuenta
        self.__titular = titular
        self.__saldo = saldo
        self.__fecha_apertura = fecha_apertura
        self.__tipo_cuenta = tipo_cuenta

    def get_numero_cuenta(self):
        return self.__numero_cuenta

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_fecha_apertura(self):
        return self.__fecha_apertura

    def get_tipo_cuenta(self):
        return self.__tipo_cuenta

    def set_numero_cuenta(self, numero_cuenta):
        self.__numero_cuenta = numero_cuenta

    def set_titular(self, titular):
        self.__titular = titular

    def set_saldo(self, saldo):
        if saldo >= 0:
            self.__saldo = saldo
        else:
            print("El saldo no puede ser negativo.")

    def set_fecha_apertura(self, fecha_apertura):
        self.__fecha_apertura = fecha_apertura

    def set_tipo_cuenta(self, tipo_cuenta):
        self.__tipo_cuenta = tipo_cuenta

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("El monto debe ser mayor a 0.")

    def retirar(self, monto):
        if monto <= 0:
            print("El monto debe ser mayor a 0.")
        elif monto > self.__saldo:
            print("Fondos insuficientes.")
        else:
            self.__saldo -= monto
            print(f"Retiro exitoso. Saldo restante: {self.__saldo}")

    def consultar(self):
        print("---- Información de la Cuenta ----")
        print(f"Número de cuenta: {self.__numero_cuenta}")
        print(f"Titular: {self.__titular}")
        print(f"Saldo: {self.__saldo}")
        print(f"Fecha de apertura: {self.__fecha_apertura}")
        print(f"Tipo de cuenta: {self.__tipo_cuenta}")
