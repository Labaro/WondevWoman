class Action(object):
    def __init__(self, index, dir_1, dir_2):
        self.index = index
        self.dir_1 = dir_1
        self.dir_2 = dir_2

class MoveAction(Action):
    def __init__(self, index, dir_1, dir_2):
        super().__init__(index, dir_1, dir_2)

    def __str__(self):
        return f"MOVE&BUILD {self.index} {self.dir_1} {self.dir_2}"

    def __repr__(self):
        return f"MOVE&BUILD {self.index} {self.dir_1} {self.dir_2}"


class PushAction(Action):
    def __init__(self, index, dir_1, dir_2):
        super().__init__(index, dir_1, dir_2)

    def __str__(self):
        return f"PUSH&BUILD {self.index} {self.dir_1} {self.dir_2}"

    def __repr__(self):
        return f"PUSH&BUILD {self.index} {self.dir_1} {self.dir_2}"

