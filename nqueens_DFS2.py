import sys


def IsGood(queens, row, col, n):
    # kt cot, bo vao tung hang nen ko can kt hang
    for i in range(n):
        if(queens[i][row] == 1):
            return False
    # kt duong cheo tren trai
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if(queens[i][j] == 1):
            return False
    # kt duong cheo duoi phai
    for i, j in zip(range(row, n, 1), range(col, n, 1)):
        if(queens[i][j] == 1):
            return False
    # kt duong cheo duoi trai
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if(queens[i][j] == 1):
            return False
    # kt duong cheo tren phai
    for i, j in zip(range(row, -1, -1), range(col, n, 1)):
        if(queens[i][j] == 1):
            return False
    return True


def solve(queens, row, col, n):
    if(row >= n or col >= n):
        return True
    if(IsGood(queens, row, col, n) == True):
        queens[row][col] = 1
        for i in range(n):
            if(i != col):
                if(solve(queens, row + 1, i, n) == True):
                    return True
        queens[row][col] = 0
    return False


def print2dArray(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            sys.stdout.write('%d ' % arr[i][j])
        sys.stdout.write('\n')


def main():
    n = 4  # int(input("Nhap n = "))
    count = 1
    for col in range(n):
        init = [[0 for i in range(n)] for j in range(n)]
        if(solve(init, 0, col, n) == True):
            print("Ket qua %d:" % count)
            print2dArray(init)
            count += 1


main()
