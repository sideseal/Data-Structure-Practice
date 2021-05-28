# Kruskal Using disjoint set

parent = dict()
rank = dict()

# path compression
def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


# union-by-rank
def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def make_set(node):
    parent[node] = node
    rank[node] = 0


def kruskal(graph):
    mst = list()

    for node in graph["vertices"]:
        make_set(node)

    edges = graph["edges"]
    edges.sort()

    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)

    return mst


graph = {
    "vertices": ["A", "B", "C", "D", "E"],
    "edges": [
        (7, "A", "B"),
        (5, "A", "D"),
        (7, "B", "A"),
        (5, "D", "A"),
        (8, "B", "C"),
        (8, "C", "B"),
        (9, "B", "D"),
        (9, "D", "B"),
        (8, "C", "B"),
        (5, "C", "E"),
        (5, "E", "C"),
        (7, "E", "D"),
        (7, "D", "E"),
    ],
}

print(kruskal(graph))
print(parent)
print(rank)