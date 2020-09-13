
def office(name, color='Yellow'):
    return f"The color of {name} is {color}"


var1 = office('MTN')
print(var1)
print(office('Alabian', 'Sky Blue'))


def multiplication(number, start=1, stop=12):
    for start in range(start, stop+1):
        print(f"{number} X {start} = {number*start}")


def times(number, start, stop):
    for start in range(start, stop+1):
        print(f"{number} X {start} = {number*start}")

times(4)


multiplication(3)
multiplication(4, 5)

