from math import inf
from heapq import heappush, heappop

n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

def dijkstra(n, graph, start):
    distance_map = [inf for _ in range(n)]
    distance_map[start] = 0

    queue = []
    heappush(queue, [distance_map[start], start])
    
    while queue:
        current_distance, current_destination = heappop(queue)
        
        if distance_map[current_destination] >= current_distance:
            for i in range(n):
                tmp = current_distance + graph[current_destination][i]
                
                if tmp < distance_map[i]:
                    distance_map[i] = tmp
                    heappush(queue, [tmp, i])

    return distance_map

def solution(n, s, a, b, fares):
    s, a, b = s-1, a-1, b-1

    min_map = []
    taxi_map = [[inf] * n for _ in range(n)]
    result = inf

    for fare in fares:
        x, y, z = fare
        taxi_map[x-1][y-1] = z
        taxi_map[y-1][x-1] = z

    for i in range(n):
        min_map.append(dijkstra(n, taxi_map, i))

    for i in range(n):
        result = min(result, min_map[s][i] + min_map[i][a] + min_map[i][b])

    return result

print(solution(n, s, a, b, fares))
