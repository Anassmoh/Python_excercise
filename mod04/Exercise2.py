cabin = input("Enter the cabin class (LUX, A, B, or C): ")

LUX = "Upper-deck cabin with a balcony."
A = "Above the car deck, equipped with a window."
B = "Windowless cabin above the car deck."
C = "Windowless cabin below the car deck."

if cabin == "LUX":
    print(LUX)
elif cabin == "A":
    print(A)
elif cabin == "B":
    print(B)
elif cabin == "C":
    print(C)
else:
    print("Invalid cabin class.")