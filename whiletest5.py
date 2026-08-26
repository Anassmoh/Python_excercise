
command_1 = input("would you like to calculate the sum, deduction or multiplication? if yes enter desired calculation: ")

while command_1 != "no":
   first = int(input("Enter a number: "))
   second = int(input("Enter the second number: "))
   sum = first + second
   deduction = first - second
   multiplication = first * second
    
   if  command_1 == "sum":
             print(f"the sum of your number is {sum}")
   elif command_1 == "deduction":
             print(f"the deduction of your number is {deduction}")
   elif command_1 == "multiplication":
             print(f"the multiplication of your number is {multiplication}")
   else:
             print("please choose an option or type 'no' to exit")



   command_1 = input("would you like to calculate the sum, deduction or multiplication? if yes enter desired calculation: ")