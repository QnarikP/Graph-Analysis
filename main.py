from graph import Graph
from utils import get_graph_from_user, display_paths, display_cycle_info
from visualization import visualize_graph, save_graph_image

def main():
    # Default graph data
    default_edges = [(0, 1), (1, 2), (2, 3), (3, 5), (3, 4), (1, 4), (4, 2)]
    default_weights = [2, 4, 6, 8, 10, 1, 3]
    default_complexities = [1, 3, 2, 5, 4, 2, 1]
    
    choice = input("Would you like to use the default graph (y/n)? ").strip().lower()
    
    if choice == 'y':
        edges, weights, complexities = default_edges, default_weights, default_complexities
    else:
        edges, weights, complexities = get_graph_from_user()

    graph = Graph(edges, weights, complexities)
    
    source_nodes, intermediate_nodes, sink_nodes = graph.classify_nodes()
    print(f"Source Nodes: {source_nodes}")
    print(f"Intermediate Nodes: {intermediate_nodes}")
    print(f"Sink Nodes: {sink_nodes}")
    
    paths = graph.find_shortest_paths(source_nodes, sink_nodes)
    display_paths(paths)
    
    has_cycle, cycle = graph.detect_cycle()
    display_cycle_info(has_cycle, cycle)
    
    visualize_graph(graph)
    save_graph_image(graph, filename='graph.png')

if __name__ == "__main__":
    main()
