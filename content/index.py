set_par = {0, 2, 4, 6, 8}
set = {1, 3, 4, 5, 6, 7}
dict = {
    "name": "pepe",
    "apellido": "pep",
}
list = ["pera", "manzana", "uva"]
tuple = ("a", "b", "c")
num_list=[1,2,3,4,2,45,35,4,544,1,2,4,7,43,8,5]
ordered_list=sorted(num_list)
reversed_ordered_list=sorted(num_list, reverse=True)
list.append("j")
list.pop(1)
list.remove("j")
print(list)
print(dict)
print(set | set_par)
print(set & set_par)
print(set - set_par)
print(set ^ set_par)
print(num_list)
print(ordered_list)
print(reversed_ordered_list)
if "pera" in list:
    print("consegui la pera")

# calculadora de imc
""" def calcular_imc(peso, altura):
    imc = peso / altura**2
    return imc

height = float(input("Ingresa tu altura en metros "))
weight = float(input("Ingresa tu peso en kilogramos "))
imc = round(calcular_imc(weight, height), 2)
print(f"Tu indice de masa corporal es: {imc}") """
