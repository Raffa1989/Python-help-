contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

name = input()
result = None
for x in contacts:
    if name in x:
        result = x[0] + " is " + str(x[1])
        break
    else:
        continue

if result:
    print(result)
else:
    print(f'{name} not found')
       
