
numbers = []
number = input("Enter a number: ")

while number != "":
        numbers.append(float(number))
        number = input("Enter a number: ")
        
numbers.sort(reverse=True)

print("The greatest numbers in descending order: ")
for _ in numbers[:5]:
        print(_)