input = open("inputs/day1.txt", 'r')

values = input.read().splitlines()

times = 0
prev = int(values[0]) + int(values[1]) + int(values[2])

for i in range(len(values) - 2):
    curr = int(values[i]) + int(values[i + 1]) + int(values[i + 2])
    if (curr > prev):
        times += 1
    prev = curr

print(times)