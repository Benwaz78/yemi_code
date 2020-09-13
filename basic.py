# length = 100
# breath = 30

# area = length * breath

# print(area)
# p = 2(l + w)


def area_rectangle(length, breath):
    area = length * breath
    print(area)


area_rectangle(30, 40)
area_rectangle(10, 20)


# 2 X 1 = 2
# 2 X 2 = 4
# 2 X 3 = 6
# 2 X 4 = 8

for increement in range(1, 13):
    print(2, 'X', increement, '=', 2*increement)

print('FUNCTION BELOW')


def multiplication(number, start, stop):
    for start in range(start, stop+1):
        print(f"{number} X {start} = {number*start}")

multiplication(3, 10, 15)
print('4 TIMES')
multiplication(4, 5, 12)

total = 0
for number in range(1, 31):
    total += number
print(total)

# total = total + number

def add_range(lower, upper):
    total = 0
    for lower in range(lower, upper+1):
        total += lower
    print(total)


add_range(2, 10)