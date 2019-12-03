# https://programmers.co.kr/learn/courses/30/lessons/42588

def solution(heights):
    answer = [0]
    for i in range(1, len(heights)):
        current = heights[i]
        find = False
        for j in range(i, -1, -1):
            if current < heights[j]:
                answer.append(j+1)
                find = True
                break
        if not find:
            answer.append(0)
    return answer