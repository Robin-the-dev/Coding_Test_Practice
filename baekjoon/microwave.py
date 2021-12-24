import sys
input = sys.stdin.readline

def solve():
    t = int(input().rstrip())
    a = 60 * 5
    b = 60
    c = 10

    counts = []

    counts.append(t // a)
    counts.append((t % a) // b)
    counts.append(((t % a) % b) // c)

    if (((t % a) % b) % c) != 0:
        print(-1)
    else:
        for count in counts:
            print(count, end = ' ')

if __name__ == '__main__':
    solve()

# 백준 10162번 문제 (전자레인지)
# https://www.acmicpc.net/problem/10162

# 엄청 간단한 그리디 알고리즘 문제이다.
# 딱히 언급할 것은 없고 실행 시간 당겨보려고 재미로 반복문을 쓰지 않고 한번 코드를 써봤다.
