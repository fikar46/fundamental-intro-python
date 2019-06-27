
listItem = list(range(1,11,2));
print(listItem);
for item in range(1,11,2): 
    print(item);

for item in range(1,11,1):
    print("Nomor urut " + str(item));

for item in range(0,21,2):
    print("Nomor urut " + str(item));
for item in range(1,21,2):
    print("Nomor urut " + str(item));

z='';
for item in range(5):
    for item1 in range(5):
        z+= ' * '
    z+= '\n'
print(z);

z='';
for item in range(5):
    for item1 in range(0,item+1):
        z+= ' * '
    z+= '\n'
print(z);

z='';
for item in range(5):
    for item1 in range(0,5-item):
        z+= ' * '
    z+= '\n'
print(z);s

z='';
for item in range(5):
    for item1 in range(0,5-item):
        z+= ' * '
    z+= '\n'
for item in range(5):
    for item1 in range(0,item+1):
        z+= ' * '
    z+= '\n'
print(z);
