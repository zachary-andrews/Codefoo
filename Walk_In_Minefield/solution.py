from game import game
import random

def bogo(game):
    path = "I"
    # my_list = [game.move_north,game.move_east,game.move_south,game.move_west]
    while game.get_location() != game.get_end():
        options = []
        if game.check_east():
            options.append(game.move_east)
        if game.check_west():
            options.append(game.move_west)
        if game.check_north():
            options.append(game.move_north)
        if game.check_south():
            options.append(game.move_south)
        path += random.choice(options)()
        
    path+="-"
    return path

def optimized(game):   
    path = "I"
    while game.get_location() != game.get_end():
        current_location = game.get_location()
        if game.end[0] > current_location[0] and game.check_east():
                path += game.move_east()
        elif game.end[0] < current_location[0] and game.check_west():
                path += game.move_west()
        elif game.end[1] < current_location[1] and game.check_north():
                path += game.move_north()
        elif game.end[1] > current_location[1] and game.check_south():
                path += game.move_south()

    path += "-"
    return path

if __name__ == "__main__":
    game1 = game()
    bogo_path = bogo(game1)
    print("Bogo solution finished in "+ str(len(bogo_path)) + " moves. \nWith a path of: " + bogo_path + "\n")
    game2 = game()
    op_path = optimized(game2)
    print("Optimized solution finished in "+ str(len(op_path)) + " moves. \nWith a path of: " + op_path)