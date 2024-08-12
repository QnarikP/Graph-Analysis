import numpy as np
import networkx as nx

class Graph:
    def __init__(self, edges_list, weights=None, complexities=None):
        self.edges = edges_list
        self.weights = weights if weights else [1] * len(edges_list)
        self.complexities = complexities if complexities else [1] * len(edges_list)
        self.start_nodes = [edge[0] for edge in edges_list]
        self.end_nodes = [edge[1] for edge in edges_list]
        self.graph_nx = self.create_networkx_graph()

    def classify_nodes(self):
        source_nodes = list(set([i for i in self.start_nodes if i not in self.end_nodes]))
        sink_nodes = [i for i in self.end_nodes if i not in self.start_nodes]
        intermediate_nodes = list(set(self.start_nodes) - set(source_nodes) - set(sink_nodes))
        return source_nodes, intermediate_nodes, sink_nodes

    def create_adjacency_matrix(self):
        max_node = max(max(edge) for edge in self.edges)
        adj_matrix = np.zeros((max_node + 1, max_node + 1))
        for edge, weight in zip(self.edges, self.weights):
            adj_matrix[edge[0], edge[1]] = weight
        return adj_matrix[1:, 1:]

    def compute_reachability(self):
        matrix_powers = [self.create_adjacency_matrix()]
        reachability_matrix = matrix_powers[0].copy()
        contour_detected = False

        for i in range(1, len(self.edges)):
            matrix_powers.append(np.dot(matrix_powers[i-1], matrix_powers[0]))
            reachability_matrix += matrix_powers[i]
            if np.diagonal(matrix_powers[i]).sum() != 0:
                contour_detected = True
                break

        return matrix_powers, reachability_matrix, contour_detected
    
    def create_networkx_graph(self):
        G = nx.DiGraph()
        for edge, weight in zip(self.edges, self.weights):
            G.add_edge(edge[0], edge[1], weight=weight)
        return G

    def find_shortest_paths(self, source_nodes, sink_nodes):
        paths = {}
        for source in source_nodes:
            for sink in sink_nodes:
                if nx.has_path(self.graph_nx, source, sink):
                    path = nx.shortest_path(self.graph_nx, source=source, target=sink, weight='weight')
                    distance = nx.shortest_path_length(self.graph_nx, source=source, target=sink, weight='weight')
                    path_complexity = sum(self.complexities[self.edges.index((path[i], path[i+1]))] for i in range(len(path)-1))
                    paths[(source, sink)] = (path, distance, path_complexity)
        return paths

    def detect_cycle(self):
        try:
            cycle = nx.find_cycle(self.graph_nx, orientation='original')
            return True, cycle
        except nx.NetworkXNoCycle:
            return False, None
