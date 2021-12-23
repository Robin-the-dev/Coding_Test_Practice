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

if __name__ == '__main__':
    solve()
