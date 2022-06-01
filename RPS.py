# -*- coding: utf-8 -*-
"""

Rock-Paper-Scissors Game
created by: Keshav bansal
"""

import random

def play_game():
    
    win=0
    lose=0
    tie=0
    
    play_again='y'
    
    #start the game
    
    while True:
        
        print("Welcome to Rock Paper Scissors, Let's Play...........")
        print('Please input the correct number you want to choose as an object')
        
        computer_choice=computer_player()
        player_choice=human_player()
        
        #printing the choice
    
        print('Computer choose', computer_choice,'.')
        print('You choose',player_choice,'.')
        
        res=judge(computer_choice,player_choice)
        win,lose,tie = update_gamerecords(res, win, lose, tie)
        print_outcome(res, computer_choice, player_choice)
        
        print('------------------------------------------')
        print("If you want to play again enter 'y' for yes or 'n' for no")
        print("To show the game records enter 'r'")
        play_again=input()
        
        if play_again.lower()!='y':
            if play_again.lower()=='r':
                print_gamerecord(win, lose, tie)
                print('-----------Game Over-----------')
                break
            print('-----------Game Over-----------')
            break
       
def computer_player():
    
    x=['r','p','s']
    choice=random.choice(x)
    
    if choice=='r':
        choice='ROCK'
    elif choice=='p':
        choice='PAPER'
    elif choice=='s':
        choice='SCISSORS'
    
    return choice


def human_player():
    
    choice=str(input('"Select rock(r), paper(p), scissors(s)')).lower()
    
    while choice not in ('r','p','s'):
        print('Please select option from r,p,s')
        choice=str(input('Enter a valid choice please')).lower()
        
    
    if choice=='r':
        choice='ROCK'
    elif choice=='p':
        choice='PAPER'
    elif choice=='s':
        choice='SCISSORS'
    
    return choice

def judge(computer_choice, player_choice):
    
    if computer_choice==player_choice:
        result='tie'
        return result
    
    elif computer_choice=='ROCK' and player_choice=='PAPER':   
        result='win'
        print('Paper covers rock!')
    
    elif computer_choice=='PAPER' and player_choice=='SCISSORS':
        result='win'
        print('Scissors cut paper')
        
    elif computer_choice=='SCISSORS' and player_choice=='ROCK':
        result='win'
        print('Rock crush scissors')
        
    else:
        result='lose'
        print('You Lose! computer win!')
        return result
    return result
        


def print_outcome(result, computer_choice, player_choice):

    if computer_choice==player_choice:
        print('Its a tie!')    
    elif computer_choice=='ROCK' and player_choice=='PAPER':
        print('You Win!')    
    elif computer_choice=='PAPER' and player_choice=='SCISSORS':
        print('You Win!') 
    elif computer_choice=='SCISSORS' and player_choice=='ROCK':
        print('You Win!')   
    else:
        print('You Lose!')    
    
        
def update_gamerecords(result, win, lose, tie):
    
    
    if result=='win':
        win += 1
    elif result=='lose':
        lose +=1
    elif result=='tie':
        tie +=1
    return win, lose, tie
    
    
def print_gamerecord(win, lose, tie):
    
    print('Your game records:')
    print('win:', win)
    print('lose:', lose)
    print('tie:', tie)
        
    
if __name__=='__main__':
    play_game()
    
        
    
    





