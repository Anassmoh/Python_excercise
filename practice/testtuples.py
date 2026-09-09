def get_season(number):
    winter, spring, summer, autumn = (12,1,2),(3,4,5),(6,7,8),(9,10,11)
    if number in winter:
        season = "The season is winter."
    elif number in spring:
        season = "The season is spring."
    elif number in summer:
        season = "The season is summer."
    elif number in autumn:
        season = "The season is autumn."
    else:
        season = "Please enter a number between 1 and 12."
    return season
    
number = int(input("Enter the number of a month (1-12): "))
season = get_season(number)
print(f"You entered: {number}\n{season}")