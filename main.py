from collections import deque


# Ханойская башня, двунаправленный поиск в ширину


def bfs(start, goal, moves):
    forward_queue = deque([(start, 0)])
    forward_visited = {start: 0}
    backward_queue = deque([(goal, 0)])
    backward_visited = {goal: 0}
    while forward_queue and backward_queue:
        if forward_queue[0][1] + backward_queue[0][1] > moves:
            return -1
        if forward_queue[0][0] in backward_visited:
            return forward_queue[0][1] + backward_visited[forward_queue[0][0]]
        if backward_queue[0][0] in forward_visited:
            return backward_queue[0][1] + forward_visited[backward_queue[0][0]]
        node, depth = forward_queue.popleft()
        for neighbor in get_neighbors(node):
            if neighbor not in forward_visited:
                forward_visited[neighbor] = depth + 1
                forward_queue.append((neighbor, depth + 1))
        node, depth = backward_queue.popleft()
        for neighbor in get_neighbors(node):
            if neighbor not in backward_visited:
                backward_visited[neighbor] = depth + 1
                backward_queue.append((neighbor, depth + 1))
    return -1


def get_neighbors(state):
    neighbors = []
    for i in range(len(state)):
        for j in range(len(state)):
            if i != j and (not state[i] or state[j] and state[i][-1] > state[j][-1]):
                new_state = list(state[:])
                new_state[i] = tuple(sorted(state[j] + new_state[i]))
                new_state[j] = tuple(state[j][:-1])
                neighbors.append(tuple(new_state))
    return neighbors


start = (tuple(range(3, 0, -1)), (), ())
goal = ((), (), tuple(range(3, 0, -1)))
moves = 10

print(bfs(start, goal, moves))