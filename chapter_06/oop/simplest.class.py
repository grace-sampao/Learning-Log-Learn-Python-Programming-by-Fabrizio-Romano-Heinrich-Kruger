class Simplest:
    pass

print(type(Simplest))       # what type is this object?

simp = Simplest()       # we create an instance of Simplest: simp
print(type(simp))       # what type is simp?
# is simp an instance of simplest?
print(type(simp) is Simplest)       # There's a better way to do this
