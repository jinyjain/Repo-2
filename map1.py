import random
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
for i in range(len(names)):
    result=list(map(lambda n:random.choice(code_names),names))
print(result)
