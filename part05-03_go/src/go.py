# Write your solution here

def who_won(game_board: list):
    points_one = 0
    points_two = 0

    for row in game_board:
        for square in row:
            if square == 1:
                points_one += 1
            elif square == 2:
                points_two += 1
    
    if points_one > points_two:
        return 1

    elif points_two > points_one:
        return 2

    else:
        return 0