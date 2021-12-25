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

def solve2():
    n, m = map(int, input().rstrip().split())

    routes = []

    for _ in range(m):
        a, b, c = map(int, input().rstrip().split())

        routes.append((c, a, b))

    routes.sort(key = lambda x: x[0])

    parent = [i for i in range(n + 1)]

    result = 0
    count = 0

    for route in routes:
        cost, start, dest = route

        if find_parent(parent, start) != find_parent(parent, dest):
            union_parent(parent, start, dest)
            result += cost
            count += 1

        if count == n - 2:
            break

    print(result)

if __name__ == '__main__':
    solve()
    solve2()

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

# solve2 함수에 더 빨리 구현 할 수 있도록 다시 풀어 보았다.
# 최소 신장 트리의 간선의 갯수는 항상 노드 - 1개 이므로
# 아무리 m을 많이 입력받아도 항상 n - 1번만 반복하면 되므로 count 변수를 만들어서
# 한번 간선을 추가 할때마다 1을 더해줘서 때가되면 반복문을 나오게끔 해줬다.

# 하지만 이 문제에서는 마을을 두개로 나누기때문에 제일 큰 간선을 하나 빼줌으로써 유지비를 최소로 들이면서
# 마을을 두개로 나눌 수 있다.
# 최소 신장 트리 알고리즘을 쓸때 가장 큰 가중치를 가진 간선은 마지막에 추가 되기 때문에
# solve 함수에서 한 것 처럼 나온 결과 값에서 제일 큰 가중치를 가진 간선을 빼주는게 아니라
# 단순히 n - 2번을 반복하면 제일 큰 가중치를 가진 간선을 제외하고 계산이 된다.
# 이렇게 하면 더 빨리 효율적으로 코드를 짤 수 있고
# 간선을 정렬 할 때도 람다 함수를 이용해서 가중치에 대해서만 정렬을 하게 되면
# 더 빨리 정렬이 되기 때문에 굳이 다른 값에 대해서도 정렬에 염두에 둘 필요가 없으면
# 람다 함수를 이용해서 가중치에 대해서만 정렬하도록 하자!!! (57번째 줄 참고)
