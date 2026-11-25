import heapq


def dijkstra(graph, start):
    """
    Find shortest distances from start to every reachable node.
    The graph must have non-negative edge weights.
    """
    distances = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}

    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Ignore an outdated queue entry.
        if current_distance > distances[current_node]:
            continue

        for neighbor, edge_weight in graph[current_node].items():
            new_distance = current_distance + edge_weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances, previous


def shortest_path(graph, start, destination):
    distances, previous = dijkstra(graph, start)

    if destination not in distances or distances[destination] == float("inf"):
        return float("inf"), []

    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()
    return distances[destination], path
