# https://www.hackerrank.com/challenges/sparse-arrays/problem

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
# 다른 사람들의 풀이를 보니 dict를 많이 썻던데 이건 인터뷰킷이 아니라 array 문제니까 array만 사용해야하는게 아닌가 하는 생각...
# 역시 collection이 능률을 오르게 해주는것같은데 collection 공부 필요함
def matchingStrings(strings, queries):
    count_list = [0 for i in range(0,len(queries))]
    for idx in range(0, len(queries)):
        for string in strings:
            if queries[idx] == string:
                count_list[idx] += 1
    return count_list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
