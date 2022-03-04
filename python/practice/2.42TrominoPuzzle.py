'''
연습문제 2.42: 트로미노 퍼즐(Divide and Conquer)
- 정사각형이 3개 붙어 있는 것을 트로미노(tromino)라고 한다.
- 가로와 세로로 m개의 정사각형이 연결되어 있는 바둑판이 있고,
  1칸은 X표시가 되어 있다. 여기서 m은 2의 거듭제곱이라고 가정한다.

- 다음 조건을 만족하도록 트로미노를 바둑판에 채우고 싶다.
    - X 표시가 되어 있는 칸은 트로미노로 덮을 수 없다.
    - 트로미노는 겹쳐 놓을 수 없다.
    - 트로미노는 바둑판 바깥으로 삐져나올 수 없다.
    - 바둑판 전체를 트로미노로 채워야 한다.

- 입력과 출력
    - 입력: m = 4, row = 1, col = 1
    - 출력: 각 트로미노에 번호를 부여하여 빈 칸 채우기

- 분할 정복
    - 분할: 4개의 사분면으로 분할
    - X가 없는 사분면의 모서리 채우기
- 정복: 채워진 네 개의 사분면을 재귀 호출
'''


def tromino(board, sRow, sCol, xRow, xCol, size):
    if (size == 1):
        return
    else:
        mRow = sRow + (size // 2)
        mCol = sCol + (size // 2)
        xRow1, xCol1 = mRow - 1, mCol           # 제1사분면
        xRow2, xCol2 = mRow - 1, mCol - 1       # 제2사분면
        xRow3, xCol3 = mRow, mCol - 1           # 제3사분면
        xRow4, xCol4 = mRow, mCol               # 제4사분면
        
        # 제 1 사분면 일 경우
        if (xRow < mRow and xCol >= mCol):
            fillCenterExcept(board, mRow, mCol, 1)
            xRow1, xCol1 = xRow, xCol

        # 제 2 사분면 일 경우
        elif(xRow < mRow and xCol < mCol):
            fillCenterExcept(board, mRow, mCol, 2)
            xRow2, xCol2 = xRow, xCol
        # 제 3 사분면 일 경우
        elif(xRow >= mRow and xCol < mCol):
            fillCenterExcept(board, mRow, mCol, 3)
            xRow3, xCol3 = xRow, xCol
        # 제 4 사분면 일 경우
        elif(xRow >= mRow and xCol >= xCol):
            fillCenterExcept(board, mRow, mCol, 4)
            xRow4, xCol4 = xRow, xCol
        
        tromino(board, sRow, mCol, xRow1, xCol1, size // 2) # 제1사분면
        tromino(board, sRow, sCol, xRow2, xCol2, size // 2) # 제2사분면
        tromino(board, mRow, sCol, xRow3, xCol3, size // 2) # 제3사분면
        tromino(board, mRow, mCol, xRow4, xCol4, size // 2) # 제4사분면
        
def fillCenterExcept(board, mRow, mCol, page):
    global count
    count += 1
    if (page != 1):
        board[mRow - 1][mCol] = count
    if (page != 2):
        board[mRow - 1][mCol - 1] = count
    if (page != 3):
        board[mRow][mCol - 1] = count
    if (page != 4):
        board[mRow][mCol] = count


def printBoard(board):
    for i in range(m):
        for j in range(m):
            if (board[i][j] < 0):
                print("%3s"%"x", end = " ")
            else:
                print("%3d"%board[i][j], end = " ")
        print()



import random
m = 4
xRow = random.randint(0, m - 1)
xCol = random.randint(0, m - 1)

board = [[0] * m for _ in range(m)]
board[xRow][xCol] = -1
count = 0
tromino(board, 0, 0, xRow, xCol, m)
printBoard(board)