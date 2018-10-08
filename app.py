# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 14:03:39 2018

@author: Usuario
"""

import mysql.connector
from dueno import Dueno
from menuDueno import menuDueno
from MenuInvernadero import MenuInvernadero
from MenuUsuario import MenuUsuario
from MenuPlanta import MenuPlanta
from MenuRegistro import MenuRegistro
conexion = mysql.connector.connect(user='root',password='',database='invernadero')
cursor = conexion.cursor()
#menuD = menuDueno()
##d = Dueno(conexion, cursor)

while True:
    print("1) Menu Dueño")
    print("2) Menu Invernadero")
    print("3) Menu Usuario")
    print("4) Menu Planta")
    print("5) Menu Registro")
    print("0) Salir")
    op = input()

    if op == "1":
        menuD = menuDueno(conexion, cursor)
    elif op == "2":
        menuI = MenuInvernadero(conexion,cursor)
    elif op == "3":
        menuU = MenuUsuario(conexion, cursor)
    elif op == "4":
        menuP = MenuPlanta(conexion, cursor)
    elif op == "5":
        menuR = MenuRegistro(conexion, cursor)
    elif op == "0":
        break
"""
#d.crear('Pedrito', 'Sola')
r = d.recuperar()
print(r)

for i in r:
    for v in i:
        print(v)
"""
