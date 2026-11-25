# Mini-Courier Planner

**Course:** Design & Analysis of Algorithms (ETCCDA302)  
**Project:** Mini-Courier Planner  
**Language:** Python

## 1. Project objective

The project simulates a courier planning system. It sorts parcels, selects parcels within a vehicle's carrying capacity, calculates shortest paths, and creates an approximate delivery route.

## 2. Algorithms used

1. **Merge Sort:** Sorts parcels by higher priority first and earlier deadline when priorities are equal.
2. **0/1 Knapsack (Dynamic Programming):** Selects the combination of parcels with maximum total value without exceeding vehicle capacity.
3. **Dijkstra's Algorithm:** Calculates shortest paths in a weighted graph. All edge weights must be non-negative.
4. **Nearest Neighbor TSP Approximation:** Repeatedly visits the nearest unvisited delivery point and returns to the depot. It is a heuristic and does not guarantee the globally shortest TSP route.

## 3. Project files

- `main.py` - runs the complete courier planner.
- `sorting.py` - Merge Sort implementation.
- `knapsack.py` - 0/1 Knapsack Dynamic Programming implementation.
- `dijkstra.py` - Dijkstra shortest-path implementation.
- `tsp.py` - Nearest Neighbor TSP approximation.
- `performance.py` - measures runtime and creates a CSV and chart.
- `data/parcels.json` - sample parcels, vehicle capacity and road graph.

## 4. Requirements

Python 3.8 or later is recommended. The main application uses Python standard-library modules. Matplotlib is used only for the optional runtime chart.

Install chart dependency:

```bash
python -m pip install -r requirements.txt
```

## 5. How to run

Open a terminal in this project folder.

Run the main application:

```bash
python main.py
```

Run performance tests:

```bash
python performance.py
```

Performance testing creates `runtime_results.csv` and, if Matplotlib is installed, `runtime_chart.png`.

## 6. Sample data format

Each parcel has an ID, destination, weight, value, priority and deadline. The graph is an adjacency list: each location stores its connected locations and road distances in kilometres.

## 7. Complexity

- Merge Sort: O(n log n) time and O(n) auxiliary space.
- 0/1 Knapsack: O(nW) time and O(nW) table space.
- Dijkstra with a binary heap: O((V + E) log V) time for a standard adjacency-list implementation.
- Nearest Neighbor TSP: O(k^2) distance-selection steps, with shortest-path calculations performed between candidate locations. Its practical total cost also depends on the graph and shortest-path implementation.

## 8. Important limitations

- The sample road graph is a simplified undirected road network.
- The TSP method is an approximation, not an exact optimal TSP solver.
- Knapsack maximizes parcel value under the weight limit. Priority sorting is displayed separately; sorting does not force the knapsack to select the highest-priority parcels.
- Runtime values depend on the computer and should be measured on the submission computer.
- Replace or extend the sample data to test additional cases.

## 9. Suggested screenshots for submission

Capture:
1. Main program showing sorted parcels.
2. Knapsack selected parcels and used capacity.
3. Dijkstra shortest-path output.
4. Nearest Neighbor delivery sequence and route distance.
5. Performance test output.
6. Runtime chart.

## 10. Conclusion

The project combines sorting, dynamic programming, graph shortest paths and a TSP approximation in one Python application. It demonstrates how algorithmic techniques can support parcel selection and courier route planning.
