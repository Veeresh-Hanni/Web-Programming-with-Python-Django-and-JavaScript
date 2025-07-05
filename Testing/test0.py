from prime import is_prime


def  test_isprime(n,expected):
    if is_prime(n) != expected:
        print(f"ERROR on is_prime({n}), expected: {expected}")