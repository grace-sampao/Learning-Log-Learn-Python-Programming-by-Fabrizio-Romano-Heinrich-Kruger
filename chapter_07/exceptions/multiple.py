# values = (1, 2)
# values = (1, 0)
values = ("one", 2)

try:
    q, r = divmod(*values)
except (ZeroDivisionError, TypeError) as e:
    print(type(e), e)
