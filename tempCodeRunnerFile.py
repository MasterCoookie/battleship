for idx in range(5):
    while(True):
        print(f'Place your {SHIP_NAMES[idx]} ({idx + 2} holes) on the board')
        print('Input the starting and edning grid coordinate of your ship')
        coordinate_1 = convert_input(input())
        coordinate_2 = convert_input(input())
        if coordinate_1 and coordinate_2 and player.player_board.add_ship(idx + 2, coordinate_1, coordinate_2):
            break