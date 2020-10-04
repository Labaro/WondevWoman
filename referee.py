class Referee:

    def compute_move(unit,dir1,dir2):

        target = neighbor(dir1,unit.position)
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

        place_target = neighbor(dir2, target)
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
            result.placeValid = True
            result.moveValid = True
        elif fog_of_war and not unit_visible_to_player(possibleUnit.get(), unit.player):
            result.placeValid = False
            result.moveValid = True
        else:
            print("PlaceOnUnit" + " " + str(place_target.x) + " " + str(place_target.y))

        if target_height == final_height - 1:
            result.score_point = True
        result.unit = unit

        return result



    def compute_push(unit,dir1,dir2) :

        if not validPushDirection(dir1, dir2):
            print("PushInvalid" + " " + str(dir1) + " " + str(dir2))
        target = neighbor(dir1, unit.position)

        #Optional < Unit > maybePushed = getUnitOnPoint(target);

        if not maybePushed.present():
            print("PushVoid" + " " + str(target.x) + " " + str(target.y))
        pushed = maybePushed.get()

        if pushed.player == unit.player :
            print("FriendlyFire" + " " + str(unit.index) + " " + str(pushed.index))

        push_to = neighbor(dir2, pushed.position)
        to_height = grid.get(push_to)
        from_height = grid.get(target)

        if to_height == null or to_height >= final_height or to_height > from_height + 1:
            print("PushInvalid" + " " + str(dir1) + " " + str(dir2))

        result = ActionResult(Action.push)
        result.move_target = push_to
        result.place_target = target

        #Optional < Unit > possibleUnit = getUnitOnPoint(pushTo);

        if not possibleUnit.present():
            result.place_valid = True
            result.move_valid = True
        elif fog_of_war and not unitVisibleToPlayer(possibleUnit.get(), unit.player):
            result.place_valid = False
            result.move_valid = False

        else:
            print("PushOnUnit" + " " + str(dir1) + " " + str(dir2))

        result.unit = pushed

        return result


    def compute_action(command,unit,dir1,dir2):

        if command.equal_ignore_case(Action.move):
            return compute_move(unit, dir1, dir2)
        else if (can_push and command.equals(Action.push):
            return compute_push(unit, dir1, dir2)

        else:
            print("InvalidCommand" + " " + str(command))
