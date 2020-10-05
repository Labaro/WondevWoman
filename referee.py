class Referee:

    game_version = 0
    got_pushed = 2
    did_push = 1
    no_push = 0
    final_height = 4
    generated_map_size = 6
    win_on_max_height = True
    can_push = False
    unit_per_player = 1
    fog_of_war = False
    view_distance = 1


    def compute_move(game,unit,dir1,dir2):

        ''' Compute the decision when move and build '''

        # target cell
        target_position = unit.position.convert_direction(dir1)
        target_height = game.get_cell(target_position).state.height

        # target cell is dead ?
        if isinstance(game.get_cell(target_position).state,DeadCell):
            print("Bad move"+" "+str(target.x)+" "+str(target.y),file = sys.stderr)
            return False

        # build cell
        place_target_position = target.convert_direction(dir2)
        place_target_height = game.get_cell(place_target_position).state.height

        # build cell is dead
        if isinstance(game.get_cell(place_target_position).state,DeadCell):
            print("Bad place"+" "+str(target.x)+" "+str(target.y),file = sys.stderr)
            return False

        # update
        unit.position = target_position
        game.get_cell(place_target_position).state.height += 1

        if target_height == final_height - 1:
            player.score += 1



    def compute_push(game,unit,dir1,dir2) :

        ''' Compute the decision when moveandpush '''

        # target cell
        target_position = unit.position.convert_direction(dir1)

        # target cell is dead ?
        if isinstance(game.get_cell(target_position).state, DeadCell):
            print("Bad move" + " " + str(target.x) + " " + str(target.y), file=sys.stderr)
            return False

        # Finding the pushed unit
        for unit in game.other_units:
            if unit.position == target_position:
                unit_pushed = unit

        # push cell
        push_to_position = unit_pushed.position.convert_direction(dir2)
        to_height = game.get_cell(push_to_position).state.height
        from_height = game.get_cell(target_position).state.height

        # target cell is dead ?
        if isinstance(game.get_cell(push_to_position).state, DeadCell):
            print("Bad push" + " " + str(target.x) + " " + str(target.y), file=sys.stderr)
            return False

        # Update
        unit.position = target_position
        unit_pushed.position = push_to_position

        if from_height == final_height - 1:
            player.score += 1

        if to_height == final_height - 1:
            player_other.score += 1


