# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 10:07:11 2025

@author: morit
"""


#%%
coordinates = []
with open('input/9.txt', 'r') as file:
# with open('input/example.txt', 'r') as file:
    for idx, line in enumerate(file, start=1):
        x, y = map(int, line.strip().split(","))
        coordinates.append({
            "id": idx,
            "x": x,
            "y": y
        })

print(coordinates)

# %% PART 1
import math

from itertools import combinations

def largest_n(coords, n_percent, mode="x"):
    pairs = []

    # All combinations of two distinct points
    for p1, p2 in combinations(coords, 2):
        x_dist = abs(p1["x"] - p2["x"])
        y_dist = abs(p1["y"] - p2["y"])
        pairs.append({
            "id1": p1["id"],
            "id2": p2["id"],
            "x_dist": x_dist,
            "y_dist": y_dist,
        })

    if not pairs:
        return []

    key_name = "x_dist" if mode == "x" else "y_dist"

    pairs.sort(key=lambda d: d[key_name], reverse=True)

    k = max(1, math.ceil((n_percent / 100.0) * len(pairs)))
    top_pairs = pairs[:k]

    result = []
    for p in top_pairs:
        product = (p["x_dist"]+1) * (p["y_dist"]+1)
        result.append({
            "id1": p["id1"],
            "id2": p["id2"],
            "x_dist": p["x_dist"],
            "y_dist": p["y_dist"],
            "product": product,
        })

    return result

def largest(results):
    if not results:
        return None

    return max(item["product"] for item in results)


x_products = largest_n(coordinates, 50, mode="x")
y_products = largest_n(coordinates, 50, mode="x")

products= x_products + y_products
print(largest(products))


# %% PART 2 

import math
from collections import defaultdict


coordinates = []
with open('input/9.txt', 'r') as file:
# with open('input/example.txt', 'r') as file:
    for idx, line in enumerate(file, start=1):
        x, y = map(int, line.strip().split(","))
        coordinates.append((x,y))


print(coordinates)


def bresenham_points(x0, y0, x1, y1):
    """All integer grid points on the segment (x0,y0)->(x1,y1), inclusive."""
    points = []
    dx = abs(x1 - x0)
    dy = -abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx + dy

    x, y = x0, y0
    while True:
        points.append((x, y))
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x += sx
        if e2 <= dx:
            err += dx
            y += sy

    return points


def compute_boundary(vertices):
    """Corners + all edge points."""
    n = len(vertices)
    boundary = set()
    for i in range(n):
        x0, y0 = vertices[i]
        x1, y1 = vertices[(i + 1) % n]
        for p in bresenham_points(x0, y0, x1, y1):
            boundary.add(p)
    return boundary


def merge_intervals(intervals):
    """Merge overlapping/touching closed intervals [(a,b), ...] -> merged."""
    if not intervals:
        return []
    intervals.sort()
    merged = [intervals[0]]
    for a, b in intervals[1:]:
        la, lb = merged[-1]
        if a <= lb + 1:  # touch/overlap
            merged[-1] = (la, max(lb, b))
        else:
            merged.append((a, b))
    return merged


def scanline_fill_intervals(vertices):
    """
    Interior fill using scanlines at y+0.5 to avoid vertex double-counting.
    Returns: dict[y] = list of closed x-intervals (x_start, x_end) for interior points.
    """
    n = len(vertices)
    ys = [y for _, y in vertices]
    min_y, max_y = min(ys), max(ys)

    filled = defaultdict(list)

    # For each integer y row, compute intersections with scanline y + 0.5
    for y in range(min_y, max_y + 1):
        y_scan = y + 0.5
        x_intersections = []

        for i in range(n):
            x1, y1 = vertices[i]
            x2, y2 = vertices[(i + 1) % n]

            # Ignore horizontal edges for intersection logic
            if y1 == y2:
                continue

            # Ensure y1 < y2
            if y1 > y2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1

            # Half-open rule: include y1 <= y_scan < y2
            if y1 <= y_scan < y2:
                t = (y_scan - y1) / (y2 - y1)
                x = x1 + t * (x2 - x1)
                x_intersections.append(x)

        x_intersections.sort()

        # Fill between pairs of intersections
        for j in range(0, len(x_intersections), 2):
            if j + 1 >= len(x_intersections):
                break
            xl = x_intersections[j]
            xr = x_intersections[j + 1]

            # Integer x values strictly inside between crossings:
            # Use ceil(left) .. floor(right)
            x_start = math.ceil(min(xl, xr))
            x_end = math.floor(max(xl, xr))

            if x_start <= x_end:
                filled[y].append((x_start, x_end))

        filled[y] = merge_intervals(filled[y])

    return dict(filled)


def eligible_space(vertices):
    """
    Returns boundary_points (set) and interior_intervals (dict[y] -> list[(x0,x1)]).
    Eligible = boundary ∪ interior.
    """
    boundary = compute_boundary(vertices)
    interior = scanline_fill_intervals(vertices)
    return boundary, interior


def point_is_filled(x, y, boundary, interior_intervals):
    """Check membership without expanding all points."""
    if (x, y) in boundary:
        return True
    intervals = interior_intervals.get(y)
    if not intervals:
        return False
    # intervals are merged, sorted
    for a, b in intervals:
        if a <= x <= b:
            return True
        if x < a:
            return False
    return False


def visualize(vertices, boundary, interior_intervals, pad=1, crop=None):
    """
    ASCII visualization.
    - '#' eligible (boundary or interior), '.' empty
    - crop=(min_x, max_x, min_y, max_y) to limit output for huge inputs
    """
    xs = [x for x, _ in vertices]
    ys = [y for _, y in vertices]
    min_x, max_x = min(xs) - pad, max(xs) + pad
    min_y, max_y = min(ys) - pad, max(ys) + pad

    if crop is not None:
        min_x, max_x, min_y, max_y = crop

    for y in range(max_y, min_y - 1, -1):
        row = []
        for x in range(min_x, max_x + 1):
            row.append("#" if point_is_filled(x, y, boundary, interior_intervals) else ".")
        print("".join(row))



#%%
from collections import defaultdict

def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort()
    merged = [intervals[0]]
    for a, b in intervals[1:]:
        la, lb = merged[-1]
        if a <= lb + 1:  # touch/overlap
            merged[-1] = (la, max(lb, b))
        else:
            merged.append((a, b))
    return merged


def runs_to_intervals(sorted_xs):
    """Convert sorted x points into merged closed intervals."""
    if not sorted_xs:
        return []
    intervals = []
    start = prev = sorted_xs[0]
    for x in sorted_xs[1:]:
        if x == prev + 1:
            prev = x
        else:
            intervals.append((start, prev))
            start = prev = x
    intervals.append((start, prev))
    return intervals


def build_eligible_row_intervals(boundary_points, interior_intervals):
    """
    boundary_points: set[(x,y)]
    interior_intervals: dict[y] -> list[(x0,x1)]  (already merged is fine)

    Returns dict[y] -> merged list[(x0,x1)] covering all eligible points in that row.
    """
    row_xs = defaultdict(list)
    for x, y in boundary_points:
        row_xs[y].append(x)

    eligible_rows = {}

    all_ys = set(interior_intervals.keys()) | set(row_xs.keys())
    for y in all_ys:
        intervals = []
        # boundary as intervals
        xs = row_xs.get(y)
        if xs:
            xs.sort()
            intervals.extend(runs_to_intervals(xs))
        # interior intervals
        intervals.extend(interior_intervals.get(y, []))

        eligible_rows[y] = merge_intervals(intervals)

    return eligible_rows


def row_covers(intervals, x0, x1):
    """Check whether merged intervals cover [x0, x1]."""
    for a, b in intervals:
        if a <= x0 and b >= x1:
            return True
        if b < x0:
            continue
        if a > x0:
            return False
    return False


def rectangle_fully_eligible(xmin, xmax, ymin, ymax, eligible_row_intervals):
    """Check if every integer point in the axis-aligned rectangle is eligible."""
    for y in range(ymin, ymax + 1):
        intervals = eligible_row_intervals.get(y)
        if not intervals:
            return False
        if not row_covers(intervals, xmin, xmax):
            return False
    return True


def find_largest_valid_product(products, coords_by_id, eligible_row_intervals):
    """
    products: list of dicts containing at least: id1,id2,product
    coords_by_id: dict[id] -> (x,y)
    eligible_row_intervals: dict[y] -> merged list[(x0,x1)]

    Returns the best product dict (with rectangle info added) or None.
    """
    # Try largest products first
    for item in sorted(products, key=lambda d: d["product"], reverse=True):
        x1, y1 = coords_by_id[item["id1"]]
        x2, y2 = coords_by_id[item["id2"]]

        xmin, xmax = sorted((x1, x2))
        ymin, ymax = sorted((y1, y2))

        if rectangle_fully_eligible(xmin, xmax, ymin, ymax, eligible_row_intervals):
            out = dict(item)
            out.update({"xmin": xmin, "xmax": xmax, "ymin": ymin, "ymax": ymax})
            return out

    return None

#%%
boundary, interior = eligible_space(coordinates)
eligible_rows = build_eligible_row_intervals(boundary, interior)
#%%
coords = []
with open('input/9.txt', 'r') as file:
# with open('input/example.txt', 'r') as file:
    for idx, line in enumerate(file, start=1):
        x, y = map(int, line.strip().split(","))
        coords.append({
            "id": idx,
            "x": x,
            "y": y
        })

coords_by_id = {c["id"]: (c["x"], c["y"]) for c in coords}
best = find_largest_valid_product(products, coords_by_id, eligible_rows)


#%%
print("largest rectangle:", best)