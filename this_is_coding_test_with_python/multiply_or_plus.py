import sys
input = sys.stdin.readline

def solve():
    s = input().rstrip()

    result = 0

    for i in s:
        n = int(i)
        if n <= 1 or result == 0:
            result += n
        else:
            result *= n

    print(result)

if __name__ == '__main__':
    solve()

# 이것이 코딩테스트다 with Python 기출문제 Q 02 (곱하기 혹은 더하기)
# P. 312

# 간단한 그리디 문제이고 접근 방법 자체는 괜찮았다.
# 숫자가 0이면 곱해버리면 결과값이 0이 되어버리니까 0일때는 더해주기만 하면 된다고 생각했다.
# 하지만 간과한 부분이 있었다.

# 1같은 경우에도 곱하는 것 보다 더하는 것이 결과값을 더 크게 바꾼다.
# 예를 들어 2 * 1 보다 2 + 1이 결과값이 항상 더 크다.

# 쉬운 문제라고 방심하면서 대충 생각해보고 코드를 짜지말고 엣지케이스의 가까운 부분도 한번 더 체크 해보자!
# (이 문제에서 제일 확인하기 쉬운 엣지 케이스는 0 이니까 0 주변인 1도 한번 시뮬레이션 해보는 것 이다.)
