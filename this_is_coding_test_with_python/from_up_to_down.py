n = int(input())

array = [int(input()) for _ in range(n)]

array.sort(reverse = True)

for i in array:
    print(i, end = ' ')

# 이것이 코딩테스트다 with Python 실전문제 6-10 문제 (위에서 아래로)
# P. 178

# 정말 기본적인 정렬알고리즘을 사용할 수 있는지 보는 문제 같지도 않은 문제이다.
# 내림차순 정렬을 요구 했기에 파이썬 기본 정렬 알고리즘을 사용하되 reverse 매개변수의
# 인자를 True로 주면 된다.
