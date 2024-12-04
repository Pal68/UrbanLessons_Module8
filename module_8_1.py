def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        if type(a) == str:
            b = str(b)
        else:
            a = str(a)
    finally:
        return a + b

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))