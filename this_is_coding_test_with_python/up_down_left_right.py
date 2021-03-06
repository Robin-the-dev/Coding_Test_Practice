n = int(input())
# 문자들을 받아 리스트안에 넣는 코드를 아래와 같이 썼는데
# plans = list(map(str, input().split()))
plans = input().split()
# 어차피 input() 함수로 입력받는 것은 문자로 처리 되기때문에
# 위의 코드처럼 간단하게 쓰면 된다.

x = 1
y = 1

for plan in plans:
    if plan == 'U':
        if x > 1:
            x -= 1
    elif plan == 'D':
        if x < n:
            x += 1
    elif plan == 'L':
        if y > 1:
            y -= 1
    elif plan == 'R':
        if y < n:
            y += 1

print(x, y)

# 이것이 코딩테스트다 with Python 예제 4-1 문제 (상하좌우)
# P. 111

# 책에서 제일 처음 나오는 구현문제답게 정말 간단한 문제이다.
# 간단한 만큼 크게 문제에 대해 언급할 것 없이 문제대로 
# 구현하면 되는 문제이다.
# 하지만 구현 문제인 만큼 문제를 꼼꼼히 읽어야하는게
# 상하좌우로 이동하는 계획대로 이동을 한 후 x와 y좌표를 구해야하는데
# 문제에서 명시되어있듯이 왼쪽위가 (1, 1)좌표이고 오른쪽아래가 (n, n)좌표이다.
# 흔히 수학에서는 위쪽 수직선이 y축, 오른쪽 수평선이 x축이고 위나 오른쪽으로 
# 갈때마다 +가 되고 반대쪽으로 이동하면 -가 되는데
# 컴퓨터 프로그래밍으로 2차원 배열을 만들면 그래프 모양이 문제와 같은 모양으로 나온다.

# 왜냐하면 길이가 5인 2차원 배열을 만들었다고 했을때
# [
#     [1, 0, 0, 0, 0],
#     [2, 3, 0, 0, 0],
#     [0, 4, 5, 0, 0],
#     [0, 0, 6, 7, 0],
#     [0, 0, 0, 8, 9],
# ]
# 위와 같은 모양으로 생성이 되는데 
# 숫자 1에 접근하려면 [0][0]으로 접근해야하고
# 숫자 2에 접근하려면 [1][0]으로 접근해야하고
# 숫자 3에 접근하려면 [1][1]으로 접근해야한다.
# 이처럼 수학의 그래프처럼 왼쪽밑이 (0, 0)이 아닐뿐더러
# 2차원 배열의 특성상 그래프의 접근법이 수학 그래프랑 다르다는 것을 명심해야 된다.

# y축
# |
# |
# |   이것이 수학 그래프
# |
# |
# |
# |_____________x축
#
##################################
# ______________y축
# |
# |
# |
# |   이것이 2차원 배열의 그래프
# |
# |
# |
# x축


