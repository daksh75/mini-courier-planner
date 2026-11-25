def knapsack(parcels, capacity):
    """
    0/1 Knapsack using Dynamic Programming.

    Each parcel can either be selected once or not selected.
    The goal is to get the maximum total parcel value without
    exceeding the vehicle's weight capacity.
    """
    number_of_parcels = len(parcels)

    # dp[i][w] = maximum value using the first i parcels
    # with a weight limit of w.
    dp = [[0 for w in range(capacity + 1)]
          for i in range(number_of_parcels + 1)]

    for i in range(1, number_of_parcels + 1):
        parcel = parcels[i - 1]
        weight = parcel["weight"]
        value = parcel["value"]

        for w in range(capacity + 1):
            # Do not select this parcel.
            dp[i][w] = dp[i - 1][w]

            # Select this parcel if it fits.
            if weight <= w:
                selected_value = value + dp[i - 1][w - weight]
                if selected_value > dp[i][w]:
                    dp[i][w] = selected_value

    # Trace backwards to find which parcels were selected.
    selected_parcels = []
    remaining_capacity = capacity

    for i in range(number_of_parcels, 0, -1):
        if dp[i][remaining_capacity] != dp[i - 1][remaining_capacity]:
            parcel = parcels[i - 1]
            selected_parcels.append(parcel)
            remaining_capacity -= parcel["weight"]

    selected_parcels.reverse()
    return selected_parcels, dp[number_of_parcels][capacity]
