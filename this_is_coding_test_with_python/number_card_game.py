import math

n, m = map(int, input().split())
num_cards = [list(map(int, input().split())) for _ in range(n)]

maximum = -math.inf

for row_cards in num_cards:
    row_minimum = min(row_cards)
    if maximum < row_minimum:
        maximum = row_minimum

print(maximum)

# 이것이 코딩테스트다 with Python 실전문제 3-3 문제 (숫자 카드 게임)
# P. 96

# 이것 또한 간단한 그리디 알고리즘을 활용하는 문제이다.
# 이 문제를 푸는 아이디어는 각 행에서의 가장 작은 수들 중에서 가장 큰 수를 출력하는 것이다.
# min() 함수를 활용하면 간단하게 원하는 값을 도출 할 수 있다.
# 내가 쓴 코드는 for 문을 이용해서 먼저 num_cards라는 2차원 리스트를 만들고 난 후 또 for 문을 이용해서 각 리스트들의 가장 작은 수를 찾아나갔는데
# 굳이 for 문을 두번 쓸 필요 없이 리스트를 유저로 부터 바로 입력 받자마자 가장 작은 수를 바로 찾아서 변수에 저장 시켜놓으면 반복문을 한번만 사용할 수 있다.
# 즉, 
'''
for _ in range(n):
    row_num_cards = list(map(int, input().split()))
    row_minimum = min(row_num_cards)
    maximum = max(maximum, row_minimum)
'''
# 처럼 하면 반복문을 한번만 쓰면서 입력을 받고 바로 가장 작은 수를 찾는 프로세스를 진행한다.
