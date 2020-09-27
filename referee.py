class Referee:

    def ComputeMove(unit,dir1,dir2):

        target = getNeigghbor(dir1,unit.position)
        targetHeight = grid.get(target)
        if targetHeight == None:
            print("BadCoords"+" "+str(target.x)+" "+str(target.y))
        currentHeight = grid.get(unit.position)
        if targetHeight > currentHeight + 1:
            print("InvalidMove" + " " + str(currentHeight) + " " + str(targetHeight))
        if targetHeight >= FINAL_HEIGHT:
            print("MoveTooHigh" + " " + str(target.x) + " " + str(target.y))
        if getUnitOnPoint(target).isPresent():
            print("MoveOnUnit" + " " + str(target.x) + " " + str(target.y))

        placeTarget = getNeighbor(dir2, target)
        placeTargetHeight = grid.get(placeTarget)
        if placeTargetHeight == None:
            print("InvalidPlace" + " " + str(placeTarget.x) + " " + str(placeTarget.y))
        if placeTargetHeight >= FINAL_HEIGHT:
            print("PlaceTooHigh" + " " + str(targetHeight))


        result = ActionResult(Action.MOVE)
        result.moveTarget = target
        result.placeTarget = placeTarget

        #Optional < Unit > possibleUnit = getUnitOnPoint(placeTarget).filter(u -> !u.equals(unit))

        if not possibleUnit.isPresent():
            result.placeValid = True
            result.moveValid = True
        elif FOG_OF_WAR and not unitVisibleToPlayer(possibleUnit.get(), unit.player):
            result.placeValid = False
            result.moveValid = True
        else:
            print("PlaceOnUnit" + " " + str(placeTarget.x) + " " + str(placeTarget.y))

        if targetHeight == FINAL_HEIGHT - 1:
            result.scorePoint = true
        result.unit = unit

        return result



    def computePush(unit,dir1,dir2) :

        if not validPushDirection(dir1, dir2):
            print("PushInvalid" + " " + str(dir1) + " " + str(dir2))
        target = getNeighbor(dir1, unit.position)

        #Optional < Unit > maybePushed = getUnitOnPoint(target);

        if not maybePushed.isPresent():
            print("PushVoid" + " " + str(target.x) + " " + str(target.y))
        pushed = maybePushed.get()

        if pushed.player == unit.player :
            print("FriendlyFire" + " " + str(unit.index) + " " + str(pushed.index))

        pushTo = getNeighbor(dir2, pushed.position)
        toHeight = grid.get(pushTo)
        fromHeight = grid.get(target)

        if toHeight == null or toHeight >= FINAL_HEIGHT or toHeight > fromHeight + 1:
            print("PushInvalid" + " " + str(dir1) + " " + str(dir2))

        result = ActionResult(Action.PUSH)
        result.moveTarget = pushTo
        result.placeTarget = target

        #Optional < Unit > possibleUnit = getUnitOnPoint(pushTo);

        if not possibleUnit.isPresent():
            result.placeValid = true
            result.moveValid = true
        elif FOG_OF_WAR and not unitVisibleToPlayer(possibleUnit.get(), unit.player):
            result.placeValid = false
            result.moveValid = false

        else:
            print("PushOnUnit" + " " + str(dir1) + " " + str(dir2))

        result.unit = pushed

        return result


    def computeAction(command,unit,dir1,dir2)

    if command.equalsIgnoreCase(Action.MOVE):
        return computeMove(unit, dir1, dir2);
    else if (CAN_PUSH & & command.equals(Action.PUSH):
        return computePush(unit, dir1, dir2);

    else:
        print("InvalidCommand" + " " + str(command))
