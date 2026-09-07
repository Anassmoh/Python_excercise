numbers = []

while True:
    number = input("Enter a number: ")
    if number == "":
        break
    # use break to avoid double input
    numbers.append(float(number))
    
numbers.sort(reverse=True)

print("The greatest numbers in descending order: ")
for num in numbers[:5]:
        print(num)