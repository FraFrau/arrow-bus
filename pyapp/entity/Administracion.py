class Administracion():
    def __init__(self) -> None:
        self.__usuario = ""
        self.__passwd = ""
    
    def setUsuario(self,username) -> None:
        self.__usuario = username

    def setPassword(self,password) -> None:
        self.__passwd = password
    
    def getUsuario(self) -> str:
        return self.__usuario
    
    def getPassword(self) -> str:
        return self.__passwd