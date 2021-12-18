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

input = open("inputs/day4.txt", 'r')

values = [line.rstrip('\n') for line in input.read().splitlines() if line != '']

calls = values[0].split(',')

boards = []

# create boards
for i in range(1, len(values), 5):
    boards.append([])
    idx = len(boards) - 1
    boards[idx].append(values[i].split())
    boards[idx].append(values[i + 1].split())
    boards[idx].append(values[i + 2].split())
    boards[idx].append(values[i + 3].split())
    boards[idx].append(values[i + 4].split())

won = False
# make the number calls
for call in calls:
    # iterate through all boards
    for board in boards:
        # iterate through all the row
        for r in range(len(board)):
            # iterate through all cols within the row
            for c in range(len(board[r])):
                if (call == board[r][c]):
                    board[r][c] = 'x'
                    won = checkWin(board, r, c)
                    if won:
                        print(getSum(board) * int(call))
                        break
        if won: 
            break
    if won:
        break
