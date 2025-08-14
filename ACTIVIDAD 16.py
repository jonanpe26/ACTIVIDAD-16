class libro:
    def __init__(self, titulo, autor, ano, codigo):
        self.titulo=titulo
        self.autor=autor
        self.ano=ano
        self.codigo=codigo
        self.disponible=True

class usuario:
    def __init__(self, nombre, carnet, carrera):
        self.nombre=nombre
        self.carnet=carnet
        self.carrera=carrera

class resgistra_libros:
    def __init__(self):
        self.libros={}

    def registrar(self, titulo, autor, ano, codigo):
        if codigo in self.libros:
            print("Error, codigo repetido")
            return
        self.libros[codigo]=libro(autor,ano, codigo)
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

