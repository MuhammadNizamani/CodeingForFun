inp = input("Enter name :")
listName = inp.split()
l = []
for i in listName:
    l.append(i.capitalize())

print(' '.join(l))
