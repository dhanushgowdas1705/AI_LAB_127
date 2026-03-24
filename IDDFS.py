def dls(graph, node, target, depth, visited):
    if depth < 0:
        return False
    if node == target:
        return True
    visited.add(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            if dls(graph, neighbor, target, depth - 1, visited):
                return True
    return False

def iddfs(graph, start, target, max_depth):
    for depth in range(max_depth + 1):
        visited = set()
        print(f"Searching at depth: {depth}")
        if dls(graph, start, target, depth, visited):
            print(f"Found target {target} at depth {depth}")
            return True
    print("Target not found within depth limit")
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

iddfs(graph, 'A', 'G', max_depth=5)