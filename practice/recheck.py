list = []
def sum(*number):
    for n in number:
        list.append(n)
    return list


print(sum(1, 2, 3, 4))