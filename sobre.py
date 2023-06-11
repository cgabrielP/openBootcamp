class Toy:
    nombre=""
    precio=0

    def __init__(self,nombre,precio) :
        self.nombre=nombre
        self.precio=precio

    def __str__(self):
        return(f'mi nombre es {self.nombre} y valgo {self.precio}')
    def __repr__(self):
        return f'Toy({self.nombre}, {self.precio})'
t1=Toy("Max Steel", 500)
print(repr(t1))#formal
print(t1)#informal

