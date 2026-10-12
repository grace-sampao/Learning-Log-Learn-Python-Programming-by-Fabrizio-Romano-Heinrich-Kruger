class A:
    label = "a"

class B(A):
    pass            # was: label = 'b'

class C(A):
    label = "c"

class D(B, C):
    pass

d = D()

print(d.label)
print(d.__class__.mro())            # another way to get the MRO
