from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)

def solve():
    n = int(input().rstrip())

    time = [0] * n
    graph = [[] for _ in range(n)]

    for i in range(n):
        input_list = list(map(int, input().rstrip().split()))

        for j in range(len(input_list)):
            if j == 0:
                time[i] = input_list[j]
            else:
                if input_list[j] != -1:
                    graph[i].append(input_list[j] - 1)
    
    indegree = [len(g) for g in graph]

    q = deque()

    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in range(n):
            for j in graph[i]:
                if j == now:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        q.append(i)
        
        if q:
            max_time = -INF
            for i in graph[q[0]]:
                max_time = max(max_time, time[i])
            time[q[0]] += max_time

    for i in time:
        print(i)

if __name__ == '__main__':
    solve()

# 이것이 코딩테스트다 with Ptyhon 실전문제 10-9 문제 (커리큘럼)
# P. 303

# 위상 정렬 알고리즘의 응용문제이다.
# 더 쉽게 풀 수 있었는데 아직 위상 정렬 알고리즘 자체가 익숙하지 않아서 정말 어렵게 풀었다.
# 21번째 줄에 해당 노드에 들어 오는 노드를 append 해서 넣어주는게아니라 해당 노드가 향하고 있는 노드를 해당 노드에 
# 넣어주는 편이 훨씬 쉽게 풀 수 있다.
# 진입 차수를 21번째 줄 처럼 쓴 다음에 해당 노드가 가지고 있는 리스트의 길이로 쓰려고 접근을 해버려서
# 더 어렵게 간 것 같았다. (23번째 줄 보면 진입차수를 해당 노드가 가지고 있는 리스트의 길이로 구현했음)

# 문제에 대한 접근 방법 자체는 올바르게 접근을 했는데 구현 단계에서 너무 어렵게 접근을 한 것 같다.
# 위상 정렬 알고리즘에 대해 책의 내용도 제대로 더 읽어보고 문제도 한번 더 풀어봐야할 것 같다.

# 그리고 입력으로 받는 n이 1에서 500까지의 수 인데 이렇게 1부터 시작하면 리스트를 만들 때도 속 편하게 n + 1로 만들자!!!
# 괜히 메모리 조금 아끼겠다고 인덱스 0까지 다 쓰려고 하다가 코드가 더 꼬인다. (21번째줄 input_list[j] - 1을 해야지 제대로 작동함...)
