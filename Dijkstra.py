def dijkstra(graph, start_node):
    # Inicializace vzdáleností na nekonečno pro všechny uzly kromě počátečního
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0

    unprocessed_nodes = set(graph)

    while unprocessed_nodes:
        current_node = min(unprocessed_nodes, key=lambda node: distances[node])

        for neighbor, weight in graph[current_node].items():
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

        # Označení aktuálního uzlu jako zpracovaného
        unprocessed_nodes.remove(current_node)

    return distances

# Příklad použití
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
result = dijkstra(graph, start_node)
print(result)
