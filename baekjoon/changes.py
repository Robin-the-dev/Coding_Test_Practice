import sys
input = sys.stdin.readline

def solve():
    n = int(input().rstrip())

    changes = [500, 100, 50, 10, 5, 1]
    m = 1000 - n

    count = 0

    for change in changes:
        count += m // change
        m %= change

    print(count)

if __name__ == '__main__':
    solve()

# 백준 5585번 문제 (거스름돈)
# https://www.acmicpc.net/problem/5585

# 정말 쉬운 그리디 알고리즘 문제이다.
# 크게 언급할 내용은 없는 듯 하다.
