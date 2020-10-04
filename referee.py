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

    def valid_push_direction(target,push):
        if target.length() == 2:
            return push == target or push == target.substring(0,1) or push == target.substring(1,2)
        else:
            return push in target

    def unit_visible_to_player(unit,player):
        if not fog_of_war:
            return True
        for u in player.units:
            if u.position.distance(unit.position) <= view_distance:
                return True
        return False

    def get_neighbor(direction,position):
        x,y=position.x,position.y

        if 'E' in direction:
            x = x + 1
        elif 'W' in direction:
            x = x - 1
        if 'S' in direction:
            y = y + 1
        elif 'S' in direction:
            y = y - 1

        return Point(x,y)

    def compute_move(unit,dir1,dir2):

        target = get_neighbor(dir1,unit.position)
        target_height = grid.get(target)
        if target_height == None:
            print("BadCoords"+" "+str(target.x)+" "+str(target.y))
        current_height = grid.get(unit.position)
        if target_height > current_height + 1:
            print("InvalidMove" + " " + str(current_height) + " " + str(target_height))
        if target_height >= final_height:
            print("MoveTooHigh" + " " + str(target.x) + " " + str(target.y))
        if get_unit_on_point(target).present():
            print("MoveOnUnit" + " " + str(target.x) + " " + str(target.y))

        place_target = get_neighbor(dir2, target)
        place_target_height = grid.get(place_target)
        if place_target_height == None:
            print("InvalidPlace" + " " + str(place_target.x) + " " + str(place_target.y))
        if place_target_height >= final_height:
            print("PlaceTooHigh" + " " + str(target_height))


        result = action_result(Action.move)
        result.move_target = target
        result.place_target = place_target

        #Optional < Unit > possibleUnit = getUnitOnPoint(placeTarget).filter(u -> !u.equals(unit))

        if not possibleUnit.present():
            result.place_valid = True
            result.move_valid = True
        elif fog_of_war and not unit_visible_to_player(possibleUnit.get(), unit.player):
            result.place_valid = False
            result.move_valid = True
        else:
            print("PlaceOnUnit" + " " + str(place_target.x) + " " + str(place_target.y))

        if target_height == final_height - 1:
            result.score_point = True
        result.unit = unit

        return result



    def compute_push(unit,dir1,dir2) :

        if not valid_push_direction(dir1, dir2):
            print("PushInvalid" + " " + str(dir1) + " " + str(dir2))
        target = get_neighbor(dir1, unit.position)

        #Optional < Unit > maybePushed = getUnitOnPoint(target);

        if not maybePushed.present():
            print("PushVoid" + " " + str(target.x) + " " + str(target.y))
        pushed = maybePushed.get()

        if pushed.player == unit.player :
            print("FriendlyFire" + " " + str(unit.index) + " " + str(pushed.index))

        push_to = get_neighbor(dir2, pushed.position)
        to_height = grid.get(push_to)
        from_height = grid.get(target)

        if to_height == null or to_height >= final_height or to_height > from_height + 1:
            print("PushInvalid" + " " + str(dir1) + " " + str(dir2))

        result = action_result(Action.push)
        result.move_target = push_to
        result.place_target = target

        #Optional < Unit > possibleUnit = getUnitOnPoint(pushTo);

        if not possibleUnit.present():
            result.place_valid = True
            result.move_valid = True
        elif fog_of_war and not unit_visible_to_player(possibleUnit.get(), unit.player):
            result.place_valid = False
            result.move_valid = False

        else:
            print("PushOnUnit" + " " + str(dir1) + " " + str(dir2))

        result.unit = pushed

        return result


    def compute_action(command,unit,dir1,dir2):

        if command.equal_ignore_case(Action.move):
            return compute_move(unit, dir1, dir2)
        else if (can_push and command == Action.push):
            return compute_push(unit, dir1, dir2)

        else:
            print("InvalidCommand" + " " + str(command))
