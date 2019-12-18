# https://app.codesignal.com/interview-practice/topics/arrays
def firstDuplicate(a):
    find_dict = {num:0 for num in a}
    for num in a:
        if find_dict[num] != 0:
            return num
        find_dict[num] += 1
    return -1