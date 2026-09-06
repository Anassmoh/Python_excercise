gender = input("Enter biological gender (male/female): ")


low = "Your hemoglobin is low."
normal = "Your hemoglobin is normal."
high = "Your hemoglobin is high."

# requirement is to ignore only the format of the first letter in moodle but testing is ignoring the whole word.

if gender[0].lower() + gender[1:] == "male":

    hemoglobin = float(input("Enter hemoglobin value (g/l): "))

    if hemoglobin > 167:
            print(high)
    elif hemoglobin > 134:
            print(normal)
    else:
            print(low)

elif gender[0].lower() + gender[1:] == "female":

    hemoglobin = float(input("Enter hemoglobin value (g/l): ")) 
    if hemoglobin > 155:
            print(high)
    elif hemoglobin > 117:
            print(normal)
    else:
            print(low)
else:
       print("Invalid gender.")

# would still ask about hemoglobin eventhough gender is invalid on moodle testing
