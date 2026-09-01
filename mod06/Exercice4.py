list = []
for _ in range(5):
    city = input("Enter the name of a city: ")
    list.append(city)

print("\n\nThe cities you entered: ")
i=0
for city in list:
    print(list[i])
    i += 1