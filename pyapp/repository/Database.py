import sqlite3
import bcrypt
import os

PATH = './db/database.db'
class Repository():
    def __init__(self) -> None:
        try:
            print(os.getcwd())
            self.__connection = sqlite3.connect(PATH)

            self.__ready = True
        except sqlite3.Error as e:
            print('Ha ocurrido un error con la conexión a la base de datos',e)
            self.__ready = False
            self.__connection.close()

    def DBReady(self) -> bool:
        return self.__ready
    
    def addAdministrador(self,administrador):
        try:
            QUERY = 'INSERT INTO ADMINISTRACION(USERNAME,PASSWORD) VALUES (?,?)'
            cursor = self.__connection.cursor()
            datos = (administrador.getUsuario(),self.generarPasswordSeguro(administrador.getPassword()))
            cursor.execute(QUERY,datos)
            self.__connection.commit()
        except sqlite3.Error as e:
            print('Error al añadir nuevo personal administrativo',e)
            
    
    def generarPasswordSeguro(self,password) -> str:
        pwd = bytes(password,'utf-8')
        return bcrypt.hashpw(pwd,bcrypt.gensalt(10))
    
    def obtenerAdministradores(self):
        try:
            QUERY = 'SELECT * FROM ADMINISTRACION'
            cursor = self.__connection.cursor()
            cursor.execute(QUERY)
            filas = cursor.fetchall()
            return filas
        except sqlite3.Error as e:
            print('Error al obtener todo el personal administrativo',e)
            
            
        