def have_dupl(our_list):
    for elem in our_list:
        new_list = our_list.copy()
        new_list.remove(elem)
        if elem in new_list:
            return False
    return True


user_list = [1, 2, 3, 4, 5, 6]
print(have_dupl(user_list))
