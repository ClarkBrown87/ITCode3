def is_polindrom(our_str):
    our_str = our_str.lower()
    our_str = our_str.replace(' ', '')
    for i in range(int(len(our_str)/2)):
        if not (our_str[i] == our_str[-(i+1)]):
            return False
    return True


print(is_polindrom("город дорог"))
