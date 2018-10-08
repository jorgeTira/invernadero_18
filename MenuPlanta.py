from Planta import Planta
from datetime import date
class MenuPlanta:
    def __init__(self, conexion, cursor):
        self.Planta = Planta(conexion, cursor)
        
        while True:
            print ("1) Agregar Planta")
            print("2) Buscar Planat")
            print("0) Salir")
            op = input()
            if op == '1':
                self.agregar()
            elif op == '2':
                self.buscar()
            elif op == '0':
                break
    def agregar(self):
        cultivo = input("Cultivo: ")
        dia = input("Dia: ")
        mes = input("Mes: ")
        year = input("Año: ")
        fecha = date(int(year), int(mes), int(dia))
        #fecha = datetime.now().date()
        id_inv = input("Id invernadero: ")
        id_clasi = input("Id Clasificacion ")
        self.Planta.agregar(cultivo, fecha, id_clasi, id_inv)
        
    def buscar(self):
        id_inv = input("Id de inverndero")
        resultado = self.Planta.buscar(id_inv)
        for p in resultado:
            print("{0:2} {1:10} {2:10}".format(p[0], p[1], str(p[2])))
        
        """
        
        dofpskpfodas
        """