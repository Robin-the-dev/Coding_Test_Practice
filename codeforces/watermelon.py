w = int(input())

def slice_watermelon(w):
    for i in range(2, w, 2):
        sliced_watermelon = w - i
        if sliced_watermelon % 2 == 0:
            return 'YES'

    return 'NO'

print(slice_watermelon(w))

# Codeforces 4A 문제 (Watermelon)
# https://codeforces.com/contest/4/problem/A

# 정말 단순한 완전 탐색 (brute force) 문제이다.
# 단순히 w에서 2에서 w사이에 있는 짝수를 빼줘서
# 그 뺀값이 짝수이면 YES 반복문이 끝나버려서 뺀값이 짝수가 아니면
# NO를 출력하게 한다.
