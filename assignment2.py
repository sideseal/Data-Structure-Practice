# 1
N, M = map(int, input().split())
D = dict()
for i in range(N + 1):
    D[i] = [i]
for j in range(M):
    c, a, b = map(int, input().split())
    if c == 0:
        D[a].extend(D[b])
        D[b].extend(D[a])
        # 중복 제거
        tmpset = set(D[a])
        D[a] = list(tmpset)
        tmpset = set(D[b])
        D[b] = list(tmpset)
    elif c == 1:
        if b in D[a]:
            print("O")
        else:
            print("X")

# 2
N = int(input())
arr = []
M = int(input())
for i in range(M):
    a, b, c = map(int, input().split())
    arr.append([a, b, c])

arr.sort(key=lambda x: x[2])
routes = set([arr[0][0], arr[0][1]])
cost = arr[0][2]

while N != len(routes):
    for i, j in enumerate(arr[1:]):
        if j[0] in routes and j[1] in routes:
            continue

        if j[0] in routes or j[1] in routes:
            routes.update([j[0], j[1]])
            cost += j[2]
            arr[i + 1] = [-1, -1, -1]
            break

print(cost)

# 3
class Min_Heap:
    def __init__(self):
        self.array = []

    def __str__(self):
        return str(self.array)

    def insertElement(self, data):
        self.array.append(data)
        length = len(self.array)
        if length > 1:
            node_num = length - 1
            while True:
                next_node_num = int(node_num // 2)
                if self.array[next_node_num] > self.array[node_num]:
                    tmp = self.array[node_num]
                    self.array[node_num] = self.array[next_node_num]
                    self.array[next_node_num] = tmp
                else:
                    break
                node_num = int(node_num // 2)
                if node_num == 0:
                    break

    def deleteRoot(self):
        length = len(self.array)
        if length < 1:
            return -1

        root_value = self.array[0]
        del self.array[0]

        last_index = len(self.array) - 1
        if last_index < 0:
            return root_value
        tail_value = self.array[last_index]
        del self.array[last_index]

        self.array.insert(0, tail_value)
        now_index = 0
        next_index = 0
        while True:
            now_index = next_index
            next_index *= 2
            if next_index + 2 > last_index:
                if (
                    len(self.array) == 2
                    and self.array[now_index] > self.array[now_index + 1]
                ):
                    tmp = self.array[now_index]
                    self.array[now_index] = self.array[now_index + 1]
                    self.array[now_index + 1] = tmp
                break
            if self.array[next_index + 1] < self.array[next_index + 2]:
                next_index += 1
            else:
                next_index += 2
            if self.array[now_index] > self.array[next_index]:
                tmp = self.array[now_index]
                self.array[now_index] = self.array[next_index]
                self.array[next_index] = tmp

        return root_value


m_heap = Min_Heap()
N = int(input())
for i in range(N):
    M = int(input())
    if M == 0:
        print(m_heap.deleteRoot())
    else:
        m_heap.insertElement(M)