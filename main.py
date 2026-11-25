import json
from pathlib import Path

from sorting import merge_sort_parcels
from knapsack import knapsack
from dijkstra import shortest_path
from tsp import nearest_neighbor_tsp


def load_data():
    file_path = Path(__file__).parent / "data" / "parcels.json"

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def display_parcels(parcels):
    print("\nID   Destination   Weight   Value   Priority   Deadline")
    print("-" * 62)

    for parcel in parcels:
        print(
            f'{parcel["id"]:<4} '
            f'{parcel["destination"]:<13} '
            f'{parcel["weight"]:<8} '
            f'{parcel["value"]:<7} '
            f'{parcel["priority"]:<10} '
            f'{parcel["deadline"]}'
        )


def main():
    data = load_data()
    parcels = data["parcels"]
    graph = data["graph"]
    capacity = data["vehicle_capacity"]
    depot = data["depot"]

    print("=" * 55)
    print("             MINI-COURIER PLANNER")
    print("=" * 55)

    # PHASE 2 - Sorting
    print("\n1. PARCEL PRIORITIZATION USING MERGE SORT")
    sorted_parcels = merge_sort_parcels(parcels)
    display_parcels(sorted_parcels)

    # PHASE 2 - Dynamic Programming
    print("\n2. OPTIMAL PARCEL SELECTION USING 0/1 KNAPSACK")
    print("Vehicle capacity:", capacity, "kg")

    selected_parcels, maximum_value = knapsack(sorted_parcels, capacity)
    selected_weight = sum(parcel["weight"] for parcel in selected_parcels)

    print("\nSelected parcels:")
    display_parcels(selected_parcels)
    print("\nTotal selected weight:", selected_weight, "kg")
    print("Maximum parcel value:", maximum_value)

    # PHASE 3 - Dijkstra
    print("\n3. SHORTEST PATH USING DIJKSTRA")
    destinations = list(dict.fromkeys(
        parcel["destination"] for parcel in selected_parcels
    ))

    if not destinations:
        print("No parcels were selected. No delivery route is required.")
        return

    for destination in destinations:
        distance, path = shortest_path(graph, depot, destination)
        print(f"{depot} to {destination}: {' -> '.join(path)} | Distance: {distance} km")

    # PHASE 3 - Nearest Neighbor TSP
    print("\n4. DELIVERY ROUTE USING NEAREST NEIGHBOR TSP")
    route, total_distance, segments = nearest_neighbor_tsp(
        graph, depot, destinations
    )

    print("Delivery sequence:", " -> ".join(route))
    print("Route distance:", total_distance, "km")
    print("\nRoute details:")
    for segment in segments:
        print(" -> ".join(segment))

    print("\n5. SUMMARY")
    print("Total parcels available:", len(parcels))
    print("Parcels selected:", len(selected_parcels))
    print("Vehicle capacity:", capacity, "kg")
    print("Used capacity:", selected_weight, "kg")
    print("Total parcel value:", maximum_value)
    print("Total route distance:", total_distance, "km")
    print("\nProject completed successfully.")


if __name__ == "__main__":
    main()
