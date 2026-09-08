def sum_of_list(number_list):
    result = 0
    for i in number_list:
        result += i
    return result
    
number_list = [1,2,3,4,5]
print("The sum of the numbers in the list is:", sum_of_list(number_list))