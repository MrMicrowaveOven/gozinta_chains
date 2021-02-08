import math

def how_many_primes(n):
    total = 0
    for i in range(2, n):
        if i % (10**9) == 0:
            print(i)
        if is_prime(i):
            total += 1
    return total

def is_prime(n):
    if n == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

# print(is_prime(2))
# print(is_prime(5))
# print(is_prime(8))
# print(is_prime(12))

print("Total: " + str(how_many_primes(10**12)))
