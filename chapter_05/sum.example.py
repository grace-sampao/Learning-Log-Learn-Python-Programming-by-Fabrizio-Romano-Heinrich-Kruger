s1 = sum([n**2 for n in range(10**6)])          # list comprehension
s2 = sum((n**2 for n in range(10**6)))          # generator expression
s3 = sum(n**2 for n in range(10**6))            # generator expression

# The expressions to get `s2` and `s3` are equivalent
# because the brackets in `s2` are redundant.

print(s1)
print(s2)
print(s3)
