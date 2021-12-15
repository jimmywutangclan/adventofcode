input = open("inputs/day2.txt", 'r')

values = input.read().splitlines()

vertical = 0
horizontal = 0

for value in values:
    if "forward " in value:
        mag = value[8:]
        horizontal += int(mag)
    elif "down " in value:
        mag = value[5:]
        vertical += int(mag)
    else:
        mag = value[3:]
        vertical -= int(mag)

print(vertical * horizontal)