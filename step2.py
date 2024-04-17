def longest_word_len1(our_words):
    word_len = 0
    longest_word = ''
    for word in words:
        w_l = len(word)
        if w_l > word_len:
            word_len = w_l
            longest_word = word
    return longest_word


def longest_word_len2(our_words):
    word_len = 0
    longest_word = ''
    i = 0
    while i < len(our_words):
        w_l = len(our_words[i])
        if w_l > word_len:
            word_len = w_l
            longest_word = our_words[i]
        i += 1
    return longest_word


words = ['aasd', 'bxvzxvzva', 'casfhiu', 'dasfa', 'dadadsae']
print(longest_word_len1(words))
print(longest_word_len2(words))

