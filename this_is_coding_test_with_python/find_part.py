# import sys
# 
# input = sys.stdin.readline
# 
# n = int(input().rstrip())
# parts = list(map(int, input().rstrip().split()))
# m = int(input().rstrip())
# reqs = list(map(int, input().rstrip().split()))
# 
# parts.sort()
# 
# def binary_search(s, e, t, a):
#     if s > e:
#         return 'no'
# 
#     mid = (s + e) // 2
# 
#     if a[mid] == t:
#         return 'yes'
#     elif a[mid] > t:
#         # return문을 꼭 까먹지말자!
#         return binary_search(s, mid - 1, t, a)
#     elif a[mid] < t:
#         # 여기도 마찬가지!
#         return binary_search(mid + 1, e, t, a)
# 
# if __name__ == '__main__':
#     for req in reqs:
#         print(binary_search(0, len(parts) - 1, req, parts), end = ' ')

# 이것이 코딩테스트다 with Python 실전문제 7-5 문제 (부품 찾기)
# P. 197

# 이진 탐색파트에서 나온 문제긴 하지만 여러 방법으로 효율적으로 풀 수 있다.
# 일단은 이진 탐색을 배우고 있기때문에 이진탐색으로 풀어보았다.
# 이진 탐색으로 풀 경우에 시간 복잡도는 O((n + m) * log n) 이 된다.
# (왜냐하면 parts 리스트를 정렬해주어야 하기때문이다.)
# 또 맞왜틀이 나와버렸는데 이진 탐색 구현할때 elif 부분에서 안에 내용을 return 해주지 않았다.
# 정말 초보적인 실수였고 다시는 하면안될 실수이다.
# 재귀를 이용해 로직을 구현할때는 한번더 다시 생각해보자!

# 또 다르게 풀 수 있는 방법으로는 계수 정렬과 set이나 dictionary를 이용하는 방법이 있다.
# 계수정렬
# import sys
# 
# input = sys.stdin.readline
# 
# n = int(input().rstrip())
# # n개의 정수는 백만보다 작거나 같기때문에 계수 정렬에 이용할 리스트를 백만한개로 만들어준다.
# counting_sort = [0] * 1000001
# 
# # 만약 있는 부품이면 해당 인덱스로 접근을 해서 1로 바꾸어준다.
# for i in input().rstrip().split():
#     counting_sort[int(i)] = 1
# 
# m = int(input().rstrip())
# reqs = list(map(int, input().rstrip().split()))
# 
# if __name__ == '__main__':
#     for req in reqs:
#         if counting_sort[req] == 1:
#             print('yes', end = ' ')
#         else:
#             print('no', end = ' ')

# n개의 정수가 입력받아 질때 정수는 1보다 크고 1,000,000 이하이기때문에 계수 정렬을 사용 할 수 있다.
# (계수 정렬은 데이터의 차이값이 백만이하일때 사용 할 수 있다. 차이가 너무 크면 메모리를 많이 잡아먹기때문에
# 사용하기 어렵다.)
# 구현은 보다시피 간단하다.

# set으로 구현
import sys

input = sys.stdin.readline

n = int(input().rstrip())
# list가 아니라 set안에 집어넣기
parts = set(map(int, input().rstrip().split()))
m = int(input().rstrip())
reqs = list(map(int, input().rstrip().split()))

if __name__ == '__main__':
    # set에서의 검색의 시간복잡도는 O(1)이기 때문에 매우 빠르다.
    for req in reqs:
        if req in parts:
            print('yes', end = ' ')
        else:
            print('no', end = ' ')

# 해쉬 테이블을 사용하는 set이기 때문에 반복문을 돌려서 in 연산자를 써도 list에 비해 굉장히 빠르기 때문에
# 이런 방법도 사용할 수 있다.
# 해쉬 테이블을 쓰는 dictionary도 똑같이 사용 할 수 있을듯하다.
