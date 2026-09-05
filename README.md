# LeetCode 133 – Clone Graph

## Problem

Given a reference to a node in a connected **undirected graph**, return a deep copy of the graph.

Each graph node contains:

* A value
* A list of neighboring nodes

The cloned graph must contain completely new nodes while preserving the same connections as the original graph.

## Example 1

**Input:**

```text id="r8e5xj"
adjList = [[2,4],[1,3],[2,4],[1,3]]
```

**Output:**

```text id="n3b2am"
[[2,4],[1,3],[2,4],[1,3]]
```

The cloned graph has the same structure and connections as the original graph, but all nodes are newly created.

## Example 2

**Input:**

```text id="v8by4g"
adjList = [[]]
```

**Output:**

```text id="x7df4oa"
[[]]
```

The graph contains one node with no neighbors.

## Example 3

**Input:**

```text id="w9f5xq"
adjList = []
```

**Output:**

```text id="g4m8x2"
[]
```

An empty graph is returned as empty.

## Approach

The graph may contain cycles, so simply creating a copy of every neighbor can result in infinite recursion.

To avoid this, we use a **Hash Map** to store the relationship between original nodes and their cloned nodes.

For every original node:

```text
Original Node → Cloned Node
```

When we encounter a node again, we return its already-created clone instead of creating another one.

The graph can be traversed using either **DFS** or **BFS**.

## Algorithm

1. If the input node is `None`, return `None`.
2. Create a hash map to store original-to-cloned node relationships.
3. Start DFS or BFS from the given node.
4. When a new node is encountered:

   * Create its clone.
   * Store the mapping in the hash map.
5. Visit each neighbor of the original node.
6. Connect the cloned node to the corresponding cloned neighbors.
7. Continue until all reachable nodes are copied.
8. Return the clone of the starting node.

## Complexity

Let `V` be the number of vertices and `E` be the number of edges.

* **Time Complexity:** `O(V + E)`
* **Space Complexity:** `O(V)`

Each node and edge is processed once, while the hash map stores one clone for every node.

## Key Learning

This problem demonstrates how **graph traversal** can be combined with a **Hash Map** to create a deep copy.

The most important concept is keeping track of already-cloned nodes, especially when the graph contains cycles.

## LeetCode Details

* **Problem Number:** 133
* **Problem Name:** Clone Graph
* **Difficulty:** Medium
* **Language:** Python 3
* **File:** `solution.py`

## Topics

* Hash Table
* Depth-First Search
* Breadth-First Search
* Graph

## Author

T.Nandhini
