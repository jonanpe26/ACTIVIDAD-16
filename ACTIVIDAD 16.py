class Libro:
    def __init__(self, titulo, autor, ano, codigo):
        self.titulo=titulo
        self.autor=autor
        self.ano=ano
        self.codigo=codigo
        self.disponible=True

class Usuario:
    def __init__(self, nombre, carnet, carrera):
        self.nombre=nombre
        self.carnet=carnet
        self.carrera=carrera

class resgistro_libros:
    def __init__(self):
        self.libros={}

    def registrar(self, titulo, autor, ano, codigo):
        if codigo in self.libros:
            print("Error, codigo repetido")
            return
        self.libros[codigo]=Libro(autor,ano, codigo)
class mostrar_libros:
    def __init__(self,registro_libros):
        self.registro_libros=registro_libros

    def mostrar(self):
        if not self.registro_libros.libros:
            print("no hay libros registrados")
            return
        for libro in self.resgistro_libros.libros.values():
            if libro.disponible:
                estado="disponible"
            else:
                estado="prestado"
                print(f"{libro.codigo}-{libro.titulo}-{libro.autor}({libro.ano})-{estado}")

class registro_usuarios:
    def __init__(self):
        self.usuarios={}

    def registrar(self, nombre, carnet, carrera):
        if carnet in self.usuarios:
            print("error, carnet duplicado")
            return
        self.usuarios[carnet]= Usuario(nombre, carnet, carrera)

class mostrar_usuarios:
    def __init__(self, registro_usuarios):
        self.resgistro_usuarios=registro_usuarios

    def mostrar(self):
        if not self.resgistro_usuarios.usuarios:
            print("usuarios")
        else:
            for usuario in self.resgistro_usuarios.values():
                print(f"{usuario.carnet}-{usuario.nombre}-{usuario.carrera}")

class prestar_libros:
    def __init__(self, registro_libros, registro_usuarios):
        self.prestamos={}
        self.registro_libros=registro_libros
        self.registro_usuarios=registro_usuarios

    def prestar(self, carnet, codigo):
        if carnet not in self.registro_usuarios.usuarios:
            print("error usuario no registrado")
            return
        if codigo not in self.registro_libros.libros:
            print("libro no registrado")
            return
        libro=self.registro_libros.libros[codigo]
        if not libro.disponible:
            print("error libro no disponible")
            return
        libro.disponible=False
        self.prestamos[codigo]=carnet

class devolver:
    def __init__(self, registro_libros, prestar_libro):
        self.registro_libros=registro_libros
        self.prestar_libro=prestar_libro
    def devolver(self, codigo):
        if codigo not in self.prestar_libro.prestamos:
            print("error no esta prestado el libro")
            return
        libro=self.registro_libros.libros[codigo]
        libro.disponible=True
        del self.prestar_libro.prestamos[codigo]

libros_registro = registro_libros()
libros_mostrar = mostrar_libros(libros_registro)
usuarios_registro = registro_usuarios()
usuarios_mostrar = mostrar_usuarios(usuarios_registro)
prestamos_prestar = prestar_libros(libros_registro, usuarios_registro)
prestamos_devolver = devolver(libros_registro, prestamos_prestar)

while True:
    print("1. registrar libros")
    print("2. registrar usuarios")
    print("3. mostrar libros")
    print("4. mostrar usuarios")
    print("5. pretar libro")
    print("6. devolver libro")
    print("7. salir")

    opcion =input("opcion")
    if opcion=="1":
        titulo = input("titulo: ")
        autor = input("autor: ")
        ano =input("ano: ")
        codigo =input("codigo: ")
        libros_registro.registrar(titulo, autor, ano, codigo)

    elif opcion=="2":
        nombre=input("nombre: ")
        carnet=input("carnet: ")
        carrera=input("carrera: ")
        usuarios_registro.registrar(nombre, carnet,carrera)

    elif opcion=="3":
        libros_mostrar.mostrar()

    elif opcion=="4":
        usuarios_mostrar.mostrar()
    elif opcion=="5":
        carnet=input("carnet: ")
        codigo=input("codigo: ")
        prestamos_prestar.prestar(carnet, codigo)

    elif opcion=="6":
        codigo=input("codigo: ")
        prestamos_devolver.devolver(codigo)

    elif opcion=="7":
        break

    else:
        print("opcion invalida")




