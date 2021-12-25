import sys
input = sys.stdin.readline
INF = int(1e9)

def solve():
    n, m = map(int, input().rstrip().split())
    edges = [tuple(map(int, input().rstrip().split())) for _ in range(m)]
    x, k = map(int, input().rstrip().split())

    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(len(graph)):
        for j in range(len(graph)):
            if i == j:
                graph[i][j] = 0

    for edge in edges:
        graph[edge[0]][edge[1]] = 1
        graph[edge[1]][edge[0]] = 1

    for j in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][j] + graph[j][b])

    result = graph[1][k] + graph[k][x]
    
    if result >= INF:
        print(-1)
    else:
        print(result)

def revise():
    n, m = map(int, input().rstrip().split())
    roads = [tuple(map(int, input().rstrip().split())) for _ in range(m)]
    x, k = map(int, input().rstrip().split())

    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0

    for road in roads:
        graph[road[0]][road[1]] = 1
        graph[road[1]][road[0]] = 1

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    
    result = graph[1][k] + graph[k][x]
    
    print(-1) if result >= INF else print(result)

if __name__ == '__main__':
    solve()
    revise()

# 이것이 코딩테스트다 with Python 실전문제 9-4 문제 (미래도시)
# P. 259

# 최단 경로를 찾는 문제이다.
# 1번 노드에서 k번 노드를 거쳐 x번 노드를 갈때의 최단거리를 찾으면 된다.
# 다익스트라 알고리즘으로 1번에서 k번 노드로 한번 찾고 k번에서 x번 노드로 가는 최단거리를 찾아서
# 더해도 되지만 n이 100이하이기 때문에 플로이드 워셜 알고리즘으로 풀어도 충분히 빠르게 풀 수 있다.

# 플로이드 워셜 알고리즘이 구현도 어렵지않고 간단하기때문에 문제 자체는 간단하지만
# 문제에서 입력으로 두 노드간의 간선이 양방향으로 적용된다고 언급되어 있었는데
# 이 부분을 깜빡하고 단방향으로만 적용을 시켜버렸다. (19번째 줄을 코드로 넣지 않았음)
# 문제를 꼭 제대로 읽고 코드로 구현하자!!!
