# 1번

from collections import deque


def bfs(x, y, ox, oy, V):
    q = deque()
    L = len(V)
    V[x][y] = 1
    s = 0
    q.append((x, y, s))
    nx = [-2, -1, 1, 2, -2, -1, 1, 2]
    ny = [-1, -2, -2, -1, 1, 2, 2, 1]
    while len(q) > 0:
        x, y, s = q.popleft()
        if (x, y) == (ox, oy):
            print(s)
            return
        for i in range(8):
            mx, my = x+nx[i], y+ny[i]
            if (mx < 0 or my < 0 or mx >= L or my >= L):
                continue
            if not V[mx][my]:
                V[mx][my] = 1
                q.append((mx, my, s+1))


l, cx, cy, ox, oy = map(int, input().split())
V = [[0 for _ in range(l)] for _ in range(l)]
bfs(cx, cy, ox, oy, V)

# 2번

from collections import deque


def bfs(X, D):
    V = [0] * (10 ** 5 + 1)
    dq = deque([X])
    while dq:
        n = dq.popleft()
        if D == n:
            print(V[n])
            break
        for i in (n-1, n+1, 2*n):
            if 0 <= i <= (10 ** 5) and not V[i]:
                V[i] = V[n] + 1
                dq.append(i)


X, D = map(int, input().split())
bfs(X, D)

# 3번

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]


def dfs(x, y):
    global c
    if x < 0 or x > N-1 or y < 0 or y > N-1:
        return False
    else:
        if G[x][y] == 1:
            G[x][y] = 0
            c += 1
            dfs(x-1, y)
            dfs(x, y-1)
            dfs(x+1, y)
            dfs(x, y+1)
            return True
    return False


r = 0
c = 0
C = []
for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            r += 1
            C.append(c)
            c = 0
print(r, max(C))
