import heapq

def dijkstra(graph, start):
    shortest_paths = {node: (float('inf'), []) for node in graph}
    shortest_paths[start] = (0, [start])
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < shortest_paths[neighbor][0]:
                shortest_paths[neighbor] = (distance, shortest_paths[current_node][1] + [neighbor])
                heapq.heappush(pq, (distance, neighbor))

    return shortest_paths


graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 6, 'D': 1},
    'C': {'A': 5, 'B': 6, 'D': 3, 'E': 8},
    'D': {'B': 1, 'C': 3, 'E': 4},
    'E': {'C': 8, 'D': 4}
}


start_node = 'A'
paths = dijkstra(graph, start_node)

print(f"\nLink State Routing Table from Node '{start_node}':")
for node in sorted(paths):
    cost, path = paths[node]
    print(f"To {node}: Cost = {cost}, Path = {' -> '.join(path)}")
