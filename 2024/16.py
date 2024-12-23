# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:27:51 2024

@author: schiltem93
"""
import numpy as np
import heapq
#%% PART 1
lines = []
with open('input/input16.txt', 'r') as file:
# with open('input/example.txt', 'r') as file:
    for line in file:
        lines.append(list(line.strip()))
# %%


matrix = np.array(lines)
start = tuple(np.argwhere(matrix == "S")[0])
end = tuple(np.argwhere(matrix == "E")[0])



def find_shortest_path(maze, start, end):
    # Directions: dy, dx, direction name
    directions = [
        (-1, 0, "NS"),  # Up
        (1, 0, "NS"),   # Down
        (0, -1, "WE"),  # Left
        (0, 1, "WE")    # Right
    ]

    # Priority queue: (score, y, x, direction)
    pq = [(0, start[0], start[1], "WE")]
    visited = set()

    while pq:
        score, current_y, current_x, direction = heapq.heappop(pq)

        # Check if reached the endpoint
        if maze[current_y, current_x] == "E":
            return score

        # Mark the cell as visited
        visited.add((current_y, current_x, direction))

        # Explore neighbors
        for dy, dx, new_direction in directions:
            new_y, new_x = current_y + dy, current_x + dx

            # Skip out-of-bounds or wall cells
            if not (0 <= new_y < maze.shape[0] and 0 <= new_x < maze.shape[1]):
                continue
            if maze[new_y, new_x] == "#":
                continue

            # Skip already visited states
            if (new_y, new_x, new_direction) in visited:
                continue

            # Calculate the new score
            new_score = score + (1001 if direction != new_direction and direction else 1)

            # Add to the priority queue
            heapq.heappush(pq, (new_score, new_y, new_x, new_direction))

    # If no path found
    return float("inf")
# Solve for the shortest path
shortest_score = find_shortest_path(matrix, start, end)
print("Shortest Score:", shortest_score)

# %% Part 2


matrix = np.array(lines)
start = tuple(np.argwhere(matrix == "S")[0])
end = tuple(np.argwhere(matrix == "E")[0])



def find_shortest_paths(maze, start, end):
    # Directions: dy, dx, direction name
    directions = [
        (-1, 0, "NS"),  # Up
        (1, 0, "NS"),   # Down
        (0, -1, "WE"),  # Left
        (0, 1, "WE")    # Right
    ]

    # Priority queue: (score, y, x, direction, path)
    pq = [(0, start[0], start[1], "WE", [(start[0], start[1])])]
    visited = set()
    
    best_paths = set()
    best_score = None

    while pq:
        score, current_y, current_x, direction, path = heapq.heappop(pq)
        # Check if reached the endpoint
        if best_score:
            if score > best_score:
                return best_paths
        if maze[current_y, current_x] == "E":
            print(path)
            best_score = score
            best_paths.update(path)

        # Mark the cell as visited
        visited.add((current_y, current_x, direction))

        # Explore neighbors
        for dy, dx, new_direction in directions:
            new_y, new_x = current_y + dy, current_x + dx

            # Skip out-of-bounds or wall cells
            if not (0 <= new_y < maze.shape[0] and 0 <= new_x < maze.shape[1]):
                continue
            if maze[new_y, new_x] == "#":
                continue

            # Skip already visited states
            if (new_y, new_x, new_direction) in visited:
                continue

            # Calculate the new score
            new_score = score + (1001 if direction != new_direction and direction else 1)
            new_path = path + [(new_y, new_x)]
            # Add to the priority queue
            heapq.heappush(pq, (new_score, new_y, new_x, new_direction, new_path))

    # If no path found
    return float("inf")
# Solve for the shortest path
print("Starting point:", start)
print("End point:", end)

shortest_paths = find_shortest_paths(matrix, start, end)
print("Shortest Paths:", len(shortest_paths))
