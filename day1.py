input = open("inputs/day1.txt", 'r')

values = input.read().splitlines()

prev = int(values[0])
count = 0

for value in values:
    if int(value) > prev:
        count += 1
    prev = int(value)

print(count)