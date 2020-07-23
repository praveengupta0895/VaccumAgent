from utils import distance_squared, turn_heading
from statistics import mean

import random
import copy
import collections


class Agent(Thing):

    def __init__(self):
        self.alive = True  # running or not
        self.bump = False  # ?
        self.holding = []
        self.performance = 0

        if program is None or not isinstance(program, collections.Callable):
            print("Can't find a valid program for {}, falling back to default.".format(
                self.__class__.__name__))

            def program(percept):
                return eval(input('Percept={}; action?'.format(percept)))

        self.program = program

    def can_grab(self, thing):
        # can grab the thing or not
        return False


def TraceAgent(agent):
    old_program = agent.program

    def new_program(percept):
        action = old_program(percept)
        print('{} perceived {} and does {}'.format(agent, percept, action))
        return action

    agent.program = new_program
    return agent


# random choice agent
def RandomAgentProgram(actions):
    return lambda percept: random.choice(actions)


loc_A, loc_B = (0, 0), (1, 0)  # vaccum world locations (2)


def RandomVaccumAgent():
    return Agent(RandomAgentProgram['Right', 'Left', 'Suck', 'NoOp'])


class Environment:
    def __init__(self):
        self.things = []
        self.agents = []

    def thing_classes(self):
        return []

    def percept(self, agent):
        # ?
        raise NotImplementedError

    def execute_action(self, agent, action):
        # ?
        raise NotImplementedError

    def default_location(self, thing):
        return None
