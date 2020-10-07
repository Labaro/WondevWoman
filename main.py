from agent import Agent, LocalAgent
from state import State
from unit import Unit

if __name__ == "__main__":
   agent_1 = LocalAgent(1)
   agent_2 = LocalAgent(-1)
   grid = [[0 for x in range(5)] for y in range(5)]
   units = [Unit(1,4,1,0), Unit(3,3,-1,0), Unit(3,1,1,1), Unit(1,0,-1,1)]
   agent_1.read_init(5, 2)
   agent_2.read_init(5, 2)
   turn = 0
   state = State(grid, units, 1, turn)
   while not state.is_terminal():
       print(f"Turn {state.turn}")
       print(f"Turn of player {agent_1.player}")
       agent_1.read_state(state)
       action = agent_1.commit(2)
       print(action)
       state = state.simulate(action)
       print('\n'.join([''.join(['{:3}'.format(item) for item in row])
                        for row in state.grid]))
       for unit in state.units:
           print(f"Unit {unit.index} of player {unit.player} in position ({unit.x}, {unit.y})")
       print(f"Turn {state.turn}")
       print(f"Turn of player {agent_2.player}")
       agent_2.read_state(state)
       action = agent_2.commit(2)
       print(action)
       state = state.simulate(action)
       print('\n'.join([''.join(['{:3}'.format(item) for item in row])
                        for row in state.grid]))
       for unit in state.units:
           print(f"Unit {unit.index} of player {unit.player} in position ({unit.x}, {unit.y})")

