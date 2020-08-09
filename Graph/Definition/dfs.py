# 인접 리스트로 구현
def dfs_list(start, graph, check_dic):
    s = list()
    if check_dic[start]:
        return
    print(start)
    check_dic[start] = True

    for i in range(0, len(graph[start])):
        dfs_list(graph[start][i], graph, check_dic)

# 인접 행렬로도 구현이 가능하다

if __name__ == "__main__":
    graph = {
        1: [2, 3, 4],
        2: [],
        3: [1, 4, 5],
        4: [1, 3, 5],
        5: [3, 4]
    }
    start = 1
    from collections import defaultdict
    check_dic = defaultdict(lambda: False)
    print("인접리스트로 구현")
    dfs_list(1, graph, check_dic)

