money = float(input("Enter money: "))

cost_of_peanuts = 5

if money >= cost_of_peanuts:
    print("Hello you're about to buy peanuts")

    if money >= 20:
        print("You can also buy cake")

    pay = input("You have a club card? : ")

    if pay == "yes":
        print("It will be " + str(cost_of_peanuts-1))

    else:
        print("it will be " + str(cost_of_peanuts))
