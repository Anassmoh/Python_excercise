number = int(input("Enter an integer: "))
test = []
for i in range(number):
    modulo = number % (i+1)
    test.append(modulo)

if test.count(0) == 2:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")