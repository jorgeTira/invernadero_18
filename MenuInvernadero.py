from Invernadero import Invernadero
class MenuInvernadero:
    def __init__(self, conexion, cursor):
        self.Invernadero = Invernadero(conexion,cursor)
        while True:
            print("1) Agregar Invernadero")
            print("2) Mostrar Inverndero")
            print("0) Salir")
            op = input()

            if op == "1":
                self.agregar()
            elif op == "2":
                self.mostrar()
            elif op == "0":
                break

    def agregar(self):
        nombre = input("Nombre de invernadero: ")
        ubicacion = input("Ubicacion de inverndero: ")
        id_dueno = input("ID Dueño: ")
        self.Invernadero.crear(nombre, ubicacion, id_dueno)
    def mostrar(self):
        resultados = self.Invernadero.recuperar()
        #print (resultados)
        for r in resultados:
            print("{0:3} {1:10} {2:15} {3:3}".format(r[0],r[1],r[2],r[3]))
