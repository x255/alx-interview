#!/usr/bin/python3
"""Module defining isWinner function."""


def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= max_num:
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    return [num for num, prime in enumerate(is_prime) if prime]

def isWinner(x, nums):
    if x <= 0 or not nums:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    prime_set = set(primes)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 2:
            ben_wins += 1
            continue

        current_set = set(range(1, n + 1))
        maria_turn = True

        while current_set:
            prime_found = False
            for prime in primes:
                if prime in current_set:
                    prime_found = True
                    multiples = set(range(prime, n + 1, prime))
                    current_set -= multiples
                    break

            if not prime_found:
                if maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            maria_turn = not maria_turn

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))

