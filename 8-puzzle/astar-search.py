import time
import random
from heapq import heappush, heappop 

def init_state() -> tuple: 
    """ Initialize all squares in the puzzle with a num from 0 - 8 """
    state = []
    count = 0
    numbers = [0,1,2,3,4,5,6,7,8]
    while len(numbers) > 0:
        chosen: int = random.choice(numbers)
        state.insert(count, chosen)
        numbers.remove(chosen)
        count += 1 

    return tuple(state)


def print_grid(s) -> None:
    """ Pretty prints current state of the puzzle """
    
    ls = [] 
    for num in s:
        ls.append(num)

    # print("+-+-+-+")
    # print(f"|{ls[0]}|{ls[1]}|{ls[2]}|")
    # print("+-+-+-+")
    # print(f"|{ls[3]}|{ls[4]}|{ls[5]}|")
    # print("+-+-+-+")
    # print(f"|{ls[6]}|{ls[7]}|{ls[8]}|")
    # print("+-+-+-+")
    print("+-----+-----+-----+")
    print("|     |     |     |")
    print(f"|  {ls[0]}  |  {ls[1]}  |  {ls[2]}  |")
    print("|     |     |     |")
    print("+-----+-----+-----+")
    print("|     |     |     |")
    print(f"|  {ls[3]}  |  {ls[4]}  |  {ls[5]}  |")
    print("|     |     |     |")
    print("+-----+-----+-----+")
    print("|     |     |     |")
    print(f"|  {ls[6]}  |  {ls[7]}  |  {ls[8]}  |")
    print("|     |     |     |")
    print("+-----+-----+-----+")
    

def astar(start, goal):
    heap = []
    heappush(heap, (0 + heuristic(start), 0, start, []))
    visited = set() 

    while heap:
        f, g, state, path = heappop(heap)


        if state == goal:

            return path 

        if state in visited:
            continue 

        visited.add(state)
        
        zero_index = state.index(0)
        for _, new_index in valid_moves(zero_index):
            new_state = list(state)
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            new_state = tuple(new_state)

            if new_state not in visited:
                cost = g + 1 
                estimate = cost + heuristic(new_state)
                heappush(heap, (estimate, cost, new_state, path + [new_state]))

    return None 


def heuristic(state):
    distance = 0
    for i, tile in enumerate(state):
        if tile == 0:
            continue 

        goal_index = tile - 1
        current_row, current_col = divmod(i, 3)
        goal_row, goal_col = divmod(goal_index, 3)
        distance += abs(current_row - goal_row) + abs(current_col - goal_col)

    return distance 


def valid_moves(num: int) -> list[tuple]:
    moves: list[tuple] = []
    row, col = divmod(num, 3)

    if row > 0:
        moves.append(("up", num - 3))
    if row < 2:
        moves.append(("down", num + 3))
    if col > 0:
        moves.append(("eft", num - 1))
    if col < 2:
        moves.append(("right", num + 1))

    return moves


def main(): 
    goal = (0,1,2,3,4,5,6,7,8)
    
    state = init_state()
    #print_grid(state)
    solution = astar(state, goal)
    
    if solution is not None:
        steps = solution 
        print(f"Steps to solution: {len(steps)}")
        count = 0
        for p in steps:
            time.sleep(1)
            #print(f"Direction Moved: {directions[count]}")
            print_grid(p)
            count += 1
    else:
        print("There is no solution to this variation")


if __name__ == "__main__":
    main()
