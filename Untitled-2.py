def a():
    a = input()
    if a!=a[::-1]:
        return 'False'
    else:
        return 'True'
print(a())
