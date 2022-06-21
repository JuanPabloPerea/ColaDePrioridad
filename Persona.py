class Dato:

    def __init__(self, nombre, apellido, direccion, telefono = 0, ):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono


    def imprimir(self):
        print("mi nimbre es: ",self.nombre, self.apellido)
        print("mi direccion es: ", self.direccion)
        print("mi telefono es: ",self.telefono)





