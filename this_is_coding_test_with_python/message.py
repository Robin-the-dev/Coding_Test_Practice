import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def solve():
    n, m, c = map(int, input().rstrip().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        x, y, z = map(int, input().rstrip().split())
        graph[x].append((z, y))

    distance = [INF] * (n + 1)

    pq = []

    distance[c] = 0
    heapq.heappush(pq, (0, c))

    while pq:
        cost, start = heapq.heappop(pq)

        if distance[start] < cost:
            continue
        
        for i in graph[start]:
            new_cost = cost + i[0]

            if new_cost < distance[i[1]]:
                distance[i[1]] = new_cost
                heapq.heappush(pq, (new_cost, i[1]))
    
    count = 0
    time = 0

    for i in range(1, n + 1):
        if distance[i] == 0 or distance[i] == INF:
            continue
        count += 1
        time = max(distance[i], time)

    print(count, time)

def revise():
    n, m, c = map(int, input().rstrip().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        x, y, z = map(int, input().rstrip().split())
        graph[x].append((y, z))

    pq = []
    distance = [INF] * (n + 1)
    distance[c] = 0
    heapq.heappush(pq, (0, c))

    while pq:
        cost, start = heapq.heappop(pq)

        if distance[start] < cost:
            continue

        for i in graph[start]:
            dest = i[0]
            # to_cost = i[1]이 되면 안되고 현재의 노드를 거쳐서 갈때의 cost를 알아야 되기 때문에
            # to_cost = i[1] + cost가 되어야 한다.
            to_cost = i[1] + cost

            if distance[dest] > to_cost:
                distance[dest] = to_cost
                heapq.heappush(pq, (to_cost, dest))

    count = 0
    time = 0

    for i in range(1, n + 1):
        if distance[i] < INF:
            count += 1
            time = max(time, distance[i])

    # 시작 노드는 제외되어야하므로 -1을 해준다.
    print(count - 1, time)

if __name__ == '__main__':
    solve()
    revise()

# 이것이 코딩테스트다 with Python 실전문제 9-5 문제 (전보)
# P. 262

# 이것 또한 최단거리 문제이고 입력으로 받는 노드의 개수와 간선의 개수가 충분히 많기 때문에
# 우선순위 큐를 이용한 다익스트라 알고리즘을 구현하는 것이 좋을것 같아 다익스트라 알고리즘을 사용하였다.

# 사실 다익스트라 알고리즘을 응용해야 되는 문제도 아닌데 왜 난이도를 높게 준지 이해가 안가지만
# 다익스트라 알고리즘을 잘 구현할줄알고 문제를 똑바로 읽고 구현만 한다면 어려운 문제는 아니다.
# 마지막 반복문을 쓸때 또 쓸데없이 실수를 해버렸는데 (38번째 줄 / 인덱스를 이용해 distance에 접근 하려고 했는데
# 바보 같이 distance[i]처럼 인덱싱을 하지않고 착각을 하고 그냥 i로 써버렸다.) 이런 초보적인 실수는
# 집중을 똑바로 하고 안 할 수 있도록 하자!

# 또 출력으로 도시의 총개수와 도시들이 모두 메시지를 받는 데까지 걸리는 시간을 내보내야 하는데
# 시간의 총합인줄알고 또 다 더해버렸다. 꼭 문제를 제대로 읽고 초보적인 실수를 하지말자!!!
