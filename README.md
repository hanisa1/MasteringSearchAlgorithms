# Search Algorithms in Python 🌟

![Search Algorithms](https://github.com/user-attachments/assets/e6628244-1103-4281-93cc-a1da067a4e3f)

Welcome to the **Search Algorithms in Python** repository! This project contains various implementations of fundamental search algorithms, including Depth-First Search (DFS), Breadth-First Search (BFS), Uniform Cost Search (UCS), and Best First Search, all written in clean, simple Python without any external libraries.

## Table of Contents

- [Introduction](#introduction)
- [Algorithms](#algorithms)
  - [Depth-First Search (DFS)](#depth-first-search-dfs)
  - [Breadth-First Search (BFS)](#breadth-first-search-bfs)
  - [Uniform Cost Search (UCS)](#uniform-cost-search-ucs)
  - [Best First Search](#best-first-search)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Search algorithms are a fundamental aspect of computer science, playing a critical role in problem-solving across various domains. This repository offers a hands-on exploration of these algorithms, providing both theoretical insights and practical Python implementations.

## Algorithms

### Depth-First Search (DFS)

DFS is a search algorithm that explores a graph by starting at the root node and exploring as far as possible along each branch before backtracking.

- **Use Cases:** Solving mazes, puzzle games, topological sorting.
- **Time Complexity:** O(V + E)
- **Space Complexity:** O(V)

### Breadth-First Search (BFS)

BFS is a search algorithm that explores all the nodes at the present depth level before moving on to the nodes at the next depth level.

- **Use Cases:** Finding the shortest path in unweighted graphs, web crawlers, social networking searches.
- **Time Complexity:** O(V + E)
- **Space Complexity:** O(V)

### Uniform Cost Search (UCS)

UCS is an extension of BFS that considers the cost of the path, making it suitable for finding the lowest-cost path.

- **Use Cases:** Route planning, AI decision-making, robotics navigation.
- **Time Complexity:** O(V + E)
- **Space Complexity:** O(V)

### Best First Search

Best First Search uses a heuristic to determine the most promising path, balancing exploration and exploitation.

- **Use Cases:** AI pathfinding (e.g., A*), puzzle solving, game AI.
- **Time Complexity:** O(V + E)
- **Space Complexity:** O(V)

## Contributing
Contributions are welcome! Whether you're fixing bugs, improving documentation, or adding new features, feel free to submit a pull request.

Fork the repository.
Create your feature branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -am 'Add YourFeature').
Push to the branch (git push origin feature/YourFeature).
Open a pull request.

## License
This project is licensed under the MIT License—see the LICENSE file for details.
