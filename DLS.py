tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

def dls(node, visited, limit, depth):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        if depth == limit:
            return

        for neighbor in tree[node]:
            dls(neighbor, visited, limit, depth + 1)

visited = set()
print("DLS Traversal:")
dls(1, visited, 2, 0)