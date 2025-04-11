from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()
sense.set_rotation(180)
while True:
    sense.show_letter("z",text_colour = [158,202,160],back_colour = [3,102,6])
    sleep(0.7)
    sense.show_letter("b",text_colour = [99,100,130],back_colour = [3,102,6])
    sleep(0.5)