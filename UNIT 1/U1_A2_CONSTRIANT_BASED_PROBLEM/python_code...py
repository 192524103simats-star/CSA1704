# ============================================
# ARTIFICIAL INTELLIGENCE - ASSESSMENT 2
# Constraint-Based Problem Solving
# 1. Hospital Doctor Shift Assignment (Backtracking)
# 2. Robot Grid Navigation (Breadth-First Search)
# 3. Autonomous Rescue Robot (Uniform Cost Search)
# ============================================

from collections import deque
import heapq

# =====================================================
# PROBLEM 1: HOSPITAL DOCTOR SHIFT ASSIGNMENT
# Backtracking Search
# =====================================================

print("=" * 60)
print("PROBLEM 1: HOSPITAL DOCTOR SHIFT ASSIGNMENT")
print("=" * 60)

doctors = ["D1", "D2", "D3"]
shifts = ["Morning", "Afternoon", "Night"]

assignment = {}

def is_valid(doctor, shift):

    # D1 cannot work Night
    if doctor == "D1" and shift == "Night":
        return False

    # D3 cannot work Morning
    if doctor == "D3" and shift == "Morning":
        return False

    # Only one doctor per shift
    if shift in assignment.values():
        return False

    return True


def check_order():
    if "D2" in assignment and "D3" in assignment:
        order = {
            "Morning": 1,
            "Afternoon": 2,
            "Night": 3
        }
        return order[assignment["D2"]] < order[assignment["D3"]]
    return True


def backtracking(index):

    if index == len(doctors):
        return check_order()

    doctor = doctors[index]

    for shift in shifts:

        if is_valid(doctor, shift):

            assignment[doctor] = shift

            if check_order():
                if backtracking(index + 1):
                    return True

            del assignment[doctor]

    return False


if backtracking(0):
    print("\nValid Shift Assignment:")
    for d in doctors:
        print(d, "->", assignment[d])
else:
    print("No Valid Assignment Found")


# =====================================================
# PROBLEM 2: ROBOT GRID NAVIGATION
# Breadth First Search (BFS)
# =====================================================

print("\n" + "=" * 60)
print("PROBLEM 2: ROBOT GRID NAVIGATION")
print("=" * 60)

grid = [
    ['S', 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 'G']
]

rows = len(grid)
cols = len(grid[0])

start = (0, 0)
goal = (4, 4)

moves = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

queue = deque([(start, [start])])
visited = set()

while queue:

    (x, y), path = queue.popleft()

    if (x, y) == goal:
        print("\nShortest Path:")
        print(path)
        print("Total Cost =", len(path) - 1)
        break

    if (x, y) in visited:
        continue

    visited.add((x, y))

    for dx, dy in moves:

        nx = x + dx
        ny = y + dy

        if 0 <= nx < rows and 0 <= ny < cols:

            if grid[nx][ny] != 1 and (nx, ny) not in visited:

                queue.append(((nx, ny), path + [(nx, ny)]))


# =====================================================
# PROBLEM 3: AUTONOMOUS RESCUE ROBOT
# Uniform Cost Search (UCS)
# =====================================================

print("\n" + "=" * 60)
print("PROBLEM 3: AUTONOMOUS RESCUE ROBOT")
print("=" * 60)

grid = [
    ['S', 1, 1, 2, 1],
    [1, -1, 1, -1, 1],
    [1, -1, 1, 1, 1],
    [1, 1, -1, -1, 1],
    [1, 1, 1, 1, 'G']
]

rows = len(grid)
cols = len(grid[0])

start = (0, 0)
goal = (4, 4)

priority_queue = []

heapq.heappush(priority_queue, (0, start, [start]))

visited = {}

while priority_queue:

    cost, (x, y), path = heapq.heappop(priority_queue)

    if (x, y) == goal:
        print("\nLeast Cost Path:")
        print(path)
        print("Total Cost =", cost)
        break

    if (x, y) in visited and visited[(x, y)] <= cost:
        continue

    visited[(x, y)] = cost

    for dx, dy in moves:

        nx = x + dx
        ny = y + dy

        if 0 <= nx < rows and 0 <= ny < cols:

            if grid[nx][ny] == -1:
                continue

            move_cost = 1

            # Risky Zone
            if grid[nx][ny] == 2:
                move_cost += 2

            heapq.heappush(
                priority_queue,
                (
                    cost + move_cost,
                    (nx, ny),
                    path + [(nx, ny)]
                )
            )

print("\n")
print("=" * 60)
print("ALL THREE AI PROBLEMS EXECUTED SUCCESSFULLY")
print("=" * 60)
