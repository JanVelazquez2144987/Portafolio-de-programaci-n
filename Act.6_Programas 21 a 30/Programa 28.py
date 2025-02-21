class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente")

    def obtener_saldo(self):
        return self.saldo

# Ejemplo de uso
cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
cuenta.retirar(200)
print(cuenta.obtener_saldo())
