from math import sqrt

# this step is the same as before
mx = 10
# we can combine generating and filtering in one comprehension
triples = [
    (a, b, int(c))
    for a in range(1, mx)
    for b in range(a, mx)
    if (c := sqrt(a**2 + b**2)).is_integer()
]

print(triples)
