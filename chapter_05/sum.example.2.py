# s = sum([n**2 for n in range(10**10)])          # this is killed
s = sum(n**2 for n in range(10**10))              # this succeeds

print(s)
