import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().rstrip().split())
    coins = [int(input().rstrip()) for _ in range(n)]

    dp_table = [0] * (m + 1)
    minimum = 10000

    coins.sort()

    for i in range(coins[0]):
        dp_table[i] = -1

    for coin in coins:
        if coin <= m:
            dp_table[coin] = 1

    for i in range(coins[0], m + 1):
        if dp_table[i] == 0:
            for coin in coins:
                if i - coin < 0 or dp_table[i - coin] == -1:
                    continue
                minimum = min(dp_table[i - coin] + 1, minimum)
            if minimum == 10000:
                dp_table[i] = -1
            else:
                dp_table[i] = minimum
            minimum = 10000
    
    print(dp_table[m])

def solve2():
    n, m = map(int, input().rstrip().split())
    coins = [int(input().rstrip()) for _ in range(n)]

    dp_table = [10001] * (m + 1)

    # 아래의 코드를 넣어줘야지 반복문이 제대로 작동한다.
    # 왜냐하면 0원의 경우, 화폐를 사용하지 않았을때 만들 수 있으므로 0을 넣어준다.
    dp_table[0] = 0

    for coin in coins:
        for i in range(coin, m + 1):
            dp_table[i] = min(dp_table[i - coin] + 1, dp_table[i])

    if dp_table[m] == 10001:
        print(-1)
    else:
        print(dp_table[m])

if __name__ == '__main__':
    solve2()

# 이것이 코딩테스트다 with Python 실전문제 8-8 문제 (효율적인 화폐 구성)
# P. 226

# 그리디로 풀 수 있을것 같아 보이지만 다이나믹 프로그래밍 문제이다.
# 왜냐하면 화폐의 큰 단위는 작은 단위의 배수가 아니라서 그리디로 최적의 해를 구할 수 없다.

# solve() 함수가 내가 푼 방법인데 시간안에 풀었고 여러가지 입력을 넣어봤는데
# 아마도 정답이 아닐까 싶다.
# 접근을 제대로 했다는 것이 고무적인데 내가 접근한 접근 방법이 책의 해설과도 같았다.

# 하지만 사실 코드가 깔끔하지 못하고 쓸데없이 반복문으로 미리 초기화를 한것이 많아서
# 해설을 읽고 다시 풀어 보았다. (다시 푼것이 solve2()이다.)

# solve2()에서는 dp table의 0번째를 0으로 할당해주는 것이 중요한 부분이다.
# 그래야지 이후에 나오는 반복문에서 제대로 계산이 된다.
# dp table에서 10001로 초기화 해준 이유는 m이 1 <= m <= 10000 이기 때문이다.

# 다이나믹 프로그래밍 문제를 계속 풀다 보니 접근방법을 익히고 있는것 같아 기분이 좋다!
