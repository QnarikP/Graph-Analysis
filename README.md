```markdown
# Graph Analysis Project

## Project Overview

This project is a Python implementation for analyzing directed graphs. It includes functionalities like contour detection, calculating metrics for different node classifications (source, intermediate, and sink nodes), and finding the shortest paths based on weights and complexities.

## Installation Instructions

1. **Clone the Repository**:
   ```bash
   git clone <https://github.com/yourusername/graph-analysis.git>
   cd graph-analysis

```

1. **Install Dependencies**:
    
    ```bash
    pip install -r requirements.txt
    
    ```
    

## Usage Guide

1. Run the main script:
    
    ```bash
    python main.py
    
    ```
    
2. Input the edges of your graph interactively.
3. View the graph visualization in the pop-up window or find the saved graph image `graph_visualization.png` in the project directory.
4. The program will display calculated metrics and detect any contours in the graph.

## Code Structure

- `main.py`: Main script to run the program.
- `graph.py`: Contains the Graph class and related functions.
- `visualization.py`: Functions for visualizing and saving the graph.
- `utils.py`: Utility functions for input handling and miscellaneous calculations.

## Visualization Examples

![graph_visualization.png](graph_visualization.png)