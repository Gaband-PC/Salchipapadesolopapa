class CuentaBancaria:
    def __init__(self, numero, titular, saldo=0, usuario="", clave=""):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.usuario = usuario
        self.clave = clave

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito de {monto} realizado. Nuevo saldo: {self.saldo}")
        else:
            print("El monto a depositar debe ser positivo.")

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro de {monto} realizado. Nuevo saldo: {self.saldo}")
            return True
        else:
            print("Fondos insuficientes o monto inválido para retirar.")
            return False

    def transferir(self, cuenta_destino, monto):
        if monto <= 0:
            print("El monto a transferir debe ser positivo.")
            return False
        if monto > self.saldo:
            print("Fondos insuficientes para realizar la transferencia.")
            return False
        
        self.saldo -= monto
        cuenta_destino.depositar(monto)
        print(f"Transferencia exitosa de {monto} de {self.titular} a {cuenta_destino.titular}.")
        print(f"Saldo actual de {self.titular}: {self.saldo}")
        return True

    def mostrar_saldo(self):
        return self.saldo


# Crear las cuentas iniciales
cuentas = [
    CuentaBancaria("001", "Neider Paternina Escobar", 17_000_000, "neiderp", "clave123"),
    CuentaBancaria("002", "Juan Daniel Perez", 0, "juandp", "clave456"),
    CuentaBancaria("003", "Johan Gomez", 100_000, "johang", "clave789"),
    CuentaBancaria("004", "Gabriel Herazo", 500_000, "gabrielh", "clave321")
]

# Función para validar usuario y clave
def validar_acceso(usuario, clave):
    for cuenta in cuentas:
        if cuenta.usuario == usuario and cuenta.clave == clave:
            print(f"Acceso concedido para {cuenta.titular}")
            return cuenta
    print("Usuario o clave incorrectos.")
    return None

# Función principal con menú y control de sesión
def menu():
    while True:  # ciclo para iniciar sesión repetidamente
        print("=== Bienvenido al Cajero Automático ===")
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")
        cuenta_actual = validar_acceso(usuario, clave)
        if not cuenta_actual:
            continue  # si usuario/clave no coincide, vuelve a pedir


        while True:  # menú de opciones para usuario autenticado
            print("\nOpciones:")
            print("1. Consultar saldo")
            print("2. Depositar dinero")
            print("3. Retirar dinero")
            print("4. Transferir dinero")
            print("5. Salir")


            opcion = input("Seleccione una opción: ")


            if opcion == "1":
                print(f"Saldo actual: {cuenta_actual.mostrar_saldo()}")


            elif opcion == "2":
                try:
                    monto = float(input("Ingrese monto a depositar: "))
                except ValueError:
                    print("Por favor, ingrese un número válido.")
                    continue
                cuenta_actual.depositar(monto)


            elif opcion == "3":
                try:
                    monto = float(input("Ingrese monto a retirar: "))
                except ValueError:
                    print("Por favor, ingrese un número válido.")
                    continue
                cuenta_actual.retirar(monto)


            elif opcion == "4":
                print("Cuentas disponibles para transferencia:")
                for c in cuentas:
                    if c != cuenta_actual:
                        print(f"- {c.numero} Titular: {c.titular}")
                numero_destino = input("Ingrese el número de cuenta destino: ")
                try:
                    monto = float(input("Ingrese monto a transferir: "))
                except ValueError:
                    print("Por favor, ingrese un número válido.")
                    continue
                cuenta_destino = None
                for c in cuentas:
                    if c.numero == numero_destino:
                        cuenta_destino = c
                        break
                if cuenta_destino:
                    cuenta_actual.transferir(cuenta_destino, monto)
                else:
                    print("Cuenta destino no encontrada.")


            elif opcion == "5":
                print("Cerrando sesión...\n")
                break  # salir del menú y pedir login de nuevo


            else:
                print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
