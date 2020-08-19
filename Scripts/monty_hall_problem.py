#!/usr/bin/env python3

'''
This is meant to be an empirical demonstration of the famous Monty Hall Problem:
You are on the 'Lets make a deal' game show. You are shown three doors labeled:
<A>, <B>, <C>
Behind one of the doors is an expensive prize, the other two have a goat behind them.

You select a door.

To make things more exciting, Monty will open one of the two remaining doors.
The door he opens always contains a goat.

He then asks you: 'Would you like to change doors?'

Do you change doors? Does it matter? Many people wrongly have the intuition that it
doesn't matter, that it is an even money proposition.

This is not the case however, this script allows one to play the game or to run any number
of simulations playing the game to show the probablility if you do or do not change doors.

https://en.wikipedia.org/wiki/Monty_Hall_problem
'''

import random
import sys

INTRO = '\n'.join(('<<< Welcome to the Monty Hall Simulation Game >>>',
                   'The rules are simple:',
                   'There are three doors labeled --------  <A> <B> <C>',
                   'Behind one of the doors is a prize, behind the other two there are goats.'))
WINS_AND_LOSSES = {'Wins': 0, 'Losses': 0} #Tally for the total wins and losses
MAIN_PROMPT = "\n".join(("", "Please choose from below options:",
                         "1 - Play a game",
                         "2 - Play several games",
                         "3 - Quit",
                         "Please select an option >>"))


class GameShow:
    '''Creates a Monty Hall problem simulation'''

    def __init__(self, door):
        self.choices = ['A', 'B', 'C']
        self.win = ''
        self.final_selection = ''
        self.removal = ''
        self.remaining = ''
        self.door = door
        self.prize = random.choice(self.choices)
        self.choices.remove(self.door)
        self.select_removal()

    def select_removal(self):
        '''Selects the removal of one of the doors with a goat behind it'''
        if self.prize == self.door:
            self.prize_selected = 1
            self.removal = random.choice(self.choices)
            self.choices.remove(self.removal)
            self.remaining = self.choices[0]
        else:
            randm = random.choice(self.choices)
            if randm == self.prize:
                self.remaining = randm
                self.choices.remove(randm)
                self.removal = self.choices[0]
            else:
                self.removal = randm
                self.choices.remove(randm)
                self.remaining = self.choices[0]

    def change_doors(self, yes_or_no):
        '''Executes whether the door change selection was made or not'''
        if yes_or_no == 'Y':
            self.final_selection = self.remaining
        elif yes_or_no == 'N':
            self.final_selection = self.door

        if self.final_selection == self.prize:
            self.win = 1
        else:
            self.win = 0
        return self.win


def repeat_game():
    '''Runs x simulations of the game with a set door and stay/switch decision'''
    WINS_AND_LOSSES['Wins'], WINS_AND_LOSSES['Losses'] = 0, 0
    input1 = input('How many times do you want to play?\n>>')
    input2 = input('Please select door - <A>, <B> or <C>:\n>>')
    input3 = input('Would you like to always switch. Y/N.\n>>')
    for _ in range(int(input1)):
        play_game(door=input2, switch=input3)
    print(f'Probability of winning in {input1} simulations. Changing doors: {input3}')
    print(round(WINS_AND_LOSSES['Wins']/int(input1), 2))

def play_game(door=None, switch=None):
    '''Main logic to play the game'''
    if door is None:
        response = input('Please select a door: <A>, <B> or <C>:\n>>')
    else:
        response = door
    g = GameShow(str(response.upper()))
    print(f'You selected <{g.door}>')
    print(f'I am removing door <{g.removal}>')

    if switch is None:
        response2 = input(f'Would you like to change to door <{g.remaining}>\n...... Y/N\n>>')
    else:
        response2 = switch

    g.change_doors(response2.capitalize())

    if g.win == 1:
        WINS_AND_LOSSES['Wins'] += 1
        print(f'Congratulations you won!! The prize was behind door <{g.prize}>.')
    elif g.win == 0:
        WINS_AND_LOSSES['Losses'] += 1
        print(f'You lose, Im sorry. The prize was behind door <{g.prize}>.')
    else:
        raise 'g.win wasnt set!!!!'
    print('New game!!\n\n\n')
    print('Wins = {}\nLosses = {}'.format(WINS_AND_LOSSES['Wins'], WINS_AND_LOSSES['Losses']))

def exit_program():
    '''Exits the program'''
    print('\nShutting down the program\n')
    sys.exit()

switch_func_dict = {
    1: play_game,
    2: repeat_game,
    3: exit_program,
}

def main_switch(response):
    '''Main code logic - Handling input response'''
    try:
        switch_func_dict.get(int(response))()
    except (ValueError, TypeError):
        print('\n----> Invalid Selection: Please input 1, 2 or 3')

def main():
    '''Main code logic'''
    while True:
        response = input(MAIN_PROMPT)
        main_switch(response)


if __name__ == '__main__':
    print(INTRO)
    main()
