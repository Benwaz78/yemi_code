
# def addition(num1, num2):
#     add = num1 + num2
#     print(add)


# addition(2, 3, 4)


def addition(*args):
    add = 0
    for n in args:
        add += n
    print(add)

addition(2, 3, 4, 5)