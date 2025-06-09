import random

# This test simulates multiple lottery runs using specific seeds so that the
# randomness is deterministic. Each set of numbers should always fall in the
# expected range 1..45 inclusive.

def test_numbers_within_range():
    for seed in range(100):
        random.seed(seed)
        numbers = random.sample(range(1, 46), 6)
        assert all(1 <= n <= 45 for n in numbers)
