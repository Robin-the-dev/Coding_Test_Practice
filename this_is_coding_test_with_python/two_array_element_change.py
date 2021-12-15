n, k = map(int, map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)

for i in range(k):
    # 비교문을 잊지말자!
    if a[i] < b[i]:
        a[i] = b[i]
    else:
        break

print(sum(a))

# 이것이 코딩테스트다 with Python 실전문제 6-12 문제 (두 배열의 원소 교체)
# P. 182

# 간단한 문제인데 처음에 풀때 너무 생각 없이 풀었다.
# 기본 컨섭은 이해하고 그대로 풀었는데 반복문을 통해 a의 원소와
# b의 원소를 비교하지 않고 바로 대입해버렸다.
# a의 원소가 클 경우도 있기때문에 비교문으로 a의 원소가 b의 원소보다
# 작을때만 대입을 해주고 아닌경우에는 반복문을 나오면 된다.
# 왜냐하면 a는 오름차순 b는 내림차순으로 이미 정렬을 했기때문에
# a의 원소가 b의 원소보다 큰 순간이 오면 반복문을 더 돌릴 필요도 없이
# b의 이후의 원소들은 무조건 a의 원소들 보다 작기 때문이다.
