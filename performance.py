import csv
import random
import time
from pathlib import Path

from sorting import merge_sort_parcels
from knapsack import knapsack
from dijkstra import dijkstra
from tsp import nearest_neighbor_tsp


def make_parcels(count):
    parcels = []

    for i in range(count):
        parcels.append({
            "id": i + 1,
            "destination": "A",
            "weight": random.randint(1, 10),
            "value": random.randint(10, 100),
            "priority": random.randint(1, 5),
            "deadline": random.randint(1, 10)
        })

    return parcels


def make_graph(count):
    graph = {}

    for i in range(count):
        graph[str(i)] = {}

    # Make a connected graph with non-negative weights.
    for i in range(count):
        for j in range(i + 1, count):
            weight = random.randint(1, 20)
            graph[str(i)][str(j)] = weight
            graph[str(j)][str(i)] = weight

    return graph


def measure_time(function):
    start_time = time.perf_counter()
    function()
    end_time = time.perf_counter()
    return end_time - start_time


def run_tests():
    random.seed(10)
    results = []

    print("PERFORMANCE TESTING")
    print("-" * 55)

    # Sorting and Knapsack tests with increasing parcel counts.
    for size in [50, 100, 200, 400]:
        parcels = make_parcels(size)

        sorting_time = measure_time(
            lambda: merge_sort_parcels(parcels)
        )
        knapsack_time = measure_time(
            lambda: knapsack(parcels, 100)
        )

        results.append({
            "algorithm": "Merge Sort",
            "input_size": size,
            "time_seconds": sorting_time
        })
        results.append({
            "algorithm": "0/1 Knapsack",
            "input_size": size,
            "time_seconds": knapsack_time
        })

        print(
            f"Parcels: {size:<4} "
            f"Merge Sort: {sorting_time:.6f} sec | "
            f"Knapsack: {knapsack_time:.6f} sec"
        )

    # Graph algorithm tests.
    for size in [10, 20, 40, 80]:
        graph = make_graph(size)

        dijkstra_time = measure_time(
            lambda: dijkstra(graph, "0")
        )

        delivery_points = [str(i) for i in range(1, min(size, 8))]
        tsp_time = measure_time(
            lambda: nearest_neighbor_tsp(graph, "0", delivery_points)
        )

        results.append({
            "algorithm": "Dijkstra",
            "input_size": size,
            "time_seconds": dijkstra_time
        })
        results.append({
            "algorithm": "Nearest Neighbor TSP",
            "input_size": len(delivery_points),
            "time_seconds": tsp_time
        })

        print(
            f"Graph nodes: {size:<4} "
            f"Dijkstra: {dijkstra_time:.6f} sec | "
            f"TSP (up to 7 stops): {tsp_time:.6f} sec"
        )

    output_folder = Path(__file__).parent
    csv_path = output_folder / "runtime_results.csv"

    with open(csv_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["algorithm", "input_size", "time_seconds"]
        )
        writer.writeheader()
        writer.writerows(results)

    print("\nRuntime results saved to:", csv_path)

    # Create a chart if matplotlib is installed.
    try:
        import matplotlib.pyplot as plt

        chart_path = output_folder / "runtime_chart.png"

        for algorithm in ["Merge Sort", "0/1 Knapsack", "Dijkstra",
                          "Nearest Neighbor TSP"]:
            selected = [
                item for item in results
                if item["algorithm"] == algorithm
            ]
            sizes = [item["input_size"] for item in selected]
            times = [item["time_seconds"] for item in selected]

            plt.plot(sizes, times, marker="o", label=algorithm)

        plt.xlabel("Input size")
        plt.ylabel("Execution time (seconds)")
        plt.title("Mini-Courier Planner - Algorithm Runtime")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(chart_path)
        plt.close()

        print("Runtime chart saved to:", chart_path)

    except ImportError:
        print("Matplotlib is not installed. Install it to create the chart.")


if __name__ == "__main__":
    run_tests()
