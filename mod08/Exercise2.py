names = set()
while True:
    name = input("Enter a name: ")
    if name == "":
        break
    elif name in names:
        print("Existing name")
    else:
        names.add(name)
        print("New name")

for name in names:
    print(name)