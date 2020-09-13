numbers = [1, 2, 3, 40, 5, 8, 'Slim']
new_numbers = []

for n in numbers:
    new_numbers.append(n)
print(new_numbers)


even_numbers = []
for e in range(1, 21):
    if e % 2 == 0:
        even_numbers.append(e)

print(even_numbers)


nums = [1, 2, 3, 4, 5, 'Slim']
print_numbers = [n for n in nums]
print(print_numbers)

list_even_numbers = [e for e in range(30) if e % 2 == 0]
print(list_even_numbers)




