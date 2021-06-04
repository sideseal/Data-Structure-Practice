INF = 999
adj_mat = [
    [0, 29, INF, INF, INF, 10, INF],
    [29, 0, 16, INF, INF, INF, 15],
    [INF, 16, 0, 12, INF, INF, INF],
    [INF, INF, 12, 0, 22, INF, 18],
    [INF, INF, INF, 22, 0, 27, 25],
    [10, INF, INF, INF, 27, 0, INF],
    [INF, 15, INF, 18, 25, INF, 0],
]

node_num = len(adj_mat)
visited = [False] * node_num
distances = [INF] * node_num


def get_min_node(node_num):
    for i in range(node_num):
        if not visited[i]:
            v = i
            break
    for i in range(node_num):
        if not visited[i] and distances[i] < distances[v]:
            v = i
    return v


def prim(start, node_num):
    for i in range(node_num):
        visited[i] = False
        distances[i] = INF

    distances[start] = 0
    for i in range(node_num):
        node = get_min_node(node_num)
        visited[node] = True

        for j in range(node_num):
            if adj_mat[node][j] != INF:
                if not visited[j] and adj_mat[node][j] < distances[j]:
                    distances[j] = adj_mat[node][j]

        print(distances)


prim(0, node_num)
print("distances: ", distances)
print("cost: ", sum(distances))