# n = input()
# 
# col = {}
# a = ord('a')
# 
# for i in range(1, 9):
#     col[chr(a + i - 1)] = i
# 
# x = int(n[1])
# y = col[n[0]]
# moves = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
# result = 0
# 
# for move in moves:
#     n_x = x + move[0]
#     n_y = y + move[1]
#     if 1 <= n_x <=8 and 1 <= n_y <=8:
#         result += 1
# 
# print(result)

# 이것이 코딩테스트다 with Python 예제 4-3 문제 (왕실의 나이트)
# P. 115

# 또 다른 간단한 구현 문제이다.
# 구현 문제답게 문제의 내용을 꼼꼼히 읽고 코드로 잘 구현해내면 된다.
# 지금의 문제에서는 입력값이 a1 같이 열과 행의 순서로 입력되는데
# 조금 문제를 까다롭게 출제한다면 입력값으로 a1같이 뿐만아니라
# 1a와 같이 입력되어도 똑같이 작동하게끔 만들어라고 할 수 있다고 한다.
# 아래는 입력값을 a1도 1a와 같이도 받을수 있게끔 만든 것이다.

n = input()

# 위에 처음 푼 코드에서는 a부터 h까지 해당하는 값을 반복문으로 dictionary를 만들어서
# y값을 찾았는데 아래처럼 한다면 더 간단하게 dictionary 없이 찾을 수 있다.
if ord('a') <= ord(n[0]) <= ord('h'):
    x = int(n[1])
    y = ord(n[0]) - ord('a') + 1
else:
    x = int(n[0])
    y = ord(n[1]) - ord('a') + 1

moves = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
result = 0

for move in moves:
    n_x = x + move[0]
    n_y = y + move[1]
    if 1 <= n_x <=8 and 1 <= n_y <=8:
        result += 1

print(result)
