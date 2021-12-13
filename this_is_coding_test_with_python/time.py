n = int(input())
result = 0
ms_count = 0

for m in range(60):
    for s in range(60):
        # 시, 분을 아래와 같이 따로 작성을 해서 or를 해도되고
        # 더 간단하게 
        # if '3' in str(m) + str(s):
        # 로 작성 할 수 있다.
        if '3' in str(m) or '3' in str(s):
            ms_count += 1

for h in range(n + 1):
    if '3' in str(h):
        result += 60 * 60
    else:
        result += ms_count

print(result)

# 이것이 코딩테스트다 with Python 예제 4-2 문제 (시각)
# P. 113

# 정말 간단한 구현문제이다.
# 책에서는 시, 분, 초를 한번에 묶어 삼중 반복문으로 작성을 했는데
# 나처럼 분, 초만 묶어서 이중 반복문으로 돌린다면 삼중보다는 
# 더 빠르지 않을까는 생각을 해본다.
# 어차피 하루는 86,400초로 삼중 반복문을 해도 별 문제 없다만...
