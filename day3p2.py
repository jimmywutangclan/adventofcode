def oxygen(values, idx):
    if len(values) == 1:
        return values

    zeroes = [num for num in values if num[idx] == '0']
    ones = [num for num in values if num[idx] == '1']

    if (len(ones) >= len(zeroes)):
        return oxygen(ones, idx + 1)
    else:
        return oxygen(zeroes, idx + 1)
    

def carbon(values, idx):
    if len(values) == 1:
        return values

    zeroes = [num for num in values if num[idx] == '0']
    ones = [num for num in values if num[idx] == '1']

    if (len(ones) >= len(zeroes)):
        return carbon(zeroes, idx + 1)
    else:
        return carbon(ones, idx + 1)

input = open("inputs/day3.txt", 'r')
values = input.read().splitlines()

oxygenVal = int(oxygen(values, 0)[0], 2)
carbonVal = int(carbon(values, 0)[0], 2)

print(oxygenVal * carbonVal)

