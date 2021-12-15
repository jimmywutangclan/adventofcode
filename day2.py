input = open("inputs/day1.txt", 'r')

values = input.read().splitlines()

vertical = 0
horizontal = 0

for value in values:
    if "forward " in value:
        mag = value[8:]
        print(mag)
    elif "down " in value:
        mag = value[5:]
        print(mag)
    else:
        mag = value[3:]
        print(mag)