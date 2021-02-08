import math

def how_many_primes():
    return 1

def is_prime(n):
    for i in range(math.ceil(math.sqrt(n))):
        if i == 0 or i == 1:
            continue
        if n % i == 0:
            return False
    return True

print(is_prime(2))
print(is_prime(5))
print(is_prime(8))
print(is_prime(12))
