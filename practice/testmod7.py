def sum_of_list(list):
    i = 0
    for number in list:
        print(list[i])
        i += 1
    return number
    
number_list = [10, 20, 30, 4, 5]
result = sum_of_list(number_list)
print(f"The sum of the numbers in the list is: {result}")
