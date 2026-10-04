A = 100

ex1 = [A for A in range(5)]
print(A)        # prints: 100
# print(ex1)

ex2 = list(A for A in range(5))
print(A)        # prints: 100
# print(ex2)

ex3 = {A: 2 * A for A in range(5)}
print(A)        # prints: 100
# print(ex3)

ex4 = {A for A in range(5)}
print(A)        # prints: 100
# print(ex4)

s = 0
for A in range(5):
    s += A
print(A)        # prints: 4
