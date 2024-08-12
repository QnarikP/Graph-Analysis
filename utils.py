def get_graph_from_user():
    edges = []
    weights = []
    complexities = []
    print("Enter edges in the format (start_node, end_node) or 'done' to finish:")
    
    while True:
        edge_input = input("Edge: ")
        if edge_input.lower() == 'done':
            break
        start_node, end_node = map(int, edge_input.strip('()').split(','))
        edges.append((start_node, end_node))
        
        weight = int(input(f"Enter weight for edge ({start_node}, {end_node}): "))
        weights.append(weight)
        
        complexity = int(input(f"Enter complexity for edge ({start_node}, {end_node}): "))
        complexities.append(complexity)
    
    return edges, weights, complexities

def display_paths(paths):
    for key, value in paths.items():
        print(f"Shortest path from {key[0]} to {key[1]}: {value[0]} with distance {value[1]} and complexity {value[2]}")

def display_cycle_info(has_cycle, cycle):
    if has_cycle:
        print(f"Cycle detected: {cycle}")
    else:
        print("No cycle detected.")