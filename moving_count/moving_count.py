from microbit import *

moving_mode = False
prev_x = 0
moving_count = 0
moving_distance = 40
goal = 400
display.show(Image.SNAKE)

boat_r = Image("00009:"
            "00000:"
            "00000:"
            "00000:"
            "00000")
boat_lr = Image("00090:"
            "00000:"
            "00000:"
            "00000:"
            "00000")
boat_m = Image("00900:"
            "00000:"
            "00000:"
            "00000:"
            "00000")
boat_ll = Image("09000:"
            "00000:"
            "00000:"
            "00000:"
            "00000")
boat_l = Image("90000:"
            "00000:"
            "00000:"
            "00000:"
            "00000")

while True:
    if button_a.was_pressed():
        if moving_mode == True:
            moving_mode = False
#            display.show(Image.SNAKE)
            display.show(str(moving_count))
        else:
            moving_mode = True

#    if button_a.is_pressed():
#        display.show(str(moving_count))
#        moving_mode = False
    
    if moving_count > goal:
        while True:
            display.show(Image.HEART)
            moving_mode = False

    if moving_mode == True:
        reading_x = accelerometer.get_x()
        reading_y = accelerometer.get_y()

        if reading_x > 40:
##            display.show("R")
            display.show(boat_r)
        elif reading_x > 20:
##            display.show("R")
            display.show(boat_lr)
        elif reading_x < -40:
##        display.show("L")
            display.show(boat_l)
        elif reading_x < -20:
##            display.show("L")
            display.show(boat_ll)
        else:
#            display.show("-")
            display.show(boat_m)
        if prev_x * reading_x < 0:
            if prev_x - reading_x > moving_distance or reading_x - prev_x > moving_distance:
                moving_count = moving_count + 1
        prev_x = reading_x
