from dijkstra import shortest_path


def nearest_neighbor_tsp(graph, start, delivery_points):
    """
    Approximate a delivery route using the Nearest Neighbor method.

    For each step, choose the unvisited delivery point with the
    smallest shortest-path distance from the current location.
    Return to the starting point after the last delivery.
    """
    unvisited = list(dict.fromkeys(delivery_points))
    if start in unvisited:
        unvisited.remove(start)

    route = [start]
    total_distance = 0
    current = start
    route_segments = []

    while unvisited:
        nearest_point = None
        nearest_distance = float("inf")
        nearest_path = []

        for point in unvisited:
            distance, path = shortest_path(graph, current, point)

            if distance < nearest_distance:
                nearest_distance = distance
                nearest_point = point
                nearest_path = path

        if nearest_point is None or nearest_distance == float("inf"):
            raise ValueError("A delivery point cannot be reached from the current location.")

        route_segments.append(nearest_path)
        total_distance += nearest_distance
        route.append(nearest_point)
        unvisited.remove(nearest_point)
        current = nearest_point

    # Return to the depot.
    if current != start:
        return_distance, return_path = shortest_path(graph, current, start)
        if return_distance == float("inf"):
            raise ValueError("The depot cannot be reached from the last delivery point.")
        total_distance += return_distance
        route_segments.append(return_path)
        route.append(start)

    return route, total_distance, route_segments
