import unittest

from node import Node
from wondev_woman import Cell, 

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


class MyTestCase(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
