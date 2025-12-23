import random
from collections import Counter


def monte_carlo_simulation(num_trials: int):
    """
    Симуляція кидання двох кубиків методом Монте-Карло
    """
    sums = []

    for _ in range(num_trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        sums.append(dice1 + dice2)

    counts = Counter(sums)

    probabilities = {
        total: counts.get(total, 0) / num_trials
        for total in range(2, 13)
    }

    return probabilities, counts

ANALYTICAL_PROBABILITIES = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36,
}

import matplotlib.pyplot as plt


def plot_probabilities(monte_carlo_probs, analytical_probs):
    sums = list(range(2, 13))

    mc_values = [monte_carlo_probs[s] for s in sums]
    an_values = [analytical_probs[s] for s in sums]

    plt.figure(figsize=(10, 6))
    plt.bar(sums, mc_values, alpha=0.7, label="Monte Carlo")
    plt.plot(sums, an_values, marker="o", linestyle="--", label="Analytical")

    plt.xlabel("Sum of dice")
    plt.ylabel("Probability")
    plt.title("Monte Carlo simulation vs Analytical probabilities")
    plt.legend()
    plt.grid(axis="y", alpha=0.3)

    plt.show()


if __name__ == "__main__":
    trials = 100_000

    probabilities, counts = monte_carlo_simulation(trials)

    print(f"Trials: {trials}\n")
    print("Sum | Count | Probability")
    print("-------------------------")

    for total in range(2, 13):
        print(f"{total:>3} | {counts.get(total, 0):>6} | {probabilities[total]:.4f}")

    plot_probabilities(probabilities, ANALYTICAL_PROBABILITIES)
