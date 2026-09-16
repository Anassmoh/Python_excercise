def filter_even_numbers(list):
    for i in list:
        if i % 2 == 0:
            filetered_list.remove(i)
    return filetered_list

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filetered_list = original_list
print("Original list:", original_list)
print("List with even numbers only:", filter_even_numbers(original_list))