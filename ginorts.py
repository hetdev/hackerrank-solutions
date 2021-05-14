n = list(input())
lowers = []
uppers = []
nums_odd = []
nums_even = []
nums_zeros = []
for word in n:
    if word.islower():
        lowers.append(word)
    elif word.isupper():
        uppers.append(word)
    else:
        if int(word) % 2 == 0:
            nums_even.append(str(word))
        elif int(word) == 0:
            nums_zeros.append(str(word))
        else:
            nums_odd.append(str(word))
str_answer = "".join(
    sorted(lowers)
    + sorted(uppers)
    + sorted(nums_odd)
    + sorted(nums_zeros)
    + sorted(nums_even)
)
print(str_answer)
