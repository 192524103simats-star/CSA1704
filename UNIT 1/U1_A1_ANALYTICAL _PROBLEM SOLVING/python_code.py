# ==========================================
# AI Assessment 1
# Analytical Problem Solving
# ==========================================

from queue import PriorityQueue

# =====================================================
# Question 1 - Water Jug Problem
# =====================================================

def water_jug():
    print("\n===================================")
    print("QUESTION 1 - WATER JUG PROBLEM")
    print("===================================")

    jug4 = 0
    jug3 = 0

    print("Initial State")
    print("4-Gallon Jug =", jug4)
    print("3-Gallon Jug =", jug3)

    jug4 = 4
    print("\nStep 1: Fill 4-Gallon Jug")
    print(jug4, jug3)

    transfer = min(jug4, 3 - jug3)
    jug4 -= transfer
    jug3 += transfer
    print("\nStep 2: Pour into 3-Gallon Jug")
    print(jug4, jug3)

    jug3 = 0
    print("\nStep 3: Empty 3-Gallon Jug")
    print(jug4, jug3)

    jug3 = jug4
    jug4 = 0
    print("\nStep 4: Transfer remaining water")
    print(jug4, jug3)

    jug4 = 4
    print("\nStep 5: Fill 4-Gallon Jug Again")
    print(jug4, jug3)

    transfer = min(jug4, 3 - jug3)
    jug4 -= transfer
    jug3 += transfer

    print("\nGoal Achieved")
    print("2 Gallons remain in the 4-Gallon Jug")


# =====================================================
# Question 2 - Mars Rover Intelligent Agent
# =====================================================

def mars_rover():
    print("\n===================================")
    print("QUESTION 2 - MARS ROVER")
    print("===================================")

    print("\nPEAS Description")
    print("Performance : Safe Navigation")
    print("Environment : Mars Surface")
    print("Actuators   : Wheels, Robotic Arm, Drill")
    print("Sensors     : Camera, Temperature Sensor, Battery Sensor")

    print("\nAgent Model : Learning Agent")

    print("\nActions")
    actions = [
        "Move Forward",
        "Turn Left",
        "Turn Right",
        "Avoid Obstacle",
        "Collect Sample",
        "Recharge Battery",
        "Send Data"
    ]

    for action in actions:
        print("-", action)


# =====================================================
# Question 3 - 8 Queens Problem
# =====================================================

N = 8

def is_safe(board, row, col):

    for i in range(col):
        if board[row][i] == 1:
            return False

    i = row
    j = col

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row
    j = col

    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve(board, col):

    if col == N:
        return True

    for row in range(N):

        if is_safe(board, row, col):

            board[row][col] = 1

            if solve(board, col + 1):
                return True

            board[row][col] = 0

    return False


def queens():

    print("\n===================================")
    print("QUESTION 3 - 8 QUEENS")
    print("===================================")

    board = [[0] * N for i in range(N)]

    if solve(board, 0):

        for row in board:
            for cell in row:

                if cell == 1:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")

            print()

    else:
        print("No Solution")


# =====================================================
# Question 4 - OLA Cab Booking
# =====================================================

def ola():

    print("\n===================================")
    print("QUESTION 4 - OLA CAB BOOKING")
    print("===================================")

    customer = input("Customer Name : ")
    source = input("Source : ")
    destination = input("Destination : ")

    print("\nAvailable Cabs")
    print("1. Mini  - Rs.150")
    print("2. Sedan - Rs.250")
    print("3. SUV   - Rs.400")

    choice = int(input("\nChoose Cab : "))

    if choice == 1:
        cab = "Mini"
        fare = 150

    elif choice == 2:
        cab = "Sedan"
        fare = 250

    elif choice == 3:
        cab = "SUV"
        fare = 400

    else:
        cab = "Invalid"
        fare = 0

    print("\nBooking Confirmed")
    print("Customer :", customer)
    print("Source :", source)
    print("Destination :", destination)
    print("Cab :", cab)
    print("Fare : Rs.", fare)

    print("\nAgent Model : Goal-Based Agent")


# =====================================================
# Question 5 - Uniform Cost Search
# =====================================================

graph = {
    'S': [('A',1), ('B',4)],
    'A': [('C',1)],
    'B': [('D',5)],
    'C': [('G',2)],
    'D': [('G',1)],
    'G': []
}


def ucs(start, goal):

    pq = PriorityQueue()

    pq.put((0, start, [start]))

    visited = set()

    while not pq.empty():

        cost, node, path = pq.get()

        if node in visited:
            continue

        visited.add(node)

        if node == goal:

            print("\nOptimal Path :", " -> ".join(path))
            print("Total Cost :", cost)
            return

        for next_node, weight in graph[node]:

            if next_node not in visited:
                pq.put((cost + weight, next_node, path + [next_node]))


def uniform_cost():

    print("\n===================================")
    print("QUESTION 5 - UNIFORM COST SEARCH")
    print("===================================")

    ucs('S', 'G')


# =====================================================
# Main Program
# =====================================================

water_jug()
mars_rover()
queens()
ola()
uniform_cost()

print("\n===================================")
print("ASSESSMENT 1 COMPLETED SUCCESSFULLY")
print("===================================")
