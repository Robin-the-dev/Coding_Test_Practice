from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

counts = [[0] * m for _ in range(n)]
q = deque()
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

q.append((0, 0))
counts[0][0] = 1

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx <= n - 1 and 0 <= ny <= m - 1 and maze[nx][ny] == 1:
            if counts[nx][ny] == 0:
                q.append((nx, ny))
                counts[nx][ny] = counts[x][y] + 1

print(counts[n - 1][m - 1])

# 이것이 코딩테스트다 with Python 실전문제 5-11 문제 (미로 탈출)
# P. 152

# 최단거리를 찾아야하는 문제이므로 BFS를 사용하는 것이 적절하다.
# 왜냐하면 BFS는 각 노드들의 최적의 해를 항상 찾아주기 때문이다.
# DFS/BFS 문제는 둘 중에 그냥 원하는 것을 사용하면 된다고 생각했는데
# 많은 문제가 둘 중 어떤 것을 이용하던 잘 풀리지만 특정 문제,
# 예를 들어 위와 같은 최단거리를 찾는 문제는 BFS롤 풀어야하고
# 아직 풀어보지 못했지만 백트랙킹 문제는 DFS를 사용해야 한다고 한다.

# (백트랙킹이 뭔지는 아직 모르겠지만 이 단어를 그대로 해석해봤을때 
# 순회를 하고 돌아가면서 무언가를 해야하는것 같아서 stack을 이용하는
# DFS로 풀 수 있을것이라고 예상해본다.)

# 처음에는 왜 DFS로 풀 수 없는지 이해를 못해서 구글링도 해보고
# 결국 잘 이해가 안가서 DFS로 구현해보려 했는데 코드를 짜면서 느낀게
# DFS는 무조건 제일 깊게부터 탐색을 하기때문에 최단거리를 찾을때는
# 항상 최적의 해를 주지 않아서 적절치 않다고 느꼈다.
# (이게 무슨말이냐면 DFS가 최적의 해를 주는 경우는 내가 찾으려는 노드의 최단거리가
# 그 그래프에서 제일 깊어야만 최적의 해를 준다.)
