import random
import sys


class Queen:
    row = None
    column = None
    value = None

    def __init__(self, row, column):
        self.row = row
        self.column = column


def CalculateValue(queens):
    for i in range(len(queens)):
        count = 0
        for j in range(len(queens)):
            if(i != j):
                if(queens[i].row == queens[j].row or queens[i].column == queens[j].column
                        or abs(queens[i].row - queens[j].row) == abs(queens[i].column - queens[j].column)):
                    count += 1
        queens[i].value = count
    return queens


def initQueens(n):
    queens = []
    for i in range(n):
        queens.append(Queen(i, 0))
    return queens


def EstimateValue(queens, row, column, i):
    value = 0
    for q in queens:
        if(q != queens[i]):
            if(q.row == row or q.column == column):
                value += 1
    return value


def IsDone(queens):
    for q in queens:
        if (q.value != 0):
            return False
    return True


def findQueens(array, queens):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if (array[i][j] == 1):
                q = Queen(i, j)
                queens.append(q)
    return queens


def moveBackToRightRow(queens):
    do = True
    while(1):
        for i in range(len(queens)):
            if(queens[i].row != i):
                queens = moveVertical(queens, len(
                    queens), i - queens[i].row, i)
        for i in range(len(queens)):
            if(queens[i].row != i):
                do = False
                break
        if(do == True):
            break
    return queens


def moveVertical(queens, N, a, index):
    moved_row = queens[index].row + a
    if (moved_row < 0 or moved_row > N - 1):
        return queens
    for q in queens:
        if (q != queens[index]):
            if(q.row == moved_row and q.column == queens[index].column):
                return queens
    queens[index].row = moved_row
    return queens


def moveHorizontal(queens, N, a, index):
    moved_column = queens[index].column + a
    if(moved_column < 0 or moved_column > N - 1):
        return queens
    for q in queens:
        if(q != queens[index]):
            if(q.column == moved_column and q.row == queens[index].row):
                return queens
    queens[index].column = moved_column
    return queens


def moveSlant(queens, N, row, column, index):
    if (abs(row) != abs(column)):
        return queens
    moved_row = queens[index].row + row
    moved_column = queens[index].column + column
    if(moved_row < 0 or moved_row > N - 1):
        return queens
    for q in queens:
        if(q != queens[index]):
            if(q.column == moved_column and q.row == moved_row):
                return queens
    queens[index].row = moved_row
    queens[index].column = moved_column
    return queens


def solveProblem(n):
    queens = initQueens(n)
    queens = CalculateValue(queens)
    i = 0
    while(1):
        min_a = -queens[i].column
        max_a = n - queens[i].column
        a = random.randint(min_a, max_a)
        #evalue = EstimateValue(queens, queens[i].row, queens[i].column + a, i)
        # if (evalue < queens[i].value):
        queens = moveHorizontal(queens, n, a, i)
        queens = CalculateValue(queens)
        if(IsDone(queens) == True):
            break
        i = (i + 1) % n
    return queens


def convert2array(queens):
    ans = [[0 for x in range(len(queens))] for y in range(len(queens))]
    for i in range(len(queens)):
        ans[queens[i].row][queens[i].column] = 1
    return ans


def print2dArray(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            sys.stdout.write('%d ' % arr[i][j])
        sys.stdout.write('\n')


def main():
    n = int(input("Input n = "))
    if(1 < n < 4):
        print("Solution does not exist")
    else:
        init = [[0 for i in range(n)] for j in range(n)]
        for k in range(n):
            init[k][0] = 1

        ans = solveProblem(n)
        end = convert2array(ans)
        print2dArray(end)


main()
