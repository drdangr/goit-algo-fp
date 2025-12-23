items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    """
    Жадібний алгоритм вибору їжі за співвідношенням калорій до вартості
    """
    # Сортуємо страви за calories / cost (спадання)
    sorted_items = sorted(
        items.items(),
        key=lambda item: item[1]["calories"] / item[1]["cost"],
        reverse=True
    )

    total_cost = 0
    total_calories = 0
    chosen_items = []

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            chosen_items.append(name)
            total_cost += data["cost"]
            total_calories += data["calories"]

    return chosen_items, total_cost, total_calories

def dynamic_programming(items, budget):
    """
    Динамічне програмування для задачі вибору їжі (0/1 knapsack)
    """
    items_list = list(items.items())
    n = len(items_list)

    # dp[i][b] — макс. калорії для перших i предметів і бюджету b
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Заповнення таблиці
    for i in range(1, n + 1):
        name, data = items_list[i - 1]
        cost = data["cost"]
        calories = data["calories"]

        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(
                    dp[i - 1][b],
                    dp[i - 1][b - cost] + calories
                )
            else:
                dp[i][b] = dp[i - 1][b]

    # Відновлення набору страв
    chosen_items = []
    b = budget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name, data = items_list[i - 1]
            chosen_items.append(name)
            b -= data["cost"]

    chosen_items.reverse()

    total_calories = dp[n][budget]
    total_cost = sum(items[item]["cost"] for item in chosen_items)

    return chosen_items, total_cost, total_calories


if __name__ == "__main__":
    budget = 100

    print("Greedy:")
    print(greedy_algorithm(items, budget))

    print("\nDynamic programming:")
    print(dynamic_programming(items, budget))
