from Usuario import Usuario
import getpass
class MenuUsuario:
    def __init__(self, conexion, cursor):
        self.Usuario = Usuario(conexion, cursor)
        while True:
            print("1) Agregar Usuario")
            print("2) Logear Usuario")
            print("0) Salir")
            op = input()

            if op == "1":
                self.capturar()
            elif op == "2":
                self.login()
            elif op == "0":
                break
    def capturar(self):
        usuario = input("Ingrese un correo: ")
        contra = getpass.getpass("Ingrese un contraseña: ")
        tipo = input("Tipo: ")

        self.Usuario.crear(usuario, contra, tipo)

    def login(self):
        usuario = input("Ingrese un correo: ")
        contra = getpass.getpass("Ingrese un contraseña: ")

        if self.Usuario.login(usuario, contra):
            print("Bienvenido")
        else:
            print("Usuario o contraseña inconrrecta")
