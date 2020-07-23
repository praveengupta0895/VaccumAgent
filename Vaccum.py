import numpy as np
from matplotlib import pyplot as plt
from enum import Enum


class Action(Enum):
    ABOVE = 1
    BELOW = 2
    LEFT = 3
    RIGHT = 4
    ASPIRAR = 5
    NOOP = 6


class Block(Enum):
    WALL = 1
    DIRT = 2
    CLEAN = 3
    VACCUMCLEANER = 4


def Display(I):
    plt.imshow(I, 'gray')
    plt.show(block=False)
    plt.pause(0.5)
    plt.clf()


def Generate():
    rows = 4
    cols = 4
    low = 2
    high = 4
    step = 1

    matrix = np.random.choice([x for x in range(low, high, step)], rows * cols)
    matrix.resize(rows, cols)

    matrix = [(1, 1, 1, 1, 1, 1),
              (1, 4, matrix[0][1], matrix[0][2], matrix[0][3], 1),
              (1, matrix[1][0], matrix[1][1], matrix[1][2], matrix[1][3], 1),
              (1, matrix[2][0], matrix[2][1], matrix[2][2], matrix[2][3], 1),
              (1, matrix[3][0], matrix[3][1], matrix[3][2], matrix[3][3], 1),
              (1, 1, 1, 1, 1, 1)]
    return matrix


class VaccumCleaner:
    VaccumCleanerLine = 1
    VaccumCleanerColumn = 1
    Points = 0
    World = ()
    ObjectiveLine = -1
    ObjectiveColumn = -1

    def trigger(self, world):
        self.World = world

        while self.hasDirt():
            action = self.perceiveWorld()
            self.mover(action)
            plt.pause(0.1)
            Display(self.World)
            self.vaccumBlock()

    def mover(self, action):
        self.Points += 1
        print("My position: ", self.VaccumCleanerLine, self.VaccumCleanerColumn)
        print("Current points: ", self.Points)
        print("Moving to ", action)

        line = list(self.World[self.VaccumCleanerLine])
        line[self.VaccumCleanerColumn] = Block.CLEAN.value
        line = tuple(line)
        self.World[self.VaccumCleanerLine] = line

        if action == Action.BELOW:
            self.VaccumCleanerLine = self.VaccumCleanerLine + 1
            line = list(self.World[self.VaccumCleanerLine])
            line[self.VaccumCleanerColumn] = Block.VACCUMCLEANER.value
            line = tuple(line)
            self.World[self.VaccumCleanerLine] = line
        elif action == Action.ABOVE:
            self.VaccumCleanerLine = self.VaccumCleanerLine - 1
            line = list(self.World[self.VaccumCleanerLine])
            line[self.VaccumCleanerColumn] = Block.VACCUMCLEANER.value
            line = tuple(line)
            self.World[self.VaccumCleanerLine] = line
        elif action == Action.RIGHT:
            self.VaccumCleanerColumn = self.VaccumCleanerColumn + 1
            line = list(self.World[self.VaccumCleanerLine])
            line[self.VaccumCleanerColumn] = Block.VACCUMCLEANER.value
            line = tuple(line)
            self.World[self.VaccumCleanerLine] = line
        elif action == Action.LEFT:
            self.VaccumCleanerColumn = self.VaccumCleanerColumn - 1
            line = list(self.World[self.VaccumCleanerLine])
            line[self.VaccumCleanerColumn] = Block.VACCUMCLEANER.value
            line = tuple(line)
            self.World[self.VaccumCleanerLine] = line
        else:
            print("Action not implemented")

    def hasDirt(self):
        for i in range(1, 6):
            lineTuple = self.World[i]
            for j in lineTuple:
                if j == Block.DIRT.value:
                    print("Moving to the dirt", i, j)
                    return True
        return False

    def perceiveWorld(self):
        for i in range(0, 5):
            lineTuple = self.World[i]
            for j in range(0, 5):
                if lineTuple[j] == Block.DIRT.value and self.blockDefinedAsObjective(i, j):
                    self.definedObjective(i, j)
                    if (self.VaccumCleanerLine - i) > 0:
                        return Action.ABOVE
                    elif (self.VaccumCleanerLine - i) < 0:
                        return Action.BELOW
                    elif (self.VaccumCleanerColumn - j) > 0:
                        return Action.LEFT
                    elif (self.VaccumCleanerColumn - j < 0):
                        return Action.RIGHT
        return Action.NOOP

    def definedObjective(self, line, Column):
        self.ObjectiveLine = line
        self.ObjectiveColumn = Column

    def blockDefinedAsObjective(self, line, Column):
        definedObjective = self.ObjectiveLine > -1
        blockDefinedAsObjective = self.ObjectiveLine == line and self.ObjectiveColumn == Column
        return blockDefinedAsObjective or (not definedObjective)

    def vaccumBlock(self):
        print('Aspiring')
        line = list(self.World[self.VaccumCleanerLine])
        line[self.VaccumCleanerColumn] = Block.CLEAN.value
        line = tuple(line)
        self.World[self.VaccumCleanerLine] = line
        if (self.VaccumCleanerColumn == self.ObjectiveColumn) and (self.VaccumCleanerLine == self.ObjectiveLine):
            self.ObjectiveLine = -1
            self.ObjectiveColumn = -1


def main():
    plt.show()
    plt.pause(0.001)
    world = Generate()
    Display(world)
    aspirador = VaccumCleaner()
    aspirador.trigger(world)
    exit()


main()
