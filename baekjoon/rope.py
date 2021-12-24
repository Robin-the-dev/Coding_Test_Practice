import sys
input = sys.stdin.readline
INF = int(1e9)

def solve():
    n = int(input().rstrip())
    ropes = [int(input().rstrip()) for _ in range(n)]
    
    maximum = -INF

    ropes.sort(reverse = True)

    for i in range(n):
        temp = ropes[i] * (i + 1)
        if temp > maximum:
            maximum = temp

    print(maximum)

if __name__ == '__main__':
    solve()

# 백준 2217번 문제 (로프)
# https://www.acmicpc.net/problem/2217

# 조금만 생각하면 어렵지않게 풀 수 있는 그리디 알고리즘 문제이다.
# 로프들을 입력 받고 그 로프들을 이용해서 들수있는 최대 중량을 구하는 문제이다. (로프를 다 사용할 필요는 없음)
# k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k만큼의 중량이 걸리게 되기 때문에
# w의 최댓값을 구하면 되어서 w = k * '고른 로프들 중에서 제일 작은 로프가 들 수 있는 최대 중량' 으로 w를 구할 수 있다.
# (예를 들어 10, 15의 로프를 사용한다고 하면 이중에서 제일 작은 최대 중량은 10 이다.)
# 이 조건을 만족시키기 위해서 내림차순으로 정렬을 한 다음 반복문으로 처음부터 끝까지 위의 계산식을 계산해서 최대 중량을 구했다.

# 그리디 알고리즘 문제를 여러개 풀어보면서 느낀건데 그리디 알고리즘은 항상 그 상황에서 제일 최적의 상황만을 고려 하기 때문에
# 정렬을 시켜서 풀어야하는 경우가 많은 것 같다고 느꼈다. 그리디 알고리즘 문제라고 판단이 되면 정렬을 적극적으로 활용해보자!
