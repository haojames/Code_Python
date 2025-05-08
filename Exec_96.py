import math as mt
def sum_proper_divisors(n):
    if n == 1:
        return 0
    total = 1
    for i in range(2, int(mt.sqrt(n)) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

def find_amicable_numbers(N):
    amicable_pairs = set()
    for m in range(2, N + 1):
        n = sum_proper_divisors(m)
        if n > m and sum_proper_divisors(n) == m:
            amicable_pairs.add((m, n))
    return amicable_pairs
print(find_amicable_numbers(3000))