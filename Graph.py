class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_edge(self, start, end, weight):
        if start not in self.adjacency_list:
            self.adjacency_list[start] = []
        if end not in self.adjacency_list:
            self.adjacency_list[end] = []
        
        self.adjacency_list[start].append((end, weight))
        self.adjacency_list[end].append((start, weight))
    
    def get_neighbors(self, node):
        return self.adjacency_list.get(node, [])
