# n, k = map(int, input().split())
# 
# coins = [int(input()) for _ in range(n)]
# coins.sort(reverse = True)
# 
# result = 0
# 
# while k != 0:
#     c = 0
#     for coin in coins:
#         if coin <= k:
#             c = coin
#             break
#     result += k // c
#     k %= c
# 
# print(result)

# 백준 11047번 문제 (동전 0)
# https://www.acmicpc.net/problem/11047

# 이것도 그리디 알고리즘을 이용해서 풀면 되는 문제이다.
# 동전들이 입력으로 주어지고 k원을 만들기 위한 최소의 동전수를 구하는 문제이다.
# 문제의 요구사항을 정확하게 코드로 구현해서 풀었는데
# 다른 사람들이 푼 코드를 보고 더 깔끔하게 코드를 쓸 수 있다는 것을 확인했다.
# 아래는 더 깔끔하게 풀어 본 것이다.

# 이렇게 풀면 위의 코드보다 시간복잡도도 더 빠르게 나올 듯 하다. O(n)
# 왜냐하면 위의 코드는 while문안에 적절한 coin을 찾는 for문이 또 있기 때문이다.

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

result = 0

while k > 0:
    coin = coins.pop()
    result += k // coin
    k %= coin

print(result)
