def del_duples1(our_list):
    for elem in our_list:
        for _ in range(our_list.count(elem)-1):
            our_list.remove(elem)

    return our_list

def del_duples2(our_list):
    i = 0
    while i < len(our_list):
        j = 0
        while j < (our_list.count(our_list[i])-1):
            our_list.remove(our_list[i])
            j += 1
        i += 1

    return our_list


user_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 9, 9, 9]
print(del_duples1(user_list))
print(del_duples2(user_list))
