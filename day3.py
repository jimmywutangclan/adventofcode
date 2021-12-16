from collections import Counter
from typing import List

# convert binary array to decimal int
def decimal(binary : List[str]) -> int:
    toReturn = 0

    for i in range(len(binary)):
        digit = 0
        power = (len(binary) - 1) - i

        if binary[i] == '1':
            digit = 1

        toReturn += (2 ** power) * digit


    return toReturn

# calculate the gamma
def gamma(values : List[str]) -> List[str]:
    binaryNum = []
    
    bits = len(values[0])
    
    for i in range(bits):
        counter = Counter(num[i] for num in values)
            
        if counter['0'] > counter['1']:
            binaryNum.append('0')
        else:
            binaryNum.append('1')

    return binaryNum

# invert the gamma array
def epsilon(binary : List[str]) -> List[str]:
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