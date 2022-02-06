#!/usr/bin/env python3

# This script is designed to simulate the light and sound of a wood-fired stove --
# see github.com/mikefsway/withoutfire.git for more on the hardware setup

# Adapted from:
# Forest fire model cellular automaton. Simulates the growth
# of trees in a forest, with sporadic outbreaks of forest fires.

# https://en.wikipedia.org/wiki/Forest-fire_model

# Based on Rosetta Code Python Forest Fire example.
# https://rosettacode.org/wiki/Forest_fire#Python

import random
import time
import pygame

from unicornhatmini import UnicornHATMini

print("""
Wood-fired stove simulator based on Unicorn HAT Mini: forest-fire.py

Press Ctrl+C to exit
""")

# The fire starts out brighter, more flickery, and louder,
# then gradually settles down like a real fire over about 30 mins.
# The rate of getting dimmer/quieter/slowly is determined by value
# of mult. 1 = no change, while 0.9 = rapid change. Default setting
# is 0.95.

mult = 0.95

# Sets the audio file which is played, and volume.

file = "/home/pi/Pimoroni/withoutfire/mediumfire.mp3" # alt options of quietfire.mp3 or loudfire.mp3
volbase = 0.2 
voladd = 0.1 # determines difference between start and final volume
vol = volbase + voladd

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(vol)
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1) # -1 here loops the playback

# Sets LED brightness (higher than normal as diffused)

unicornhatmini = UnicornHATMini()
unicornhatmini.set_brightness(0.99)
unicornhatmini.set_rotation(0)

# The height and width of the led matrix (the forest in original script)
width, height = unicornhatmini.get_shape()

# Initial probability of a grid square having a tree
# In the script, a tree is used to represent a bright flicker,
# while a space is dimmer. 0.25 seems to be a good starting value
# for number of brigher leds

initial_trees = 0.25

# p = probability of tree growing, f = probability of fire
p = 0.01
f = 0.0005

# Sets the colours of trees and spaces based on RGB values (out of 255, 255, 255).

tr1base = 150 # base R value of a "tree" i.e. bright flicker
tr2base = 25 # base G value of tree -- higher makes yellower
sp1base = 100 # base R value of space i.e. the dimmer bit of flicker
sp2base = 15 # base G value of space

tr1add = 100 # determines change between initial brightness/redness of tree, and final
tr2add = 15 # as above, for yellowness
sp1add = 50 
sp2add = 15

tr1 = tr1base + tr1add
tr2 = tr2base + tr2add
sp1 = sp1base + sp1add
sp2 = sp2base + sp2add

# Uses the above to set the actual variable values

tree = [tr1, tr2, 0]
burning = [255, 20, 0]
space = [sp1, sp2, 0]

# Each square's neighbour coordinates -- leave like this
hood = ((-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1))

# Brightness, loudness etc. values apply for a set period of time before decreasing.
# The below sets that period at 40 seconds, plus/minus a random integer between -10 and 10.
# This is to give it some timing randomness.

dur = 40 + (random.randint(-10, 10))

# Function to populate the initial forest - leave
def initialise():
    grid = {(x, y): (tree if random.random() <= initial_trees else space) for x in range(width) for y in range(height)}
    return grid


# Display the forest, in its current state, on UnicornHATMini - leave
def show_grid(grid):
    unicornhatmini.clear()
    for x in range(width):
        for y in range(height):
            unicornhatmini.set_pixel(x, y, *grid[(x, y)])
    unicornhatmini.show()


# Go through grid, update grid squares based on state of
# square and neighbouring squares - leave
def update_grid(grid):
    new_grid = {}
    for x in range(width):
        for y in range(height):
            if grid[(x, y)] == burning:
                new_grid[(x, y)] = space
            elif grid[(x, y)] == space:
                new_grid[(x, y)] = tree if random.random() <= p else space
            elif grid[(x, y)] == tree:
                new_grid[(x, y)] = (burning if any(grid.get((x + dx, y + dy), space) == burning for dx, dy in hood) or random.random() <= f else tree)
    return new_grid


# Main function!

global t_end
t_end = time.time() + dur # as above, sets how long the loop runs before values change.

def mainora(speed): # Sets the speed of flicker, see below function for settings.
    grid = initialise()
    while time.time() < t_end:
        show_grid(grid)
        grid = update_grid(grid)
        time.sleep(1 / speed)

slowth = 590 # This sets how much faster flickering is at the start than at end
rapid = 10 + slowth # 10 is the end (slowest) flicker, 10+590 is the start flicker
speed = rapid

# This sets how long a brighter/louder to dimmer/quiter cycle lasts. It includes a
# random element to make it a bit less predictable.

cycle = 50 + random.randint(-10,5)

while True:

    mainora(rapid) # Runs the main function at the set speed.

    print(tr1) # Prints the R(ed) value of a tree, as a way of checking it is updating.
    unicornhatmini.clear()
    unicornhatmini.show()

    dur = 40 + (random.randint(-10, 10)) # Re-sets value for how long it loops with certain values
    t_end = time.time() + dur

# Here is where the colour values are ramped down according to the value of mult

    if cycle >= 1: 
         tr1add = tr1add * mult
         tr2add = tr2add * mult
         sp1add = sp1add * mult
         sp2add = sp2add * mult

         tr1 = int(tr1base + tr1add)
         tr2 = int(tr2base + tr2add)
         sp1 = int(sp1base + sp1add)
         sp2 = int(sp2base + sp2add)

         tree = [tr1, tr2, 0]
         space = [sp1, sp2, 0]

# And where flicker and volume are also ramped down according to mult

         slowth = slowth * mult
         rapid = 10 + slowth

         voladd = voladd * mult
         vol = volbase + voladd
         pygame.mixer.music.set_volume(vol)

         cycle = cycle - 1

# When it is time for a new cycle this resets the colour etc. values back to the original ones
# (or whatever you want).

    else:
         tr1 = 250
         tr2 = 45
         sp1 = 150
         sp2 = 30

         tree = [tr1, tr2, 0]
         space = [sp1, sp2, 0]

         slowth = 590
         rapid = 10 + slowth

         voladd = 0.1
         vol = volbase + voladd
         pygame.mixer.music.set_volume(vol)

         cycle = 50 + random.randint(-10,5)

