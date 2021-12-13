n, m = map(int, input().split())
x, y, d = map(int, input().split())
game_map = [list(map(int, input().split())) for _ in range(n)]
visited = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 0
visited.append([x, y])

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

while True:
    turn_left()

    to_x = dx[d] + x
    # 아래부분의 dy[d]를 dx[d]로 오타가 나버리는 바람에 한참을 해맸다.
    to_y = dy[d] + y

    if game_map[to_x][to_y] != 1 and [to_x, to_y] not in visited:
        x = to_x
        y = to_y
        visited.append([x, y])
        count = 0
        continue
    else:
        count += 1

    if count == 4:
        count = 0
        back_x = x - dx[d]
        back_y = y - dy[d]

        if game_map[back_x][back_y] == 1:
            break
        else:
            x = back_x
            y = back_y

print(len(visited))

# 이것이 코딩테스트다 with Python 실전문제 4-4 문제 (게임 개발)
# P. 118

# 앞서 풀어본 문제와 같이 구현문제이지만 요구사항이 조금 더 있는
# 난이도가 조금 올라간 문제이다.
# 사실 거의 다 풀었는데 오타와 깜빡해버린 요구사항이 있어서 제대로 풀리지 않았다.
# 구현문제를 풀때는 요구사항을 제대로 읽고 오타를 조심해가면서 차근차근 풀어야겠다고
# 생각이 들었다.
# 급하게 빨리 풀겠다고 double check 하지 않으면서 풀면 오히려 차근차근 푸는 것 보다
# 더 오래 걸리니 꼭 요구사항을 제대로 읽고 차근차근 풀 수 있도록 하자!

# 이 문제와 같이 일반적으로 방향을 설정해서 이동하는 문제 유형에서는
# dx, dy라는 별도의 리스트를 만들어 방향을 정하는 것이 효과적으로 구현이 가능하다.
