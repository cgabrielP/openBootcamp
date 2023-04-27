import math,random
pronouns = ["The", "Our", "A"]
names = ["pepe", "cr7","elbichosiuu"]
domains = ["@gmail", "@hotmail","@yahoo","@icloud"]
births=["23-03","17-07" ]
dots = [".com", ".us", ".net", ".io"]

for i in range(0,len(pronouns)):
    for j in range(0,len(names)):
        for k in range(0,len(domains)):
            for w in range(0,len(dots)):
                print(f'{pronouns[i]}{names[j]}{domains[k]}{dots[w]}')

pronounIndex = math.floor(random.randrange(len(pronouns)) )
nameIndex = math.floor(random.randrange(len(names)))
domainIndex = math.floor(random.randrange(len(domains)))
dotIndex = math.floor(random.randrange(len(dots)))

birthIndex = math.floor(random.randrange(len(births)))
print("Este es el random")
print(f'{pronouns[pronounIndex]}.{births[birthIndex]}{names[nameIndex]}{domains[domainIndex]}{dots[dotIndex]}')