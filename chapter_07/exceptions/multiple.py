# values = (1, 2)
# values = (1, 0)
values = ("one", 2)

try:
    q, r = divmod(*values)
except ZeroDivisionError:
    print("You tried to divide by zero!")
except TypeError as e:
    print(e)
