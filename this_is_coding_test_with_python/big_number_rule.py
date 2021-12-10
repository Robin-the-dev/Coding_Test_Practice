n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort(reverse = True)
num1 = numbers[0]
num2 = numbers[1]
big_num = 0

if num1 == num2:
    big_num = num1 * m
    print(big_num)
else:
    if k >= m:
        big_num = num1 * m
        print(big_num)
    else:
        m_remainder = m % (k + 1)
        m_quotient = m // (k + 1)
        big_num = (num1 * k + num2) * m_quotient + num1 * m_remainder
        print(big_num)

# 이것이 코딩테스트다 with Python 실전문제 3-2 문제 (큰 수의 법칙)
# P. 92

# 이것도 크게 어렵지 않은 그리디 알고리즘을 사용하는 문제이다.
# 문제에 제시되어있는 법칙을 이용해 배열안에 들어있는 숫자들을 사용하여 가장 큰 수를 만드는 문제이다.
# 배열에서의 가장 큰 수 * k에 두번째로 큰 수를 더한 것이 반복되는 꼴이다.
# 그렇기 떄문에 반복문을 이용해 하나 하나 풀 수 도 있지만 더 효율적인 방법으로는
# 반복되는 수열을 파악하여 (이 문제에서는 가장 큰 수 * k + 두번째로 큰 수) 식을 만들어 코드에 바로 적용하는 것이다.
