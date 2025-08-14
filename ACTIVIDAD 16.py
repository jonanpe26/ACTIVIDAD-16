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

class libros:
    def __init__(self):
        self.libros={}

    def registrar(self, titulo, autor, ano, codigo):
        if codigo in self.libros:
            print("Error, codigo repetido")
            return
        self.libros[codigo]=libro(autor,ano, codigo)
    def mostrar(self):
        if not self.libros:
            print("no hay libros registrados")
        else:
            for libro in self.libros.values():

