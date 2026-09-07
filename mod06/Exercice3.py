number = int(input("Enter an integer: "))
result = 0
for n in range(number):
    test = number % (number - n)
    if test == 0:
        result += 1
if result != 2:
    print(number, "is not a prime number.")
else: 
    print(number, "is a prime number.")