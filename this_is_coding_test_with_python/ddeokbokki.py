import sys
import random
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

d = list(map(int, input().rstrip().split()))

def binary_search(d, s, e, m):
    mid = (s + e) // 2
    if s > e:
        return mid

    req = 0

    # 잘랐을때 나온 총합 계산
    for i in d:
        if i < mid:
            continue
        else:
            req += i - mid

    if req > m:
        return binary_search(d, mid + 1, e, m)
    elif req < m:
        return binary_search(d, s, mid - 1, m)
    else:
        return mid

def binary_search_loop(d, s, e, m):
    start = s
    end = e
    result = 0

    while start <= end:
        mid = (start + end) // 2

        total = 0

        for i in d:
            if i > mid:
                total += i - mid

        if total < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    return result

if __name__ == '__main__':
    d.sort()
    # while True:
    #     n = random.randrange(1, 1000001)
    #     m = random.randrange(1, 2000000001)
    #     d.clear()
    #     for _ in range(n):
    #         r = random.randrange(0, 1000000001)
    #         d.append(r)
    #     if sum(d) < m:
    #         continue
    #     print('running...')
    #     if binary_search(d, 0, max(d), m) != binary_search_loop(d, 0, max(d), m):
    #         break
            
    print(binary_search(d, 0, max(d), m))
    print(binary_search_loop(d, 0, max(d), m))

# 이것이 코딩테스트다 with Python 실전문제 7-8 문제 (떡볶이 떡 만들기)
# P. 201

# 제대로 된 이진탐색 문제이다. m의 범위가 20억이므로 이진탐색으로 풀지않으면
# 시간초과가 뜰 것이다.
# 이런 입력 조건을 잘 보고 어떤 알고리즘으로 풀어야 되는지 예상할 수 있다.
# 이 문제의 요구사항은 손님이 요청한 길이가 m일때 적어도 m만큼의 떡을 얻기 위해
# 절단기에 설정할 수 있는 높이의 최댓값을 구하라는 것이다.
# m만큼의 떡을 주기 위해 설정할 수 있는 높이가 여러가지지만 그 중에서 최댓값을 구하라는 것이다.
# 이런류의 문제는 파라메트릭 서치로 풀 수 있는데 파라메트릭 서치란 최적화 문제를 결정 문제로 
# 바꾸어 해결하는 기법이다. 결정 문제를 조건문안에 넣어 최대한 최적화된 해를 구하게 하는 것이다.
# 이 문제에서 결정 문제는 'h높이로 떡을 잘랐을때 잘린 부분의 총합이 손님이 원하는 m보다 작은가 큰가' 이다.
# 그래서 이런류의 해가 여러개고 그 중 최적화된 해를 찾아야하는 문제는  파라메트릭 서치를 이용한다.
# (파라메트릭 서치와 이진 탐색의 차이점은 결정 문제로 바꾸어 해결하느냐 마느냐 인것이다.)

# 문제에서는 재귀보다 반복문을 쓰는게 더 간결하다고 했지만
# 처음에 문제를 풀때 재귀로 풀어 보았다.
# 무한반복문을 이용해 랜덤넘버를 입력변수에 넣어서 재귀로 푼 방법과 반복문으로 푼 방법을 비교해보았는데
# 아마도 재귀로 푼 저 방법도 정답일듯...

