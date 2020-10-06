class Node(object):
    """Node object is a box to handle tree exploration. All information about the game are store in the state object."""

    def __init__(self, state):
        self.state = state
        self.children = []
        self.value = 0

    def __hash__(self):
        return self.state.__hash__()

    def __eq__(self, other):
        return self.state.__eq__(other.state)

    def get_children(self):
        for action in self.state.get_actions():
            self.children.append(Node(self.state.simulate(action)))
        return self.children

    def evaluate(self):
        return self.state.evaluate()

    def is_terminal(self):
        return self.state.is_terminal()

    def negamax(self, depth):
        if depth == 0 or self.is_terminal():
            self.value = self.evaluate()
            return self.value
        children = self.get_children()
        value = -1e17
        for child in children:
            value = max(value, -child.negamax(depth - 1))
        self.value = value
        return self.value

    def negamax_alpha_beta_pruning(self, depth, alpha, beta):
        if depth == 0 or self.is_terminal():
            self.value = self.evaluate()
            return self.evaluate()
        children = self.get_children()
        value = -1e17
        for child in children:
            value = max(value, -child.negamax_alpha_beta_pruning(depth - 1, -beta, -alpha))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        self.value = value
        return self.value
