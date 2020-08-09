"""
예시
- 정점을 저장하고 거장된 정점 중 가장 먼저 저장된 정점을 선택하며 해당 정점에 대한 작업을 하는 과정을 들어보자.
* 이 방법은 큐 자료구조를 사용하여 구현이 가능하다.
"""

def dfs(start, graph):
    from collections import deque, defaultdict
    check_dic = defaultdict(lambda: False)
    q = deque()
    q.append(start)
    check_dic[start] = True

    while q:
        cur = q.popleft()
        print(cur)
        for elem in graph[cur]:
            if not check_dic[elem]:
                check_dic[elem] = True
                q.append(elem)

if __name__ == "__main__":
    graph = {
        1: [2, 3, 4],
        2: [1, 5],
        3: [1, 6],
        4: [1, 6],
        5: [2, 6],
        6: [3, 4, 5, 7],
        7: [6]
    }
    start = 1
    dfs(1, graph)
