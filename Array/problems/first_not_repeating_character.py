# https://app.codesignal.com/interview-practice/topics/arrays

from collections import OrderedDict

def firstNotRepeatingCharacter(s):
    find_dict = OrderedDict({alpha:0 for alpha in s})
    
    for alpha in s:
        try:
            if find_dict[alpha] >= 1:
                del find_dict[alpha]
                continue
        except:
            continue
        find_dict[alpha] += 1
    
    if find_dict:
        return find_dict.popitem(last=False)[0]
    return '_'