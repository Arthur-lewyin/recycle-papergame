import pgzrun
import random

WIDTH = 800
HEIGHT = 600

START_SPEED = 10
ITEMS = ["bag","battery",'bottle','chips']

FINAL_LEVEL = 6
current_level = 1

#lose the game
game_over = False
#win the game
game_complete=False

items=[]
animations = []

def draw():
    global items, current_level, game_over, game_complete

    screen.clear()
    screen.blit("bg", (0,0))

    #abstraction
    if game_over:
        display_message("GAME OVER", "try again.")  
    elif game_complete:
        display_message("WELLDONE", "all levels finished")
    else :
        for item in items:
            item.draw()

def display_message(heading,subheading) :
    screen.draw.text(heading,fontsize = 60, center = (400,300), color="black")
    screen.draw.text(subheading,fontsize = 30, center = (400,340), color="black")

def update():
    global items
    if len(items)==0:
        items = make_items(current_level)

def make_items():
    pass 
#Make items
#1.get the options from ITEMS list - random
#2.Create actors and add it to items list
#3.Layout items - display them with equal spacing
#4.Animations - move the objects down

pgzrun.go()