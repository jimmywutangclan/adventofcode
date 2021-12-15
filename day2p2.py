input = open("inputs/day2.txt", 'r')

values = input.read().splitlines()

vertical = 0
horizontal = 0
aim = 0

for value in values:
    if "forward " in value:
        mag = value[8:]
        horizontal += int(mag)
        vertical += aim * int(mag)
    elif "down " in value:
        mag = value[5:]
        aim += int(mag)
    else:
        mag = value[3:]
        aim -= int(mag)

print(vertical * horizontal)