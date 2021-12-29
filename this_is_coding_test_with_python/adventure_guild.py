import sys
input = sys.stdin.readline

def solve():
    n = int(input().rstrip())
    m = list(map(int, input().rstrip().split()))

    result = 0
    count = 0
    
    m.sort()

    for i in m:
        count += 1
        if i == count:
            result += 1
            count = 0

    print(result)

if __name__ == '__main__':
    solve()

# 이것이 코딩테스트다 with Python 기출문제 Q 01 (모험가 길드)
# P. 311

# 그리디 알고리즘 문제라는 것을 인지만 하면 간단하게 풀 수 있는 문제이다.
# 간단한 입력을 기준으로 손으로 직접 접근 방법을 그려보면 더 간단하게 풀 수 있다.
# 크게 언급할만한 부분은 없다.
