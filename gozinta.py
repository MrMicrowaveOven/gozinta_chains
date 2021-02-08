def get_factors(n):
    factors = []
    for i in range(2, n - 1):
        if n % i == 0:
            factors.append(i)
    return factors

def get_gozinta(n):
    chains = [[1,n]]
    factors = get_factors(n)
    for factor in factors:
        factor_chains = get_gozinta(factor)
        for factor_chain in factor_chains:
            factor_chain.append(n)
            chains.append(factor_chain)
    chains.sort()
    return chains

# print(get_factors(10))
# print(get_factors(15))
# print(get_factors(100))
# print(get_factors(2))

print(len(get_gozinta(48)))
