import sys
input = sys.stdin.readline

def solve():
    n = int(input().rstrip())
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    c = [-1] * n
    min_num = 101
    min_num_idx = -1
    result = 0

    a.sort(reverse = True)

    for i in range(n):
        for j in range(n):
            if b[j] < min_num and c[j] == -1:
                min_num = b[j]
                min_num_idx = j

        c[min_num_idx] = a[i]
        result += a[i] * b[min_num_idx]
        min_num = 101
        min_num_idx = -1

    return result

if __name__ == '__main__':
    print(solve())

# 백준 1026번 문제 (보물)
# https://www.acmicpc.net/problem/1026

# 단순한 그리디 문제인데 b는 재배열 하지 않고 정답을 내야한다.
# 그래서 b의 가장 작은 수를 찾을때 c라는 배열을 만들어서 그 다음의 작은수를 찾을 수 있게끔 중복체크를 할 수 있게
# 해주었다.
# 큰 틀은 반복문 두개를 돌려 a의 가장 큰수와 b의 가장 작은수 끼리 곱셈을 해줘서 결과값을 도출 하면 된다.
