import sys
def goodplace(queens, row, col, n):
    #insert tu trai qua phai nen kiem tra trai du roi
    #kt hang o khoang trai
    for i in range(col):
        if(queens[row][i] == 1):
            return False
    #kt duong cheo tren trai
    for i,j in zip(range(row, -1, -1), range(col, -1, -1)):
        if(queens[i][j] == 1):
            return False
    #kt duong cheo duoi trai
    for i,j in zip(range(row, n, 1), range(col, -1, -1)):
        if(queens[i][j] == 1):
            return False
    return True

def solve(queens, column, n):
    if(column >= n):
        return True
    for i in range(n):
        #neu dat vi tri ok
        if(goodplace(queens, i, column, n) == True):
            queens[i][column] = 1
            #kt xem co dan toi ket qua ko
            if(solve(queens, column + 1, n) == True):
                return True
            #ko thi huy buoc
            queens[i][column] = 0
    return False

def print2dArray(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            sys.stdout.write('%d ' % arr[i][j])
        sys.stdout.write('\n')

def main():
    n = int(input("Nhap n = "))
    init = [[0 for i in range(n)] for j in range(n)]
    if(solve(init, 0, n) == False):
        print("Khong co ket qua!")
    print2dArray(init)
    
        
main()
    

