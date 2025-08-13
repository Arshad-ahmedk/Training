import math

# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

def findGCD(nums):
    a,b=max(nums),min(nums)
    return math.gcd(a,b)

print(findGCD([1,2,3]))