n = int(input())
people = list(map(int, input().split()))
time = 0
prev_time = 0

people.sort()

for person in people:
    time += person + prev_time
    prev_time = person + prev_time

print(time)

# 백준 11399번 문제 (ATM)
# https://www.acmicpc.net/problem/11399

# 정말 직관적이고 단순한 내용의 그리디 문제였다.
# ATM 앞에 사람들이 서있고 그 사람들마다 돈을 인출하는데 걸리는 시간이 다르다고 하였을때
# 필요한 시간의 합의 최솟값을 구하는 내용이다.
# 사람들의 순서를 변경할 수 있다고 문제에서 제시를 했기 때문에
# 보자마자 바로 떠오른 방법으로 오름차순으로 정렬을 하고 시간의 합을 구하면
# 항상 최솟값을 구할 수 있다.
