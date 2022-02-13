def find_parent(parent, x):
    # 루트 노드 아니면 재귀적 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def make_union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int, input().split())
parent = [0] * (V + 1)

edges = []

for i in range(V + 1):
    parent[i] = i

for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append([C, A, B])


edges.sort()
count = 0
answer = 0

for edge in edges:
    if count == (V-1):
        break

    C,A,B = edges.pop(0)

    if find_parent(parent, A) != find_parent(parent, B):
        make_union(parent, A, B)
        count += 1
        answer += C
        
print(answer)