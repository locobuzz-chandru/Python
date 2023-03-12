nodes = []
graph = []
node_count = 0


def add_node(node):
    global node_count
    if node in nodes:
        return f'{node} is already present in the graph'
    node_count = node_count + 1
    nodes.append(node)
    for row_list in graph:
        row_list.append(0)
    temp = []
    for columns in range(node_count):
        temp.append(0)
    graph.append(temp)


# unweighted
def add_edge_unweighted(node1, node2):
    if node1 not in nodes:
        return f'{node1} is not present in the graph'
    elif node2 not in nodes:
        return f'{node2} is not present in the graph'
    else:
        index1 = nodes.index(node1)
        index2 = nodes.index(node2)
        graph[index1][index2] = 1
        graph[index2][index1] = 1


# weighted
def add_edge_weighted(node1, node2, cost):
    if node1 not in nodes:
        return f'{node1} is not present in the graph'
    elif node2 not in nodes:
        return f'{node2} is not present in the graph'
    else:
        index1 = nodes.index(node1)
        index2 = nodes.index(node2)
        graph[index1][index2] = cost
        graph[index2][index1] = cost


def delete_node(node):
    global node_count
    if node not in nodes:
        return f'{node} is not present in the graph'
    else:
        index1 = nodes.index(node)
        node_count = node_count - 1
        nodes.remove(node)
        graph.pop(index1)  # deletes row
        for row_list in graph:
            row_list.pop(index1)


def delete_edge(node1, node2):
    if node1 not in nodes:
        return f'{node1} is not present in the graph'
    elif node2 not in nodes:
        return f'{node2} is not present in the graph'
    else:
        index1 = nodes.index(node1)
        index2 = nodes.index(node2)
        graph[index1][index2] = 0
        graph[index2][index1] = 0


def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j], "<5"), end=' ')
        print()


add_node("A")
add_node("B")
add_node("C")
add_node("D")
print(nodes)
# print(graph)
# add_edge_unweighted("A", "C")
# add_edge_unweighted("D", "C")
add_edge_weighted("A", "C", 10)
add_edge_weighted("D", "C", 8)
add_edge_weighted("A", "B", 5)
add_edge_weighted("A", "D", 12)
add_edge_weighted("B", "C", 15)
print_graph()
# print()
# delete_node("B")
# print_graph()
# delete_edge("B", "C")
# print_graph()
