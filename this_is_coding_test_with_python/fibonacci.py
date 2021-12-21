import sys
input = sys.stdin.readline

def solve():
    n = int(input().rstrip())
    dp = [0] * 10001

    dp[1] = dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    print(dp[n])

if __name__ == '__main__':
    solve()

# 이것이 코딩테스트다 with Python 예제 8-4 문제 (피보나치 수열)
# P. 215

# 대표적인 다이나믹 프로그래밍 문제이다.
# 단순히 다이나믹 프로그래밍을 사용하지 않고 재귀로만 푼다면
# 연산수가 너무 많아지고 또한 재귀 특성상 너무 많은 재귀함수가 호출된다면
# 스택 오버플로우가 일어나기때문에 다이나믹 프로그래밍으로 풀어야한다.

# 다이나믹 프로그래밍은 반복문으로 풀 수 있는 보텀업과 재귀로 풀수있는 탑다운 방식이 있다.
# 보통 반복문으로 풀수있는게 더 효율적이기 때문에 보텀업 방식으로 풀어 보았다.
# 참고로 예제라 입력조건은 없지만 스스로 만든 입력조건은 
# 1 <= n <= 10000 이다.
