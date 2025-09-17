"""
小组成员：
余沛翰 72510479 YuFish131416
岳佳璇 72512147 jiaxuan-yue
翁梓严 72510283 Hoopopi
赵海超 72515790 zhaohc1997
胡薛林 72510295 yeli13
"""


def is_win(game):
    # 简化的胜利判断
    for i in range(3):
        # 检查行
        if game[i][0] != ' ' and game[i][0] == game[i][1] == game[i][2]:
            return True
        # 检查列
        if game[0][i] != ' ' and game[0][i] == game[1][i] == game[2][i]:
            return True

    # 检查对角线
    if game[0][0] != ' ' and game[0][0] == game[1][1] == game[2][2]:
        return True
    if game[0][2] != ' ' and game[0][2] == game[1][1] == game[2][0]:
        return True

    return False


def main():
    game = [[' ' for _ in range(3)] for _ in range(3)]
    player1 = 'X'
    player2 = 'O'
    turn = 0  # 用0和1表示回合，更简单

    print("X: Player 1, O: Player 2")

    for n in range(9):
        current_player = player1 if turn == 0 else player2
        print(f"Player {turn + 1} ({current_player}): Which cell? Enter row and column (1-3):")

        try:
            i, j = map(int, input().split())
            if i < 1 or i > 3 or j < 1 or j > 3:
                print("Numbers must be between 1 and 3. Try again.")
                continue
        except:
            print("Please enter two numbers. Try again.")
            continue

        i -= 1
        j -= 1

        if game[i][j] != ' ':
            print("That cell is already taken. Try again.")
            continue

        game[i][j] = current_player

        # 显示棋盘
        for row in game:
            print(" ".join(row))

        if is_win(game):
            print(f"Player {turn + 1} wins!")
            break

        if n == 8:
            print("It's a tie!")
            break

        turn = 1 - turn  # 切换玩家 (0->1, 1->0)


if __name__ == "__main__":
    main()