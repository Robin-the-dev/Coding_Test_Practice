# from collections import deque
# 
# n, m = map(int, input().split())
# 
# tray = [input() for _ in range(n)]
# q = deque()
# dx = (-1, 1, 0, 0)
# dy = (0, 0, -1, 1)
# result = 0
# visited = [[False] * m for _ in range(n)]
# 
# for i in range(n):
#     for j in range(m):
#         if tray[i][j] == '0' and not visited[i][j]:
#             visited[i][j] = True
#             q.append((i, j))
#             result += 1
# 
#             while q:
#                 top = q.popleft()
#                 for k in range(4):
#                     nx = top[0] + dx[k]
#                     ny = top[1] + dy[k]
#                     if 0 <= nx <= n - 1 and 0 <= ny <= m - 1:
#                         if tray[nx][ny] == '0' and not visited[nx][ny]:
#                             visited[nx][ny] = True
#                             q.append((nx, ny))
# 
# print(result)

# 이것이 코딩테스트다 with Python 실전문제 5-1 문제 (음료수 얼려 먹기)
# P. 149

# DFS/BFS 문제이다.
# DFS나 BFS로 풀 수 있다고 생각만 되어지면 구현만 숙달되면 복잡해보이지만 간단하게 풀 수 있는 문제이다.
# 계속해서 DFS/BFS 문제를 풀어보며 구현에 익숙해지면 좋을 것 같다.
# 위에 쓴 코드는 BFS로 구현했고 재귀함수를 이용해 DFS를 풀면 코드가 더 간결해질것이다.
# 그리고 tray 변수 (얼음틀)을 받을때 정수화 시키지않고 문자열 그대로 받았는데
# 파이썬에서는 문자열은 indexing을 통해 새로운 값을 대입시킬 수 없기때문에 추가적으로 방문 여부를 확인하는
# visited 2차원 리스트를 만들었다.
# visited 리스트 없이 하려면 tray 변수의 값을 문자열으로 받은것을 정수화 시켜주면 된다.

# 아래는 DFS 구현

n, m = map(int, input().split())
tray = [list(map(int, input())) for _ in range(n)]
result = 0

def dfs(x, y):
    global tray
    if not (0 <= x <= n - 1) or not (0 <= y <= m - 1):
        return
    if tray[x][y] == 1:
        return
    
    tray[x][y] = 1

    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)

for i in range(n):
    for j in range(m):
        if tray[i][j] == 0:
            result += 1
            dfs(i, j)

print(result)
