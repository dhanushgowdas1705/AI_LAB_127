def dfs(tree, node, visited=None):
    if visited is None:
        visited = []

    visited.append(node)

    for child in tree[node]:
        if child not in visited:
            dfs(tree, child, visited)

    return visited
tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}
result = dfs(tree, 1)

print("DFS Traversal:", *result)