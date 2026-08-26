cabin_class = input("Enter the cabin class (LUX, A, B, or C): ")
                

LUX = "Upper-deck cabin with a balcony."
A = "Above the car deck, equipped with a window."
B = "Windowless cabin above the car deck."
C = "Windowless cabin below the car deck."

if cabin_class == "LUX":
    print(LUX)
elif cabin_class == "A":
    print(A)
elif cabin_class == "B":
    print(B)
elif cabin_class == "C":
    print(C)
else:
    print("Invalid cabin class.")