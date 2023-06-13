nombre="pepe"
anonima= lambda arg:print("hola",arg)
def hola_mundo():
    global nombre
    nombre=input("tu nombre es: ")
    return ("hola mundo", nombre)

def suma(a,b=2,c=5):
    return (a+b+c)


def hogar(**any_dict):
    for key, value in any_dict.items():
        print(key, ':',value)

def acumulador(**kwargs):
    inicial=kwargs["inicial"] if "inicial" in kwargs else 0
    final=kwargs["final"] if "final" in kwargs else 0 #operador ternario
    res=0
    for i in range(inicial,(final+1)):
        res+=i
    return res

hogar(name = "pepe")
print(hola_mundo())
print(nombre)
print(suma(2))
print(acumulador(final=5))
anonima("Carlos")