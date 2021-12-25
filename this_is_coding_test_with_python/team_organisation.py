import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def solve():
    n, m = map(int, input().rstrip().split())
    
    parent = [i for i in range(n + 1)]

    result = []

    for _ in range(m):
        o, a, b = map(int, input().rstrip().split())

        if o == 0:
            union(parent, a, b)
        else:
            if find_parent(parent, a) == find_parent(parent, b):
                result.append('YES')
            else:
                result.append('NO')

    for r in result:
        print(r)

if __name__ == '__main__':
    solve()

# 이것이 코딩테스트다 with Python 실전문제 10-7 문제 (팀 결성)
# P. 298

# 서로소 집합 자료구조를 이용하여 푸는 문제이다.
# 사실 서로소 집합 자료구조를 사용할줄 아는지를 묻는 문제라서 너무 어거지로 만들지 않았나 싶지만
# 아무튼 서로 집합 자료구조의 find parent와 union parent만 제대로 할 줄 안다면
# 간단한 문제이다.

# 서로소 집합 자료구조를 이용하면 싸이클을 판별할수있어서 최소신장트리문제를 풀 수 있기때문에
# 최소신장트리문제를 풀기위한 연습문제라고 생각하면 될듯하다.
# 코딩 테스트에서 이런문제는 아마도 안 나올듯?
