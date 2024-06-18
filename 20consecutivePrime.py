def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p] == True:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n + 1) if primes[p]]
    return prime_numbers

def sum_of_consecutive_primes(n):
    prime_numbers = sieve_of_eratosthenes(n)
    sum_primes = sum(prime_numbers)
    return sum_primes

# Example usage
N = 30
result = sum_of_consecutive_primes(N)
print(f"The sum of all consecutive prime numbers up to {N} is: {result}")
