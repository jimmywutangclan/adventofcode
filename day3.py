
def decimal(binary):
    toReturn = 0

    for i in range(len(binary)):
        digit = 0
        power = (len(binary) - 1) - i

        if binary[i] == '1':
            digit = 1

        toReturn += (2 ** power) * digit


    return toReturn

def gamma(values):
    binaryNum = []
    
    bits = len(values[0])
    zeroes = 0
    ones = 0

    for i in range(bits):
        zeroes = 0
        ones = 0

        for value in values:
            if value[i] == '0':
                zeroes += 1
            if value[i] == '1':
                ones += 1
            
        if zeroes > ones:
            binaryNum.append('0')
        else:
            binaryNum.append('1')

    return binaryNum

def epsilon(binary):
    binaryNum = []

    for digit in binary:
        if digit == '0':
            binaryNum.append('1')
        if digit == '1':
            binaryNum.append('0')

    return binaryNum

input = open("inputs/day3.txt", 'r')
values = input.read().splitlines()

gammaList = gamma(values)
epsilonList = epsilon(gammaList)

print(decimal(gammaList) * decimal(epsilonList))