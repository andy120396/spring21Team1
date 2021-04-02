import random
import pygame
from pygame.locals import *
pygame.init()
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Arcade RPS")
#define game variables
tile_size = 213.3

#load images
background_img = pygame.image.load('templates/IMGpack1/Arcadebackground.png')

def draw_grid():
    for line in range(0,11):
        pygame.draw.line(screen,(255,255,255),(0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen,(255,255,255),(line * tile_size,0),(line * tile_size, screen_height))

run = True
while run:
    screen.blit(background_img,(0,0))
    draw_grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
'pygame.quit()'
'''
while True:
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    user_name = input("What is player's Name?")
    print("Hello!", user_name, "Welcome to Arcade R! P! S! Lets start a exciting game!")
    user_action =input("-Enter Your choice (rock, paper, scissors): ")

    if user_action == computer_action:
        print(f"WOW,Both players selected {user_action}. what a coincidence.It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock have destroy scissors! You win the round! Congratulation!🎉🎉🎉")
        else:
            print("Paper have trap rock! You lose the round.😭😭😭")


    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")


    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
    '''