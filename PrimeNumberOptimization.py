# Prime numbers are integers greater than 1 that are divisible only by 1 and themselves.
# The first few prime numbers are:
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, ...
# If you want all prime numbers except 2 and 3, then the list starts from:
# 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, ...
# 👉 In general, all primes except 2 and 3 are of the form 6k ± 1 (where k is an integer ≥ 1).
# For example:
# 5 = 6×1 − 1
# 7 = 6×1 + 1
# 11 = 6×2 − 1
# 13 = 6×2 + 1

def isprime(n):
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

for x in [25, 29, 49, 97]:
    print(x, isprime(x))

