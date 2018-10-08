from dueno import Dueno
class menuDueno:
    """docstring menuDueno."""
    def __init__(self, conexion, cursor ):
        self.dueno = Dueno(conexion, cursor)
        while True:
            print("1) Agregar Dueño")
            print("2) Mostrar Dueños")
            print("0) Salir")
            op = input()
            if op == "1":
                self.agregarDueno()
            elif op == "2":
                self.mostarDueno()
            elif op == "0":
                break
    def agregarDueno(self):
        nombre = input("Dame tu nombre: ")
        apellido = input("Dame tu apellido")
        self.dueno.crear(nombre,apellido)
    def mostarDueno(self):
        resultados = self.dueno.recuperar()
        #print (resultados)
        for r in resultados:
            print("{0:3} {1:10} {2:15}".format(r[0],r[1],r[2]))
