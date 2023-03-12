graph = {}


def add_node(node):
    if node in graph:
        return f'{node} is already present in the graph'
    graph[node] = []


def add_edge_unweighted(node1, node2):
    if node1 not in graph:
        return f'{node1} is not present in the graph'
    elif node2 not in graph:
        return f'{node2} is not present in the graph'
    graph[node1].append(node2)
    graph[node2].append(node1)


def add_edge_weighted(node1, node2, cost):
    if node1 not in graph:
        return f'{node1} is not present in the graph'
    elif node2 not in graph:
        return f'{node2} is not present in the graph'
    else:
        graph[node1].append([node2, cost])
        graph[node2].append([node1, cost])


def delete_unweighted_node(node):
    if node not in graph:
        return f'{node} is not present in the graph'
    else:
        graph.pop(node)
        for key in graph:
            values_list = graph[key]
            if node in values_list:
                values_list.remove(node)


def delete_weighted_node(node):
    if node not in graph:
        return f'{node} is not present in the graph'
    else:
        graph.pop(node)
        for key in graph:
            values_list = graph[key]
            for weighted_values_list in values_list:
                if node == weighted_values_list[0]:
                    values_list.remove(weighted_values_list)
                    break


# undirected graph
def delete_unweighted_edge(node1, node2):
    if node1 not in graph:
        return f'{node1} is not present in the graph'
    elif node2 not in graph:
        return f'{node2} is not present in the graph'
    else:
        if node2 in graph[node1]:
            graph[node1].remove(node2)
            graph[node2].remove(node1)


def delete_weighted_edge(node1, node2, cost):
    if node1 not in graph:
        return f'{node1} is not present in the graph'
    elif node2 not in graph:
        return f'{node2} is not present in the graph'
    else:
        if [node2, cost] in graph[node1]:
            graph[node1].remove([node2, cost])
            graph[node2].remove([node1, cost])


add_node("A")
add_node("B")
add_node("C")
add_node("D")
print(graph)
# add_edge_unweighted("A", "B")
# add_edge_unweighted("C", "B")
# print(graph)
# delete_unweighted_node("A")
# print(graph)
add_edge_weighted("A", "D", 10)
add_edge_weighted("C", "B", 8)
add_edge_weighted("A", "B", 6)
print(graph)
# delete_weighted_node("C")
# print(graph)
# delete_unweighted_edge("C", "B")
# print(graph)
# delete_weighted_edge("D", "A", 10)
# print(graph)
