import heapq
from copy import deepcopy

GOAL_STATE = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

class Puzzle:
    def __init__(self, state, parent=None, move="", depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth

    def __lt__(self, other):
        return False

    def display(self):
        for row in self.state:
            print(row)
        print()

    def is_goal(self):
        return self.state == GOAL_STATE

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def generate_successors(self):
        successors = []
        x, y = self.find_blank()

        moves = {
            "Up": (x - 1, y),
            "Down": (x + 1, y),
            "Left": (x, y - 1),
            "Right": (x, y + 1)
        }

        for move, (new_x, new_y) in moves.items():
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = deepcopy(self.state)
                moved_tile = new_state[new_x][new_y]

                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]

                successors.append(Puzzle(
                    new_state,
                    parent=self,
                    move=f"Move {moved_tile} {move}",
                    depth=self.depth + 1
                ))

        return successors


def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                target_x = (value - 1) // 3
                target_y = (value - 1) % 3
                distance += abs(i - target_x) + abs(j - target_y)
    return distance


def a_star(initial_state):
    start = Puzzle(initial_state)
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(start.state), start))

    visited = set()

    while open_list:
        _, current = heapq.heappop(open_list)

        if current.is_goal():
            return current

        visited.add(tuple(map(tuple, current.state)))

        for neighbor in current.generate_successors():
            state_tuple = tuple(map(tuple, neighbor.state))

            if state_tuple not in visited:
                cost = neighbor.depth + manhattan_distance(neighbor.state)
                heapq.heappush(open_list, (cost, neighbor))

    return None


def print_solution(goal_node):
    path = []
    while goal_node:
        path.append(goal_node)
        goal_node = goal_node.parent

    path.reverse()

    print("Solution Steps:\n")
    for i, node in enumerate(path):
        if i == 0:
            print("Initial State:")
        else:
            print(f"Move {i}: {node.move}")
        node.display()


initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

goal_node = a_star(initial_state)

if goal_node:
    print_solution(goal_node)
else:
    print("No solution found.")