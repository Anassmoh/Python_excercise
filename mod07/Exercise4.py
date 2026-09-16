def filter_even_numbers(list):
    for i in list:
        if i % 2 == 0:
            filtered_list.remove(i)
    return filtered_list
    
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = original_list
filtered_list = filter_even_numbers(original_list)
print("Original list:", original_list)
print("List with even numbers only:", filtered_list)