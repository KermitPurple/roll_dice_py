#!/usr/bin/env python3

from typing import Callable
import random, sys

def get_std_die(faces: int) -> Callable[[], int]:
    '''
    :faces: number of faces on a die
    :returns: a function that corresponds to a die with {faces} faces
    '''
    return lambda: random.randint(1, faces)

def roll_std_die(faces: int) -> int:
    '''
    :faces: number of faces on a die
    :returns: a roll of a die with {faces} faces
    '''
    return get_std_die(faces)()

def roll_d100() -> int:
    '''
    roll a d100, a special die with faces:
    10, 20, 30, 40, 50, 60, 70, 80, 90, 100
    :returns: the selected roll
    '''
    return random.randrange(10, 101, 10)

def parse_dice_roll(dice_roll_string: str) -> int:
    f'''
    :returns: the roll of the dice
    '''
    match tuple(map(int, filter(lambda x: x, dice_roll_string.strip().lower().split('d')))):
        case [repetitions, faces]:
            return sum((roll_std_die(faces) for _ in range(repetitions)))
        case [faces]:
            return roll_std_die(faces)
        case _:
            raise ValueError('Invalid string')

def main():
    '''Driver Code'''
    sys.argv.pop(0)
    for arg in sys.argv:
        try:
            result = parse_dice_roll(arg)
            print(f'{arg} = {result}')
        except ValueError as e:
            print(f'Error: Invalid dice roll string passed {arg}')

if __name__ == "__main__":
    main()
