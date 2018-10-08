class Invernadero:
    def __init__(self, conexion, cursor):
        self.conexion = conexion
        self.cursor = cursor

    def crear (self, nombre, ubicacion, id_dueno):
        insertar = ('INSERT INTO invernadero(nombre, ubicacion,id_dueno) VALUES(%s,%s,%s)')
        self.cursor.execute(insertar, (nombre,ubicacion,id_dueno))
        self.conexion.commit()
    def recuperar(self):

        select = ('SELECT * FROM invernadero ')
        self.cursor.execute(select)
        resultados = self.cursor.fetchall()
        return resultados
