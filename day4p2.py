def checkWin(board, r, c): 
    # use all function to check condition within for all elements
    return all(board[i][c] == 'x' for i in range(len(board))) or all(board[r][i] == 'x' for i in range(len(board[r])))

def getSum(board):
    sum = 0
    for row in board:
        for val in row:
            if val != 'x':
                sum += int(val)
    
    return sum

# input parser
input = open("inputs/day4.txt", 'r')
values = [line.rstrip('\n') for line in input.read().splitlines() if line != '']
calls = values[0].split(',')

boards = []
winning_boards = []

# create boards
for i in range(1, len(values), 5):
    boards.append([])
    idx = len(boards) - 1
    boards[idx].append(values[i].split())
    boards[idx].append(values[i + 1].split())
    boards[idx].append(values[i + 2].split())
    boards[idx].append(values[i + 3].split())
    boards[idx].append(values[i + 4].split())
    winning_boards.append(False)

boardsLeft = len(boards)
# make the number calls
for call in calls:
    # iterate through all boards
    for i in range(len(boards)):
        if winning_boards[i]:
            continue
        else:
            # iterate through all the row
            for r in range(len(boards[i])):
                # iterate through all cols within the row
                for c in range(len(boards[i][r])):
                    if (call == boards[i][r][c]):
                        boards[i][r][c] = 'x'
                        won = checkWin(boards[i], r, c)
                        if won:
                            winning_boards[i] = True
                            boardsLeft -= 1
                            
                            if boardsLeft == 0:
                                print(getSum(boards[i]) * int(call))
                            break
        if boardsLeft == 0: 
            break
    if boardsLeft == 0:
        break
