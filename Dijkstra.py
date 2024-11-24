class Dijkstra:
    def __init__(self, graph):
        self.graph = graph

    def find_shortest_path(self, start, end):
       
        # Distancias iniciales a infinito para todos los nodos excepto el inicial
        distances = {node: float('inf') for node in self.graph.adjacency_list}
        distances[start] = 0

        # Diccionario para rastrear la ruta más corta
        previous_nodes = {node: None for node in self.graph.adjacency_list}

        # Nodos no visitados
        unvisited = list(self.graph.adjacency_list.keys())

        while unvisited:
            # Seleccionar el nodo con la menor distancia en el conjunto de no visitados
            current_node = min(unvisited, key=lambda node: distances[node])

            # Si llegamos al nodo final, podemos detenernos
            if current_node == end:
                break

            # Actualizar distancias a los vecinos del nodo actual
            for neighbor, weight in self.graph.get_neighbors(current_node):
                if neighbor in unvisited:
                    new_distance = distances[current_node] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        previous_nodes[neighbor] = current_node

            # Marcar el nodo actual como visitado
            unvisited.remove(current_node)

        # Reconstruir el camino más corto
        path = []
        current = end
        while current is not None:
            path.insert(0, current)
            current = previous_nodes[current]

        return distances[end], path
