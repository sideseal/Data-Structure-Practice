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


t = int(input())
for i in range(t):
    l = int(input())
    cx, cy = map(int, input().split())
    ox, oy = map(int, input().split())
    V = [[0 for _ in range(l)] for _ in range(l)]
    bfs(cx, cy, ox, oy, V)
