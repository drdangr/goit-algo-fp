import uuid
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="#222222"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, color=node.color, label=node.val)

        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)

        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

    return graph

def draw_tree(root, ax, title=""):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(tree, root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    ax.set_title(title)
    nx.draw(
        tree,
        pos,
        labels=labels,
        node_color=colors,
        node_size=2500,
        arrows=False,
        ax=ax
    )



def generate_colors(n):
    start = 85    # ~ #555555 — тёмный, но читаемый
    end = 220     # ~ #dcdcdc — светлый

    colors = []
    for i in range(n):
        intensity = int(start + (end - start) * (i / max(1, n - 1)))
        hex_color = f"#{intensity:02x}{intensity:02x}{intensity:02x}"
        colors.append(hex_color)
    return colors

def bfs_traversal(root):
    queue = deque([root])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return order

def dfs_traversal(root):
    stack = [root]
    order = []

    while stack:
        node = stack.pop()
        order.append(node)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return order


def visualize_bfs_dfs(root):
    import copy

    # Чтобы цвета BFS не повлияли на DFS
    root_bfs = copy.deepcopy(root)
    root_dfs = copy.deepcopy(root)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # ===== BFS =====
    bfs_order = bfs_traversal(root_bfs)
    bfs_colors = generate_colors(len(bfs_order))
    for node, color in zip(bfs_order, bfs_colors):
        node.color = color

    draw_tree(root_bfs, axes[0], "BFS Traversal")

    # ===== DFS =====
    dfs_order = dfs_traversal(root_dfs)
    dfs_colors = generate_colors(len(dfs_order))
    for node, color in zip(dfs_order, dfs_colors):
        node.color = color

    draw_tree(root_dfs, axes[1], "DFS Traversal")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    visualize_bfs_dfs(root)