# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 13:37:49 2018

@author: Usuario
"""

#!/usr/bin/python
#import mysql.connector
#conexion = mysql.connector.connect(user='luis', password='12345', database='invernadero')

#cur = conexion.cursor()

#insertar = ('INSERT INTO dueno (nombre, apellidos) VALUES("Jorge", "Tirado")')

#cur.execute(insertar)

#conexion.commit()

class Dueno:
    def __init__(self,conexion,cursor):
        self.conexion = conexion
        self.cursor = cursor
    def crear(self,nombre,apellidos):
        insertar = ('INSERT INTO dueno(nombre, apellidos) VALUES(%s,%s)')
        self.cursor.execute(insertar, (nombre,apellidos))
        self.conexion.commit()
    def recuperar(self):

        select = ('SELECT * FROM dueno ')
        self.cursor.execute(select)
        resultados = self.cursor.fetchall()
        return resultados
