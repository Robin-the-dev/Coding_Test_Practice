import sys
input = sys.stdin.readline

def solve():
    n = input().rstrip()
    num = []

    for i in n:
        num.append(int(i))

    num.sort(reverse = True)

    if sum(num) % 3 == 0 and num[-1] == 0:
        for i in num:
            print(i, end = '')
        print()
    else:
        print(-1)

if __name__ == '__main__':
    solve()

# 백준 10610번 문제 (30)
# https://www.acmicpc.net/problem/10610

# 그리디 알고리즘 문제를 풀려고 문제 유형에서 그리디로 해놓고 찾은 문제인데
# 그리디 알고리즘이 아닌건 아니지만 정수론 유형에 더 가까운 문제인듯 하다.

# 정수론 유형의 문제를 처음 풀어봐서 어떻게 접근하는지 몰라서 구글링의 도움을 받았고 그후 바로 코드로 구현했다.
# 코드로 구현하는것 자체는 보다시피 전혀 어려운 부분이 아니고 정수론을 잘 이해하고 있는 것이 중요한 것 같다.

# 위의 문제는 여러가지의 숫자조합을 받아 제일 큰 30의 배수를 만들어 출력으로 내보내는 것이다.
# 숫자조합은 최대 10^5개의 숫자로 구성이 되어있기 때문에 완전 탐색으로 경우의 수를 모두 찾는 것도 불가능하다.
# (10^5 까지의 숫자만을 받는다는 뜻이 아니라 숫자 갯수 자체가 최대 10^5라는 말이다.)
# 그리디적인 알고리즘이나 완전탐색을 생각하는 것보다 이 문제는 30의 배수가 되는 조건에 대해 한번 연구해볼 필요가 있다.
# 30의 배수가 되려면 숫자 조합의 1의 자리가 무조건 0 이어야한다. 아니면 나머지가 남기때문이다.
# 그리고 두번째 조건은 숫자조합들의 합이 3의 배수가 되어야한다. 왜냐하면 1의 자리는 0 이라는 전제조건을 위에서 이미 적용시켰기때문에
# 모든 숫자의 합이 3의 배수인것만 확인하면 된다.

# 그리고 위의 두 조건을 토대로 코드로 구현하면 된다.

# 정수론에 대해서 조금 더 알아보고 위와 같은 뭔가 정수를 다루는 문제인데 완전 탐색을 할 수 없을 경우에는 그 정수들의 패턴을 확인 해보는 것도
# 좋은 방법이라고 생각한다.

# 개인적으로는 코딩테스트로는 잘 안 나올 유형이라는 생각이 든다. 왜냐하면 코딩 테스트의 주 목적은 이런 정수론의 지식들 보다는 
# 코드의 구현이나 기본적인 알고리즘을 잘 사용할줄아는지를 묻기 때문이다. 그래도 공부를 해두면 좋을듯 하다.
