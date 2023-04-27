from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod #metodo abstracto no es heredado por otras clases
    def sonido(self):
        pass
    def diHola(self):
        print("hola")

class Perro(Animal):
    def sonido(self):
        print("guau")

class Gato(Animal):
    def sonido(self):
        print("miau")

p=Perro()
p.sonido()
p.diHola()
g=Gato()
g.sonido()
g.diHola()