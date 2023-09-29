from Map import Map_Obj


class Node():
    """
    Class to store information about each visited node
    """

    def __init__(self, parent, pos: list[int, int], g: int, h: int):
        self.pos = pos
        self.parent = parent
        self.g = g
        self.h = h

    def get_pos(self):
        return self.pos

    def get_f(self):
        return self.g + self.h


def a_star(map: Map_Obj):
    S = map.get_start_pos()
    G = map.get_goal_pos()

    # Init the open and closed list
    open_list = []
    closed_list = []
    open_list.append(Node(None, S, 0, manhattan(S, G)))

    while open_list:
        # Task 5 moving goal ticker
        if map.get_goal_pos != map.get_end_goal_pos:
            G = map.tick()
        # Sorting the open list to have lowest f-value on top
        open_list.sort(key=lambda x: x.get_f())
        # Getting the node with the lowest f-value
        q = open_list.pop(0)
        current_pos = q.get_pos()

        # Check if goal is reached
        if current_pos == G:
            break

        # Find neighbours/possible successors of current node
        neighbour_pos = [
            [current_pos[0], current_pos[1] - 1],
            [current_pos[0], current_pos[1] + 1],
            [current_pos[0] - 1, current_pos[1]],
            [current_pos[0] + 1, current_pos[1]]
        ]

        for pos in neighbour_pos:
            # Check if neighbour can be traversed
            if map.get_cell_value(pos) > 0:
                # Calculate the cost from the start to this position
                # get_cell_value will allow for maps with variable cell cost (Part 2)
                g = q.g + map.get_cell_value(pos)
                child = Node(q, pos, g, manhattan(pos, G))
                # Check if the possible successor node is already in the open or closed list
                if pos not in [item.get_pos() for item in open_list] and pos not in [item.get_pos() for item in closed_list]:
                    open_list.append(child)

        # map.set_cell_value(current_pos, 5)
        closed_list.append(q)

    if current_pos != G:
        print("No path to the goal!")
    else:
        # Trace back the path to find the fastest route
        path = []
        while q:
            path.insert(0, q.get_pos())
            q = q.parent
        for pos in path:
            if pos not in [S, G]:
                # Draw route onto map
                map.set_cell_value(pos, 5)
        map.show_map()


# Calculate the manhattan distance from pos to goal
def manhattan(pos: list[int, int], G: list[int, int]) -> int:
    x = abs(pos[0] - G[0])
    y = abs(pos[1] - G[1])
    return x + y


if __name__ == "__main__":
    task_1 = Map_Obj(1)
    a_star(task_1)

    task_2 = Map_Obj(2)
    a_star(task_2)

    task_3 = Map_Obj(3)
    a_star(task_3)

    task_4 = Map_Obj(4)
    a_star(task_4)

    task_5 = Map_Obj(5)
    a_star(task_5)
