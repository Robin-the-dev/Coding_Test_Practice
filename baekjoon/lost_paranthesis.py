import sys
input = sys.stdin.readline

def solve():
    exp = input().rstrip()
    
    num = ''
    arr = []

    for i in exp:
        if i != '+' and i != '-':
            num += i
        else:
            arr.append(int(num))
            arr.append(i)
            num = ''
    arr.append(int(num))

    while '+' in arr:
        plus_idx = arr.index('+')
        n1 = arr[plus_idx - 1]
        n2 = arr[plus_idx + 1]
        del arr[plus_idx - 1:plus_idx + 2]
        arr.insert(plus_idx - 1, n1 + n2)

    while '-' in arr:
        minus_idx = arr.index('-')
        n1 = arr[minus_idx - 1]
        n2 = arr[minus_idx + 1]
        del arr[minus_idx - 1:minus_idx + 2]
        arr.insert(minus_idx - 1, n1 - n2)

    print(arr[0])

def solve2():
    arr = list(input().rstrip().split('-'))
    newArr = []
    result = 0

    for i in arr:
        temp = list(map(int, i.split('+')))
        newArr.append(sum(temp))

    isFirst = True

    for i in newArr:
        if isFirst:
            result = i
            isFirst = False
        else:
            result -= i

    print(result)

if __name__ == '__main__':
    solve2()

# 백준 1541번 문제 (잃어버린 괄호)
# https://www.acmicpc.net/problem/1541

# 문자열 조작과 그리디 알고리즘 문제이다.
# 문제를 풀기위한 로직은 바로 알아차렸다.
# 단순히 더하기 연산자를 먼저 계산해주고 거기서 나온 결과물에 대해
# 빼기 연산자를 계산해주면 된다.

# 하지만 입력을 한줄에 받아서 문자열을 잘 처리해줬어야 했는데 여기서 조금 시간이 걸렸다.
# 결국 풀긴 풀었고 결과물은 solve() 함수이다.
# 하지만 코드가 너무 간결하지 못하고 살짝 어거지로 푼 느낌이 있어 다른 사람들이 푼 정답을 보고
# 힌트를 얻어서 문자열의 split() 함수를 잘 사용하면 쉽고 간결하게 풀 수 있다는 것을 알았다.

# 문자열을 다뤄야하는 문제가 나오면 문자열 함수들을 잘사용하자! 특히 split() 함수!
# 문자열 관련된 함수에 조금 더 익숙해 질 필요가 있을것 같다.
