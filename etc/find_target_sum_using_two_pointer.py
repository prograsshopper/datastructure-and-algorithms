"""
투포인터
- 정렬된 배열에서 두 개의 포인터를 이용하여 해당 값들과 원하는 값들을 비교한 뒤 포인터를 조작하여 원하는 결과를 얻어내는 기법

배열내 합이 S가 되는 순서쌍 찾기
- 만약 루프중첩으로 하면 n^2 시간이 걸리나 투포인터를 쓰면 nlogn의 시간안에 해결이 가능하다.

두 포인터를 이용하여 양 끝지점을 가리키게 한다.
왼쪽의 포인터를 l, 오른쪽의 포인터를 r이라고 하고 l <= r 을 만족하는 동안 다음의 작업을 반복한다.

- 두 개의 포인터가 가리키고 있는 원소의 합이 S보다 큰 경우 r을 감소시킨다.
- 두 개의 포인터가 가리키고 있는 원소의 합이 S보다 작은 경우 l을 증가시킨다.
- 두 개의 포인터가 가리키고 있는 원소의 합이 S와 같다면 l을 증가시키고 r을 감소시키거나 작업을 종료한다.
"""

def get_sum_with_two_pointer(sorted_arr, target_sum):
    l = 0
    r = len(sorted_arr) - 1
    result = 0

    while l <= r:
        current_sum = sorted_arr[l] + sorted_arr[r]
        if target_sum > current_sum:
            l += 1
        elif target_sum < current_sum:
            r -= 1
        else:
            result += 1
            l += 1
            r -= 1
    return result

if __name__ == "__main__":
    arr = [2, 5, 8, 7, 10, 3, 9, 10, 11, 13, 12]
    arr.sort()
    target = 15
    ans = get_sum_with_two_pointer(arr, 15)
    print(ans)
