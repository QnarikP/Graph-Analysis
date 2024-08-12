import matplotlib.pyplot as plt
import networkx as nx

def visualize_graph(graph):
    pos = nx.spring_layout(graph.graph_nx)
    weights = nx.get_edge_attributes(graph.graph_nx, 'weight')
    nx.draw(graph.graph_nx, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=14, font_weight='bold', edge_color='gray')
    nx.draw_networkx_edge_labels(graph.graph_nx, pos, edge_labels=weights)
    plt.show()

def save_graph_image(graph, filename='graph.png'):
    pos = nx.spring_layout(graph.graph_nx)
    weights = nx.get_edge_attributes(graph.graph_nx, 'weight')
    plt.figure(figsize=(10, 7))
    nx.draw(graph.graph_nx, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=14, font_weight='bold', edge_color='gray')
    nx.draw_networkx_edge_labels(graph.graph_nx, pos, edge_labels=weights)
    plt.savefig(filename)
    print(f"Graph saved as {filename}")
