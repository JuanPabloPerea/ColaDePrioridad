# se importa las datos neceesarios la clase de colas por prioridad
# y la clase persona
from queue import PriorityQueue
from Persona import Dato

# se crean objetos de tipo persona con nombre,
# apellido, direccion y telefono

a = "Juan Pablo "
b = "Perea Hernandez"
c = "sopas"
d = 123456789

a2 = "Maria Jose"
b2 = "Rodriguez x"
c2 = "sop"
d2 = 123654789

a3 = "Pedro Pablo"
b3 = "Leon Jaramillo"
c3 = "sas"
d3 = 951736482

a4 = "Maria Paola"
b4 = "Naranjo y"
c4 = "sop"
d4 = 741852963

a5 = "Pedro Pablo"
b5 = "Leon Jaramillo"
c5 = "feed"
d5 = 741963852

per = Dato(a,b,c,d)
per2 = Dato(a2,b2,c2,d2)
per3 = Dato(a3,b3,c3,d3)
per4 = Dato(a4,b4,c4,d4)
per5 = Dato(a5,b5,c5,d5)


persona = (per.apellido,per.nombre,per.direccion,per.telefono)
persona2 = (per2.apellido,per2.nombre,per2.direccion,per2.telefono)
persona3 = (per3.apellido,per3.nombre,per3.direccion,per3.telefono)
persona4 = (per4.apellido,per4.nombre,per4.direccion,per4.telefono)
persona5 = (per5.apellido,per5.nombre,per5.direccion,per5.telefono)

# se inicializa las colos de prioridad

pq = PriorityQueue()

# se va llena la lista con el metodo put

pq.put(persona)
pq.put(persona2)
pq.put(persona3)
pq.put(persona4)
pq.put(persona5)


while not pq.empty():
    item = pq.get()
    print(item)