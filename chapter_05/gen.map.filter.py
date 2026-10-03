N = 20
cubes1 = map(
    lambda n: (n, n**3),
    filter(
        lambda n: n % 3 == 0 or n % 5 == 0, range(N)
    ),
)
cubes2 = (
    (n, n**3) for n in range(N) if n % 3 == 0 or n % 5 == 0
)

print(cubes1)
print(cubes2)
