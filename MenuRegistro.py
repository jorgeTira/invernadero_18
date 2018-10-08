from Registro import Registro
class MenuRegistro:
    def __init__(self, conexion, cursor):
        self.Registro = Registro(conexion,cursor)
        while True:
            print("1) Agregar Registro")
            print("2) Mostrar Registro")
            print("0) Salir")
            op = input()

            if op == "1":
                self.agregar()
            elif op == "2":
                self.mostrar()
            elif op == "0":
                break

    def agregar(self):
        fecha = input("Fecha de Cultivo de Planta : ")
        pH = input("PH de la planta: ")
        luz = input("Luz de la planta: ")
        humedad = input("Humedad de la planta: ")
        c02 = input("Co2 de la planta: ")
        id_planta = input("ID de la planta: ")
        self.Registro.crear(fecha, pH, luz,humedad,c02,id_planta)
    def mostrar(self):
        id_planta = input("Dame el id de la planta: ")
        resultados = self.Registro.recuperar(id_planta)
        #print (resultados)
        #print(resultados)
        for r in resultados:
            print("{0:3} {1:5} {2:5} {3:5} {4:5} {4:5} {5:5} {6:5}".format(r[0],str(r[1]),r[2],r[3],r[4],r[5],r[6]))
