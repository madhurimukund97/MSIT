'''game'''
def tic_tac_toe(mat):
    '''tic tac toe game'''
    win = []
    for row in mat:
        if row[0] == row[1] == row[2]:
            win.append(row[0])
    for ind in range(0, 3):
        if mat[0][ind] == mat[1][ind] == mat[2][ind]:
            win.append(mat[0][ind])
    if mat[0][0] == mat[1][1] == mat[2][2]:
        win.append(mat[0][0])
    if mat[2][0] == mat[1][1] == mat[0][2]:
        win.append(mat[0][2])
    if len(win) is 0:
        print('draw')
        return None
    if len(win) == 1:
        if win[0] == 'x' or win[0] == 'o':
            print(win[0])
        else:
            print("invalid input")
        return win[0]
    else:
        print("invalid game")
        return None
def main():
    '''main'''
    list1 = []
    for _ in range(0, 3):
        cols = input().split(' ')
        list1.append(cols)
    tic_tac_toe(list1)
if __name__ == '__main__':
    main()
