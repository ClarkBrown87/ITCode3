def get_elem(our_list):
    for index, element in enumerate(our_list):
        if (index + 1) % 3 == 0:
            print(index, element)


user_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
get_elem(user_list)
