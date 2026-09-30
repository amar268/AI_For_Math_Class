"""Estimate pi using random points in a unit square."""

import random


def estimate_pi(samples=100_000):
    inside_circle = 0
    for _ in range(samples):
        x, y = random.random(), random.random()
        if x * x + y * y <= 1:
            inside_circle += 1
    return 4 * inside_circle / samples


if __name__ == "__main__":
    print(f"Estimated pi: {estimate_pi():.6f}")
