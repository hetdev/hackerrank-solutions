from itertools import combinations, combinations_with_replacement

word, size = input().split()
words_list = list(combinations_with_replacement(sorted(word), int(size)))
for word_l in words_list:
    print("".join(word_l))
