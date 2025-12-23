
import heapq

graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4},
    "D": {"B": 1, "C": 4}
}


def dijkstra(graph: dict, start):
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0

    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            if neighbor in visited:
                continue

            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances

if __name__ == "__main__":
   
    start_vertex = "A"
    result = dijkstra(graph, start_vertex)

    print(f"Shortest distances from {start_vertex}:")
    for vertex, distance in result.items():
        print(f"{vertex}: {distance}")
