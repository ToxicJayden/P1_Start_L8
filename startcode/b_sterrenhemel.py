import random
import turtle

from sterren_module import *
kleuren = ("red", "orange", "yellow", "lime green", "orchid", "magenta", "dodger blue", "crimson", "chocolate", "navy", "salmon", "green yellow", "teal", "cyan", "aquamarine", "hot pink", "firebrick", "royal blue", "wheat")
for i in range(30):
    x = random.randint(-350, 350)
    y = random.randint(-350, 350)
    kleur = random.choice(kleuren)
    teken_ster(x,y,kleur)
turtle.exitonclick()