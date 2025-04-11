from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
sense.set_rotation(180)
while True:        
    sense.show_message("king kohli",scroll_speed = 0.1,text_colour = [158,202,160],back_colour = [3,102,6])