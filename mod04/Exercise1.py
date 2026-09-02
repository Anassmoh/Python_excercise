length = float(input("Enter the length of the zander in centimeters: "))
missing_cm = 42 - length

if missing_cm > 0:
    print(f"The zander does not meet the size limit.\nPlease release the fish back into the lake.\nThe fish was {missing_cm:.1f} centimeters below the size limit.")
else:
    print("The zander meets the size limit.")