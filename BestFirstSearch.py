import Graph
import Node


def heuristic(node, goal):
    # Example heuristic: assume all nodes are the same distance to goal
    return 1

def best_first_search(graph, start_name, goal_name):
    start = graph.get_node(start_name)
    goal = graph.get_node(goal_name)
    queue = [(heuristic(start, goal), start)]  # (heuristic, node)
    visited = set()

    while queue:
        # Find the node with the lowest heuristic value
        min_index = 0
        for i in range(1, len(queue)):
            if queue[i][0] < queue[min_index][0]:
                min_index = i

        h, node = queue.pop(min_index)
        print(f"Visiting: {node.name} with heuristic: {h}")

        if node == goal:
            print(f"Goal {goal.name} found!")
            return True

        if node not in visited:
            visited.add(node)
            for neighbor, _ in node.neighbors:
                if neighbor not in visited:
                    queue.append((heuristic(neighbor, goal), neighbor))

    return False

# Example usage:
g = Graph.Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('E', 'F')

best_first_search(g, 'A', 'F')