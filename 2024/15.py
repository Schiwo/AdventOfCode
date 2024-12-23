# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:27:51 2024

@author: schiltem93
"""


#%% PART 1

with open('input/input15.txt', 'r') as file:
# with open('input/example.txt', 'r') as file:
    lines = file.read().strip().split("\n")
    
index = lines.index('')

map_lines = lines[:index]
movements = ''.join(lines[index + 1:])

# %%
   
class GameObject:
    def __init__(self, symbol):
        self.symbol = symbol

    def __repr__(self):
        return self.symbol


class GameMap:
    def __init__(self, grid):
        self.grid = [[GameObject(cell) for cell in row] for row in grid]
        self.height = len(grid)
        self.width = len(grid[0])
        self.robot_position = self.find_robot()

    def find_robot(self):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell.symbol == "@":
                    return (y, x)
        raise ValueError("Robot not found on the map!")

    def display(self):
        for row in self.grid:
            print("".join(cell.symbol for cell in row))
        print()

    def is_wall(self, y, x):
        return self.grid[y][x].symbol == "#"

    def is_box(self, y, x):
        return self.grid[y][x].symbol == "O"

    def is_empty(self, y, x):
        return self.grid[y][x].symbol == "."

    def move_robot(self, direction):
        dy, dx = 0, 0
        if direction == "<":
            dy, dx = 0, -1
        elif direction == ">":
            dy, dx = 0, 1
        elif direction == "^":
            dy, dx = -1, 0
        elif direction == "v":
            dy, dx = 1, 0

        y, x = self.robot_position
        new_y, new_x = y + dy, x + dx

        if self.is_wall(new_y, new_x):
            return  # Skip movement if moving into a wall

        if self.is_box(new_y, new_x):
            if not self.move_boxes(new_y, new_x, dy, dx):
                return  # Skip movement if boxes cannot move

        # Move the robot
        self.grid[y][x] = GameObject(".")
        self.grid[new_y][new_x] = GameObject("@")
        self.robot_position = (new_y, new_x)

    def move_boxes(self, y, x, dy, dx):
        positions_to_move = []

        while True:
            if not (0 <= y < self.height and 0 <= x < self.width):
                break
            if self.is_box(y, x):
                positions_to_move.append((y, x))
                y, x = y + dy, x + dx
            else:
                break

        # Check if the last position is valid
        if not (0 <= y < self.height and 0 <= x < self.width) or not self.is_empty(y, x):
            return False  # Cannot move if blocked

        # Move all boxes
        for box_y, box_x in reversed(positions_to_move):
            self.grid[box_y][box_x] = GameObject(".")
            self.grid[box_y + dy][box_x + dx] = GameObject("O")

        return True
    
    def countGPS(self):
        gps_value = 0
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell.symbol == "O":
                    gps_value += 100 * y + x
        return gps_value
    
# %%
    
game_map = GameMap(map_lines)
print("Initial Map:")
game_map.display()

for i, move in enumerate(movements):
    print("step", i, "; move:", move)
    game_map.move_robot(move)
    game_map.display()

print("GPS Value:", game_map.countGPS())

# %% PART 2

with open('input/input15.txt', 'r') as file:
# with open('input/example.txt', 'r') as file:
    lines = file.read().strip().split("\n")
    
index = lines.index('')

map_lines = []
for line in lines[:index]:
    map_lines.append("")
    for element in line:
        if element == "O":
            map_lines[-1] += "[]"
        elif element =="@":
            map_lines[-1] += "@."
        else:
            map_lines[-1] += 2*element
movements = ''.join(lines[index + 1:])

# %%
class GameObject:
    def __init__(self, symbol):
        self.symbol = symbol

    def __repr__(self):
        return self.symbol



class GameMap:
    def __init__(self, grid):
        self.grid = [[GameObject(cell) for cell in row] for row in grid]
        self.height = len(grid)
        self.width = len(grid[0])
        self.robot_position = self.find_robot()

    def find_robot(self):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell.symbol == "@":
                    return (y, x)
        raise ValueError("Robot not found on the map!")

    def display(self):
        for row in self.grid:
            print("".join(cell.symbol for cell in row))
        print()

    def is_wall(self, y, x):
        return self.grid[y][x].symbol == "#"

    def is_box_left(self, y, x):
        return self.grid[y][x].symbol == "["

    def is_box_right(self, y, x):
        return self.grid[y][x].symbol == "]"

    def is_box(self, y, x):
        return self.is_box_left(y, x) or self.grid[y][x].symbol == "]"

    def is_empty(self, y, x):
        return self.grid[y][x].symbol == "."

    def move_robot(self, direction):
        dy, dx = 0, 0
        if direction == "<":
            dy, dx = 0, -1
        elif direction == ">":
            dy, dx = 0, 1
        elif direction == "^":
            dy, dx = -1, 0
        elif direction == "v":
            dy, dx = 1, 0

        y, x = self.robot_position
        new_y, new_x = y + dy, x + dx

        if self.is_wall(new_y, new_x):
            return  # Skip movement if moving into a wall

        if self.is_box(new_y, new_x):
            if self.is_box_right(new_y, new_x):
                new_x1 = new_x - 1
                new_x2 = new_x
            elif self.is_box_left(new_y, new_x):
                new_x1 = new_x
                new_x2 = new_x + 1
            if not self.move_boxes(new_y, new_x1, new_x2, dy, dx):
                return  # Skip movement if boxes cannot move

        # Move the robot
        self.grid[y][x] = GameObject(".")
        self.grid[new_y][new_x] = GameObject("@")
        self.robot_position = (new_y, new_x)

        
    def move_boxes(self, y, x1, x2, dy, dx):
        positions_to_move = []
        
        positions_to_evaluate = [(y, x1, x2)]
        while True:
            y,x1,x2 = positions_to_evaluate[0]
            if not (0 <= y < self.height and 0 <= x1 and x2 < self.width):
                break
            if (dy != 0 and (self.is_wall(y, x1) or self.is_wall(y, x2))) or \
                (dx > 0 and self.is_wall(y, x1)) or \
                (dx < 0 and self.is_wall(y, x2)):
                    print("there is a wall!", y, x1, x2)
                    return False  # Invalid box structure
            if (dy != 0 and (self.is_box(y, x1) or self.is_box(y, x2))) or \
                (dx > 0 and self.is_box(y, x1)) or \
                (dx < 0 and self.is_box(y, x2)):
                # if self.is_box_left(y, x):
                if (self.is_box_left(y, x1)):
                    print("normal")
                    positions_to_move.append((y, x1, x2))
                    positions_to_evaluate.append((y + dy, x1 + 2*dx, x2 + 2*dx))
                if (self.is_box_right(y, x1)):
                    print("left")
                    positions_to_move.append((y, x1-1, x1))
                    positions_to_evaluate.append((y + dy, x1 - 1 + 2*dx, x1 + 2*dx))
                if (self.is_box_left(y, x2)):
                    print("right")
                    positions_to_move.append((y, x2, x2+1))
                    positions_to_evaluate.append((y + dy, x2 + 2*dx, x2 + 1 + 2*dx))  
                positions_to_evaluate.pop(0)    
            elif(len(positions_to_evaluate)>1):
                positions_to_evaluate.pop(0) 
            else:
                break
            
        print(positions_to_move)
        # Check if the last position is valid for all box parts
        if not (0 <= y < self.height and (0 <= x1 and x2 <= self.width)):# or not (self.is_empty(y, x1) and self.is_empty(y, x2)):
            return False
        # Move all boxes
        for box_y, box_x1, box_x2 in reversed(positions_to_move):
            print(box_x1, box_x2)
            self.grid[box_y][box_x1] = GameObject(".")
            self.grid[box_y][box_x2] = GameObject(".")
            self.grid[box_y + dy][box_x1 + dx] = GameObject("[")
            self.grid[box_y + dy][box_x2 + dx] = GameObject("]")

        return True
    
    def countGPS(self):
        gps_value = 0
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell.symbol == "[":
                    gps_value += 100 * y + x
        return gps_value

  
game_map = GameMap(map_lines)

print("Initial Map:")
game_map.display()

for i, move in enumerate(movements):
    # if i > 5:
    #     break
    # print("step", i, "; move:", move)
    game_map.move_robot(move)
    game_map.display()
    
print("GPS Value:", game_map.countGPS())
