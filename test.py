import unittest

from action import MoveAction, PushAction
from node import Node
from state import State
from unit import Unit


class TestState(object):
    def __init__(self, value, final, actions):
        self.value = value
        self.final = final
        self.actions = actions
        self.eval = False

    def __repr__(self):
        return str(self.value)

    def is_terminal(self):
        return self.final

    def evaluate(self):
        self.eval = True
        return self.value

    def get_actions(self):
        return self.actions

    def simulate(self, action):
        return action


class TestNode(unittest.TestCase):
    def setUp(self):
        self.state1 = TestState(2, True, [])
        self.state2 = TestState(3, True, [])
        self.state3 = TestState(0, True, [])
        self.state4 = TestState(1, True, [])
        self.state5 = TestState(3, True, [])
        self.state6 = TestState(-3, True, [])
        self.state7 = TestState(-1, True, [])
        self.state8 = TestState(3, False, [self.state6, self.state7])
        self.state9 = TestState(-2, False, [self.state1, self.state2])
        self.state10 = TestState(0, False, [self.state3, self.state4])
        self.state11 = TestState(-3, False, [self.state5, self.state8])
        self.state12 = TestState(3, False, [self.state9, self.state10, self.state11])

        self.root = Node(self.state12)

    def test_alpha_pruning(self):
        self.root.negamax_alpha_beta_pruning(3, -1e17, 1e17)
        assert not self.state4.eval

    def test_beta_pruning(self):
        self.root.negamax_alpha_beta_pruning(3, -1e17, 1e17)
        assert not self.state7.eval

    def test_negamax_with_alpha_beta_pruning(self):
        self.root.negamax_alpha_beta_pruning(3, -1e17, 1e17)
        assert self.root.value == self.root.state.value

    def test_negamax(self):
        self.root.negamax(3)
        assert self.root.value == self.root.state.value


class TestStateMethods(unittest.TestCase):
    def setUp(self):
        grid1 = [[0 for x in range(8)] for y in range(8)]
        units1 = [Unit(2, 2, 1, 0), Unit(5, 5, 1, 1)]
        self.state1 = State(grid1, units1, 1)

        grid2 = [[0 for x in range(5)] for y in range(5)]
        units2 = [Unit(2, 2, 1, 0), Unit(3, 1, -1, 0)]
        self.state2 = State(grid2, units2, 1)

        self.move_action = MoveAction(0, "N", "S")
        self.push_action = PushAction(0, "NE", "N")

    def test_maximum_legal_actions(self):
        assert len(self.state1.get_legal_actions()) == 176

    def test_simulation_move(self):
        new_state = self.state2.simulate(self.move_action)
        unit_1, unit_2 = new_state.units
        assert unit_1.x == 2
        assert unit_1.y == 1
        assert unit_2.x == 3
        assert unit_2.y == 1
        final_grid = [[0 for x in range(5)] for y in range(5)]
        final_grid[2][2] = 1
        assert new_state.grid == final_grid

    def test_simulation_push(self):
        new_state = self.state2.simulate(self.push_action)
        unit_1, unit_2 = new_state.units
        assert unit_1.x == 2
        assert unit_1.y == 2
        assert unit_2.x == 3
        assert unit_2.y == 0
        final_grid = [[0 for x in range(5)] for y in range(5)]
        final_grid[1][3] = 1
        assert new_state.grid == final_grid

    def test_all_moves(self):
        for action in self.state2.get_legal_actions():
            self.state2.simulate(action)


if __name__ == '__main__':
    unittest.main()
