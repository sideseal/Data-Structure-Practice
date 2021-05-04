# adjacency list (set)
a,b,c,d,e,f = range(6)
N = [{b,c,d,f}, {a,d,f}, {a,b,d,e}, {a,e}, {a,b,c}, {b,c,d,e}]
print("\n"+"인접리스트(set): ",N)
print("인접리스트(set) 첫 번째 노드의 2 포함 유무:",b in N[a])
print("인접리스트(set) 두 번째 노드의 2 포함 유무:",b in N[b])
print("인접리스트(set) 6 번째 노드의 길이:",len(N[f]))

# adjacency list (list)
a,b,c,d,e,f = range(6)
N = [[b,c,d,f], [a,d,f], [a,b,d,e], [a,e], [a,b,c], [b,c,d,e]]
# 삭제하려는 객체를 맨 마지막으로 이동 후 pop을 하면 O(1)의 시간으로 단축 가능하다.

# adjacency list (dict)
a,b,c,d,e,f = range(6)
N = [{b:2,c:1,d:4,f:1}, {a:4,d:1,f:4}, {a:1,b:1,d:2,e:4}, {a:3,e:2}, {a:3,b:4,c:1}, {b:1,c:2,d:4,e:3}]
print("\n"+"인접리스트(dict): ",N)
print("인접리스트(dict) 첫 번째 노드의 2 포함 유무:",b in N[a])
print("인접리스트(dict) 6 번째 노드의 길이:",len(N[f]))
print("인접리스트(dict) 첫 번째 노드의 2 멤버쉽의 가중치:", N[a][b])

# adjacency list (dict): weight
a,b,c,d,e,f = range(6)
N = { 'a':set('bcdf'), 'b':set('adf'), 'c':set('abde'), 'd':set('ae'), 'e':set('abc'), 'f':set('bcde')}
'b' in N['a'] # True

# adjacent matrix
a,b,c,d,e,f = range(6)
N = [[0,1,1,1,0,1], [1,0,0,1,0,1], [1,1,0,1,1,0], [1,0,0,0,1,0], [1,1,1,0,0,0], [0,1,1,1,1,0]]
print("\n"+"인접행렬:",N)
print("인접행렬 첫 번째 노드의 2 포함 유무:",bool(N[a][b]))
print("인접행렬 첫 번째 노드의 5 포함 유무:",bool(N[a][e]))
print("인접행렬 6 번째 노드의 길이:",sum(N[f]))

# adjacent matrix: weight
_ = float('inf') # None, -1 ...
N = [[_,2,1,4,_,1], [4,_,_,1,_,4], [1,1,_,2,4,_], [3,_,_,_,2,_], [3,4,1,_,_,_], [1,2,_,4,3,_]]
print("\n"+"인접행렬:",N)
print("인접행렬 첫 번째 노드의 2 멤버쉽의 가중치:",N[a][b])
print("인접행렬 첫 번째 노드의 2 포함 유무:",N[a][b] < _)
print("인접행렬 6 번째 노드의 길이:",sum(1 for w in N[f] if w < _))