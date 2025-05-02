import random as r
from cube import Cube
import sys
import os

def welcome():
    print("""
==================================
        RUBIKS CUBE SOLVER
==================================
This program was created by 
Nathaniel Reeves.

Credit to tcbegley for the
Kociemba's implementation.
""")

def exit():
    print("""
==================================
              Goodbye
==================================
""")
    sys.exit(0)
    
    
def get_number_action(input_message, valid_options):
    try:
        number = int(input(input_message))
    except ValueError as e:
        return None
    return number

def get_move_action(input_message):
    c = Cube()
    valid_moves = c.get_valid_moves()
    move = input(input_message)
    if move not in valid_moves:
        return get_move_action(input_message)
    print(f'Doing Move:', end=' ')
    return move

def print_valid_moves():
    print("""

Cube is always arranged thus:
    Top:     Yellow
    Front:   Blue
    Right:   Red
    Left:    Orange
    Back:    Green
    Bottom:  White

Valid Cube Moves:
(R)  - Right         CLOCKWISE
(R') - Right         COUNTER
(F)  - Front         CLOCKWISE
(F') - Front         COUNTER
(L)  - Left          CLOCKWISE
(L') - Left          COUNTER
(B)  - Back          CLOCKWISE
(B') - Back          COUNTER
(U)  - up/top        CLOCKWISE
(U') - up/top        COUNTER
(D)  - down/bottom   CLOCKWISE
(D') - down/bottom   COUNTER
""")

def handle_cube_randomization(cube):
    valid_moves = cube.get_valid_moves()
    num_random_moves = get_number_action("Number of random moves: ", [range(1, 50)])
    print("Ramomizing Cube with {} moves.".format(num_random_moves))
    for i in range(num_random_moves):
        print("Random Move #{}:".format(i + 1), end=" ")
        cube.do_move(r.choice(valid_moves))
    print("Cube Randomized")
    return cube

def handle_cube_best_solution(cube):
    print("Calculating Solution...")
    try:
        cube.get_best_solution()
    except ValueError as e:
        print("Error:", e)
        return cube
    return cube

def handle_cube_solution(cube):
    print("Calculating Solution...")
    solution = ''
    try:
        solution = cube.get_solution()
    except ValueError as e:
        print("Error:", e)
        return solution, cube
    print("Solution:", solution)
    return solution, cube

def handle_cube_solver(solution, cube):
    moves = solution.split(' ')
    print("""==================================""")
    print("Current Cube: ")
    print(cube)
    print("""==================================""")
    for i, move in enumerate(moves):
        print()
        print("""==================================""")
        print(f"STEP {i+1}:  {move}")
        print("""----------------------------------""")
        if len(move) > 1 and move[1] == '2':
            cube.do_move(move[:1])
            cube.do_move(move[:1])
            print()
        else:
            cube.do_move(move)
            print()
        print(cube)
        print()
        input("Move Complete [enter].")
    print("""==================================""")    
    print("""          CUBE SOLVED!""")
    print("""==================================""")
    return cube

def handle_main_menu(cube):
    print("""
Menu
----------------------------------
1. Reset Cube
2. Print Cube
3. Input Cube
4. Do Move
5. Show Valid Moves
6. Randomize Cube
7. Cube Solver
8. Best Cube Solver (Longer Calc)
0. Quit Program
""")

    action = get_number_action("Action: ", [1, 2, 3, 0])
    print()
    if action == 1:
        cube = Cube()
    elif action == 2:
        print("Current Cube State: ")
        print()
        print(cube)
    elif action == 3:
        cube.build_custom_cube()
    elif action == 4:
        cube.do_move(get_move_action("Enter Move: "))
        print("Current Cube State: ")
        print()
        print(cube)
    elif action == 5:
        print_valid_moves()
    elif action == 6:
        cube = handle_cube_randomization(cube)
    elif action == 7:
        solution, cube = handle_cube_solution(cube)
        cube = handle_cube_solver(solution, cube)
    elif action == 8:
        cube = handle_cube_best_solution(cube)
    elif action == 0:
        exit()
    else:
        print("Error: Unknown action")
        handle_main_menu(cube)
    return cube

def main():
    os.system('clear')
    c = Cube()
    welcome()
    
    # Program Main Loop
    try:
        while True:
            c = handle_main_menu(c)
    except KeyboardInterrupt:
        print()
        exit()

if __name__ == '__main__':
    main()