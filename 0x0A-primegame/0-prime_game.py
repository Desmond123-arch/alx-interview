#!/usr/bin/python3
""" Pick the winner of the game """


def isWinner(x, nums):
    """ Is winner function returns the winner"""
    if not nums or x < 1:
        return None

    max_num = max(nums)

    # Step 1: Use Sieve of Eratosthenes to find all primes up to max_num
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes

    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False

    # Step 2: Calculate the number of prime removals for each number n
    prime_removals = [0] * (max_num + 1)
    for i in range(2, max_num + 1):
        prime_removals[i] = prime_removals[i - 1] + (1 if sieve[i] else 0)

    # Step 3: Simulate each game
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # The number of primes up to n is prime_removals[n]
        if prime_removals[n] % 2 == 1:
            maria_wins += 1  # Maria wins if the number of primes is odd
        else:
            ben_wins += 1    # Ben wins if the number of primes is even

    # Step 4: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
