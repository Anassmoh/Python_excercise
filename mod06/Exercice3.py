number = int(input("Enter an integer: "))
modulos = []

i = 0

while i < number:

    div = number % (i+1)
    modulos.append(div)
    i += 1

if number == 0 or number == 1:
    print(number, "is not a prime number.")
elif modulos.count(0) > 2:
    print(number, "is not a prime number.")
else:
    print(number, "is a prime number.")
