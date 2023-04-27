my_str="Hello wOrld, how you doin, fool"
my_list=["hola","como","estas","tu"]
list_to_str=" chupa el perro ".join(my_list)
number="5"
print(my_str)
print(my_str.capitalize())
print(my_str.lower())
print(my_str.title())
print(my_str.upper())
print(my_str.replace("l","j"))
print(my_str.find("llo"))
print(my_str.split())
print(my_str.lower().replace("o", "y").split(","))
print(my_list)
print(list_to_str)
print(number.isnumeric())

for i in range(5):
    print(f'hola{i}')