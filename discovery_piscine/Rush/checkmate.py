def checkmate(board):
    board = board.strip().split("\n")
    n = len(board)

    # หาตำแหน่งคิง
    king_x, king_y = -1, -1
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                king_x, king_y = i, j

    # ฟังก์ชันเช็คขอบเขต ได้ตำแหน่งคิง
    def in_bounds(x, y):
        return 0 <= x < n and 0 <= y < n

    # Pawn เอาตำแหน่งคิงเทียบตำแหน่งในบอด
    for dx, dy in [(-1, -1), (-1, 1)]:
        x, y = king_x + dx, king_y + dy
        if in_bounds(x, y) and board[x][y] == 'P':
            print("Success")
            return

    # Rook + Queen (แนวตรง)
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        x, y = king_x + dx, king_y + dy
        while in_bounds(x, y):
            if board[x][y] != '.':
                if board[x][y] in ['R','Q']:
                    print("Success")
                    return
                break
            x += dx
            y += dy

    # Bishop + Queen (แนวทแยง)
    for dx, dy in [(-1,-1),(-1,1),(1,-1),(1,1)]:
        x, y = king_x + dx, king_y + dy
        while in_bounds(x, y):
            if board[x][y] != '.':
                if board[x][y] in ['B','Q']:
                    print("Success")
                    return
                break
            x += dx
            y += dy

    print("Fail")