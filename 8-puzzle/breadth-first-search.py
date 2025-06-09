import time
import random
from collections import deque
from typing import Optional

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


def print_mini_grid(s) -> None:
    """ Pretty prints current state of the puzzle """
    
    ls = [] 
    for num in s:
        ls.append(num)

    print("+-+-+-+")
    print(f"|{ls[0]}|{ls[1]}|{ls[2]}|")
    print("+-+-+-+")
    print(f"|{ls[3]}|{ls[4]}|{ls[5]}|")
    print("+-+-+-+")
    print(f"|{ls[6]}|{ls[7]}|{ls[8]}|")
    print("+-+-+-+")


def breadth_first_search(start, solution) -> Optional[list]|None:
    queue: deque = deque()
    queue.append((start, [], []))  # Append the starting state and the path taken 
    visited = set()
    visited.add(start)         # visited is a set used to keep track of past states
    
    while queue:
        state, path, dir = queue.popleft()

        if state == solution:
            return (path, dir)        # We found the answer 
 
        zero_index = state.index(0)
        for move, new_index in valid_moves(zero_index):
            new_state = list(state)
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            new_state = tuple(new_state)

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state], dir + [move]))
    return None 


def valid_moves(num: int) -> list[tuple]:
    moves: list[tuple] = []
    row, col = divmod(num, 3)

    if row > 0:
        moves.append(("up", num - 3)) 
    if row < 2:
        moves.append(("down", num + 3))
    if col > 0:
        moves.append(("left", num - 1))
    if col < 2:
        moves.append(("right", num + 1))
    return moves


def main(): 
    goal = (0,1,2,3,4,5,6,7,8)
    
    state = init_state()
    #print_grid(state)
    solution = breadth_first_search(state, goal)
    
    if solution is not None:
        steps, directions = solution 
        print(f"Steps to solution: {len(steps)}")
        count = 0
        for p in steps:
            time.sleep(1)
            print(f"Direction Moved: {directions[count]}")
            print_grid(p)
            count += 1
    else:
        print("There is no solution to this variation")


if __name__ == "__main__":
    main()
