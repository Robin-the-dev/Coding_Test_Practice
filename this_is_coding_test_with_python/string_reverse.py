import sys
input = sys.stdin.readline

def solve():
    s = input().rstrip()

    zero_cnt = 0
    one_cnt = 0
    prev_num = '' 

    for i in s:
        if prev_num != i:
            if i == '1':
                one_cnt += 1
            else:
                zero_cnt += 1
            prev_num = i

    print(min(zero_cnt, one_cnt))

if __name__ == '__main__':
    solve()

# 이것이 코딩테스트다 with Python 기출문제 Q 02 (문자열 뒤집기)
# P. 313
# https://www.acmicpc.net/problem/1439

# 정말 간단한 그리디 알고리즘 문제이지만 이것이 그리디 알고리즘 문제가 맞는지 아닌지 판별하기가 조금 까다로웠던것 같다.
# 보통의 그리디 알고리즘 문제들이 정렬을 하고 최적의 해를 구하는 것이 많기 때문에 뭔가 문제를 보자마자
# 바로 '아! 이거는 그리디 알고리즘 문제이다!'라고는 나오지 않았다. (책에서는 유형별로 문제를 정리 해놨기 때문에
# 그리디 알고리즘 유형을 풀고있어서 이 문제도 그리디 유형이니까 생각을 그리디 알고리즘이라고 정하고 접근해서
# 풀 수 있었다.)
# 이런식의 그리디 알고리즘 문제도 있다는 걸 염두에 두고 더 다양한 문제들을 접해볼 필요가 있을 것 같다.
