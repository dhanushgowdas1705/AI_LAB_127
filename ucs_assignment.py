class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        self.queue.append((priority, item))

    def dequeue(self):
        self.queue.sort(key=lambda x: x[0])
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0


def uniform_cost_search(graph, start, goal):
    pq = PriorityQueue()
    pq.enqueue((start, [start], 0), 0)
    visited = set()

    while not pq.is_empty():
        cost, (node, path, _) = pq.dequeue()

        if node == goal:
            return cost, path

        if node in visited:
            continue

        visited.add(node)

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                pq.enqueue((neighbor, path + [neighbor], cost + weight), cost + weight)

    return None


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 1), ('E', 3)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

result = uniform_cost_search(graph, 'A', 'G')
print("Cost and Path:", result)