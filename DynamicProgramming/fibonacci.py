# dp를 사용한 피보나치
# 상향식
def get_target_fibo_bottomup(target_num):
    from collections import defaultdict
    fibo_dic = defaultdict(lambda: 1)
    current_num = 3
    while current_num <= target_num:
        fibo_dic[current_num] = fibo_dic[current_num-1] + fibo_dic[current_num-2]
        current_num += 1
    return fibo_dic[target_num]

def get_target_fibo_topdown(target_num):
    fibo = {}
    
    for i in range(1, target_num+1):
        if i == 1 or i == 2:
            fibo[i] = 1
        else:
            fibo[i] = fibo[i - 1] + fibo[i - 2]
    return fibo[target_num]


if __name__ == "__main__":
    target = 7
    first_ans = get_target_fibo_bottomup(target)
    print(first_ans)
    second_ans = get_target_fibo_topdown(target)
    print(second_ans)


