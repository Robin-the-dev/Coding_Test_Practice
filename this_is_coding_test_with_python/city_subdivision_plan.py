import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def solve():
    n, m = map(int, input().rstrip().split())

    routes = []

    for _ in range(m):
        a, b, c = map(int, input().rstrip().split())

        routes.append((c, a, b))

    routes.sort()

    parent = [i for i in range(n + 1)]

    result = 0
    max_cost = 0

    for route in routes:
        cost, start, dest = route

        if find_parent(parent, start) != find_parent(parent, dest):
            union_parent(parent, start, dest)
            result += cost
            # cost를 기준으로 오름차순 정렬을 했기때문에 굳이 max 함수를 쓸 필요없이
            # max_cost = cost 라고 해도 된다.
            max_cost = max(max_cost, cost)

    print(result - max_cost)

if __name__ == '__main__':
    solve()

# 이것이 코딩테스트다 with Python 실전문제 10-8 문제 (도시 분할 계획)
# P. 300

# 최소 신장 트리 문제이다.
# 앞에서 풀어본 서로소 집합 자료구조를 이용해서 사이클 여부를 확인해 나가면서 union 함수를 이용해서 
# union 연산을 해주면 된다.

# 처음에 문제를 잘못 이해해서 하나의 최소 신장 트리만 만들면 된다고 생각했는데
# 문제에서 마을을 두개로 나눈다고 했기 때문에 마을을 두개로 유지하면서 도로의 유지비를 최소로 들게 하는 방법은
# 먼저 최소 신장 트리를 모든 집들을 포함해서 구한 다음 최소 신장 트리를 구성하는 간선의 가중치 중에서
# 가장 큰 가중치를 빼면 마을이 두개로 나눠 지면서 최소 유지비를 구할 수 있다.

# 꼭 문제를 잘 읽고 원하는 바가 무엇인지 제대로 깨닫고 문제를 풀자!
# 빠른 시간안에 다 풀었는데 이 부분을 간과해서 틀린 답을 냈다. 꼭 문제를 제대로 읽자!!!
