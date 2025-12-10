# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 10:07:11 2025

@author: morit
"""


#%%
boxes = []
with open('input/8.txt', 'r') as file:
# with open('input/example.txt', 'r') as file:
    lines = file.read().strip().split("\n")
    for line in lines:
        boxes.append(list(map(int, line.split(","))))

    

print(boxes)
# for line in boxes:
    # print(line)
# print(grid)
    
# %% PART 1 Rabin by chatgpt

import random
import math
from itertools import product
from typing import List, Tuple, Optional

Point3D = Tuple[int, int, int]


def dist2_3d(p: Point3D, q: Point3D) -> int:
    """Squared Euclidean distance between two 3D integer points."""
    dx = p[0] - q[0]
    dy = p[1] - q[1]
    dz = p[2] - q[2]
    return dx*dx + dy*dy + dz*dz


def brute_force_threshold(points: List[Point3D],
                          min_dist2: float,
                          eps2: float) -> Tuple[float, Tuple[int, int]]:
    """
    Fallback: O(n^2) search for the smallest distance > min_dist
    (actually > min_dist^2 + eps2 in squared space).
    """
    n = len(points)
    best_d2 = float("inf")
    best_pair = (-1, -1)

    for i in range(n):
        for j in range(i + 1, n):
            d2 = dist2_3d(points[i], points[j])
            # enforce strict threshold with epsilon
            if d2 <= min_dist2 + eps2:
                continue
            if d2 < best_d2:
                best_d2 = d2
                best_pair = (i, j)

    if best_pair == (-1, -1):
        return float("inf"), (-1, -1)
    return math.sqrt(best_d2), best_pair


def closest_pair_rabin_3d(
    points: List[Point3D],
    min_dist: float = 0.0,
    num_samples: Optional[int] = None,
    seed: Optional[int] = None,
) -> Tuple[float, Tuple[int, int]]:
    """
    Rabin-style randomized closest-pair algorithm in 3D, extended with min_dist:

      -> returns the smallest distance STRICTLY GREATER than min_dist.

    Args:
        points: list of (x, y, z) integer points
        min_dist: ignore all pairs with distance <= min_dist
        num_samples: number of random pairs to sample
        seed: random seed (optional)

    Returns:
        (distance, (i, j)):
          - distance: smallest distance > min_dist (or inf if none)
          - i, j: indices into `points` (or -1, -1 if none)
    """
    n = len(points)
    if n < 2:
        raise ValueError("Need at least two points")

    if seed is not None:
        random.seed(seed)

    # Make sure all points are 3D
    for p in points:
        if len(p) != 3:
            raise ValueError("All points must be 3D (x, y, z)")

    # Work with squared distances; add a small epsilon to enforce "strictly greater"
    min_dist2 = float(min_dist) * float(min_dist)
    eps2 = 1e-6  # you can tweak this; it's in "squared distance" units

    # ----------------------------------------------------------------------
    # 1. Random sampling to get an upper bound on the next distance > min_dist
    # ----------------------------------------------------------------------
    if num_samples is None:
        num_samples = n

    best_sampled_d2 = float("inf")

    for _ in range(num_samples):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        if i == j:
            continue

        d2 = dist2_3d(points[i], points[j])

        # Only consider distances strictly larger than the threshold
        if d2 <= min_dist2 + eps2:
            continue

        if d2 < best_sampled_d2:
            best_sampled_d2 = d2

    # If sampling didn't find any pair above threshold, fall back to O(n^2)
    if best_sampled_d2 == float("inf"):
        return brute_force_threshold(points, min_dist2, eps2)

    # Use sampled distance as grid cell size
    d = math.sqrt(best_sampled_d2)

    # ----------------------------------------------------------------------
    # 2. Build 3D grid with cell size = d
    # ----------------------------------------------------------------------
    def cell_index(p: Point3D) -> Tuple[int, int, int]:
        return (
            int(math.floor(p[0] / d)),
            int(math.floor(p[1] / d)),
            int(math.floor(p[2] / d)),
        )

    cell_to_points: dict[Tuple[int, int, int], List[int]] = {}
    for idx, p in enumerate(points):
        c = cell_index(p)
        cell_to_points.setdefault(c, []).append(idx)

    # ----------------------------------------------------------------------
    # 3. Check only within each cell and its neighbors
    # ----------------------------------------------------------------------
    neighbor_offsets = list(product([-1, 0, 1], repeat=3))

    best_d2 = float("inf")
    best_pair = (-1, -1)

    for i, p in enumerate(points):
        c = cell_index(p)

        for off in neighbor_offsets:
            neighbor_cell = (c[0] + off[0], c[1] + off[1], c[2] + off[2])

            if neighbor_cell not in cell_to_points:
                continue

            for j in cell_to_points[neighbor_cell]:
                if j <= i:
                    continue

                d2 = dist2_3d(points[i], points[j])

                # enforce the threshold with epsilon
                if d2 <= min_dist2 + eps2:
                    continue

                if d2 < best_d2:
                    best_d2 = d2
                    best_pair = (i, j)

    # If grid pass failed (should be rare), fallback
    if best_pair == (-1, -1):
        return brute_force_threshold(points, min_dist2, eps2)

    return math.sqrt(best_d2), best_pair


# %% 

connected = set()
circuits = []
depth = 1000
min_distance = 0

for i in range(depth):
    print("Min distance:", min_distance)
    d, (x, y) = closest_pair_rabin_3d(boxes, min_distance, seed=42)
    print("Closest distance:", d, "pair:", boxes[x], boxes[y])
    # print(x,y)
    min_distance = d
    if x in connected and y in connected:
        x_circ_id = None
        y_circ_id = None
        for i in range(len(circuits)):            
            if x_circ_id and y_circ_id:
                break
            if x in circuits[i]:
                x_circ_id = i
            if y in circuits[i]:
                y_circ_id = i
        if x_circ_id != y_circ_id:
            circuits[x_circ_id] = circuits[x_circ_id].union(circuits[y_circ_id])
            circuits.pop(y_circ_id)

        
    elif x in connected:
        print("hello")
        x_circ_id = None
        for i in range(len(circuits)):            
            if x_circ_id:
                break
            if x in circuits[i]:
                x_circ_id = i
        connected.add(y)
        circuits[x_circ_id].add(y)

    elif y in connected:
        y_circ_id = None
        for i in range(len(circuits)):            
            if y_circ_id:
                break
            if y in circuits[i]:
                y_circ_id = i
        connected.add(x)
        circuits[y_circ_id].add(x)

    else:
        connected.add(x)
        connected.add(y)
        circuits.append(set((x,y)))
    for circ in circuits:
        print(circ)

            
print("Number of circuits:", len(circuits))
for circ in circuits:
    print(len(circ))
print("Number of single circuits:", depth-len(circuits))

# 162,817,812 and 425,690,689
# 162,817,812 and 431,825,988
# 906,360,560 and 805,96,715
# 431,825,988 and 425,690,689
result = math.prod(sorted((len(s) for s in circuits), reverse=True)[:3])
print("Length of 3 longest circuits", result)

# %% PART 2 convex hull by chatgpt

import numpy as np
from scipy.spatial import ConvexHull
from typing import List, Tuple
from typing import List, Tuple


Point3D = Tuple[int, int, int]

def convex_hull_3d(points: List[Point3D]):
    """
    Compute the 3D convex hull of a set of points using scipy.spatial.ConvexHull.

    Returns:
        vertex_indices: sorted list of indices of points on the hull (in original list)
        faces: list of triangular faces (triples of point indices)
        hull_points: list of points on the hull
    """
    pts = np.array(points, dtype=float)
    n = len(pts)

    if n == 0:
        return [], [], []
    if n <= 3:
        vertex_indices = list(range(n))
        return vertex_indices, [], [points[i] for i in vertex_indices]

    hull = ConvexHull(pts)

    vertex_indices = sorted(set(hull.vertices.tolist()))
    faces = [tuple(face) for face in hull.simplices]
    hull_points = [points[i] for i in vertex_indices]

    return vertex_indices, faces, hull_points




def most_isolated_points(points: List[Point3D], n: int):
    """
    Find the n points that are most distant from all other points,
    in the sense of having the largest distance to their nearest neighbor.

    Candidate points are restricted to the convex hull (outer layer),
    but nearest neighbors are searched among *all* points.

    Returns:
        A list of tuples:
        [
            (
                nn_dist,        # distance to nearest neighbor (float)
                idx_global,     # index of the isolated point in `points`
                p,              # coordinates of the isolated point (Point3D)
                nn_idx_global,  # index of its nearest neighbor in `points`
                nn_point        # coordinates of its nearest neighbor (Point3D)
            ),
            ...
        ]
        sorted from most isolated (largest nn_dist) to less isolated.
    """
    if n <= 0 or not points:
        return []

    # 1) Compute convex hull and restrict to hull vertices
    hull_indices, faces, hull_points = convex_hull_3d(points)

    if len(hull_indices) <= 1:
        # No meaningful isolation with <= 1 hull point
        return []

    isolation_scores = []  # will hold the tuples described above
    N = len(points)

    # 2) For each hull point, compute distance to its nearest neighbor in **all** points
    for idx_global in hull_indices:
        p = points[idx_global]

        min_d2 = float("inf")
        nn_idx_global = -1

        for j in range(N):
            if j == idx_global:
                continue

            q = points[j]
            d2 = dist2_3d(p, q)
            if d2 < min_d2:
                min_d2 = d2
                nn_idx_global = j

        nn_dist = math.sqrt(min_d2)
        nn_point = points[nn_idx_global]
        isolation_scores.append(
            (nn_dist, idx_global, p, nn_idx_global, nn_point)
        )

    # 3) Sort by isolation (largest nearest-neighbor distance first) and take top n
    isolation_scores.sort(key=lambda t: t[0], reverse=True)
    return isolation_scores[:n]


    
# %% 

distant = most_isolated_points(boxes, n=1)
for nn_dist, idx, p, nn_idx, nn_p in distant:
    print(
    f"Point {p} (idx {idx}) has nearest neighbor {nn_p} (idx {nn_idx}) "
    f"at distance {nn_dist:.3f}"
    )
    print("x multiplication:", p[0]*nn_p[0])


# %%
import math
from typing import List, Tuple, Union

Point3D = Tuple[int, int, int]
CoordInput = Union[int, Tuple[int, int, int], List[int]]

def nn(points: List[List[int] | Tuple[int,int,int]], 
       target: CoordInput
) -> Tuple[float, int, List[int] | Tuple[int,int,int]]:
    """
    Nearest-neighbor distance for a point in a 3D list of points.
    Points may be lists or tuples.
    target may be an index or coordinates (list or tuple).
    """

    # Normalize all points internally to tuples for comparison
    points_as_tuples = [tuple(p) for p in points]

    # --- Case 1: target is index ---
    if isinstance(target, int):
        if not (0 <= target < len(points)):
            raise IndexError("Index out of range")
        p = points_as_tuples[target]
        target_index = target

    # --- Case 2: target is coordinates ---
    else:
        if len(target) != 3:
            raise ValueError("Coordinate must have length 3")

        p = tuple(target)

        # must exist (normalized)
        if p not in points_as_tuples:
            raise ValueError(f"Point {p} does not exist in the points list!")

        target_index = points_as_tuples.index(p)

    # --- Find nearest neighbor ---
    min_d2 = float("inf")
    nearest_index = -1

    for j, q in enumerate(points_as_tuples):
        if j == target_index:
            continue

        dx = p[0] - q[0]
        dy = p[1] - q[1]
        dz = p[2] - q[2]
        d2 = dx*dx + dy*dy + dz*dz

        if d2 < min_d2:
            min_d2 = d2
            nearest_index = j

    nearest_point = points[nearest_index]  # return original (list or tuple)
    return math.sqrt(min_d2), nearest_index, nearest_point

    # %%
nn(boxes, [216, 146, 977])

