from entity.Administracion import Administracion
from repository.Database import Repository
def main():
    admin1 = Administracion()
    db = Repository()
    admin1.setPassword("test")
    admin1.setUsuario("test")
    db.addAdministrador(admin1)
    if db.obtenerAdministradores()[0][0] == "test":
        print("pass")
    else:
        print("Error")

if __name__ == "__main__":
    main()