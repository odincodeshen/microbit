from microbit import *

import radio

import music



select_mode = 0



moving_mode = False

prev_x = 0

moving_count = 0

moving_distance = 40

goal = 400


image_num = 0



tempo_base = 120
tempo_cnt = 0



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

all_images = [Image.HEART, Image.SMILE, Image.DIAMOND, Image.YES, Image.GHOST, Image.RABBIT, Image.XMAS]

notes = [



    'c4:1', 'e', 'g', 'c5', 'e5', 'g4', 'c5', 'e5', 'c4', 'e', 'g', 'c5', 'e5', 'g4', 'c5', 'e5',



    'c4', 'd', 'g', 'd5', 'f5', 'g4', 'd5', 'f5', 'c4', 'd', 'g', 'd5', 'f5', 'g4', 'd5', 'f5',



    'b3', 'd4', 'g', 'd5', 'f5', 'g4', 'd5', 'f5', 'b3', 'd4', 'g', 'd5', 'f5', 'g4', 'd5', 'f5',



    'c4', 'e', 'g', 'c5', 'e5', 'g4', 'c5', 'e5', 'c4', 'e', 'g', 'c5', 'e5', 'g4', 'c5', 'e5',



    'c4', 'e', 'a', 'e5', 'a5', 'a4', 'e5', 'a5', 'c4', 'e', 'a', 'e5', 'a5', 'a4', 'e5', 'a5',



    'c4', 'd', 'f#', 'a', 'd5', 'f#4', 'a', 'd5', 'c4', 'd', 'f#', 'a', 'd5', 'f#4', 'a', 'd5',



    'b3', 'd4', 'g', 'd5', 'g5', 'g4', 'd5', 'g5', 'b3', 'd4', 'g', 'd5', 'g5', 'g4', 'd5', 'g5',



    'b3', 'c4', 'e', 'g', 'c5', 'e4', 'g', 'c5', 'b3', 'c4', 'e', 'g', 'c5', 'e4', 'g', 'c5',



    'b3', 'c4', 'e', 'g', 'c5', 'e4', 'g', 'c5', 'b3', 'c4', 'e', 'g', 'c5', 'e4', 'g', 'c5',



    'a3', 'c4', 'e', 'g', 'c5', 'e4', 'g', 'c5', 'a3', 'c4', 'e', 'g', 'c5', 'e4', 'g', 'c5',



    'd3', 'a', 'd4', 'f#', 'c5', 'd4', 'f#', 'c5', 'd3', 'a', 'd4', 'f#', 'c5', 'd4', 'f#', 'c5',



    'g3', 'b', 'd4', 'g', 'b', 'd', 'g', 'b', 'g3', 'b3', 'd4', 'g', 'b', 'd', 'g', 'b'



]



radio.on()

#display.show(Image.HEART)
display.show(Image.XMAS)




while True:

    if button_a.is_pressed():

        select_mode = select_mode + 1

        if select_mode == 1:

            ## Run mode

            display.show("P")

        elif select_mode == 2:

            ## Jump mode

            display.show("J")

        elif select_mode == 3:

            ## Sing mode

            display.show("S")

        elif select_mode == 4:

            ## Sing mode
            display.show(Image.HEART)

        else:

            select_mode = 0

    

    if button_b.is_pressed():

        if select_mode == 1:

            ## Run mode

#            press_fun(select_mode)

            display.scroll("Press")

            sleep(500)

            num = 0

            while True:

                message = radio.receive()

                if message == "hi":

#                    display.show(Image.SMILE)
#                    display.show(random.choice(all_images))
                    display.show(all_images[image_num % len(all_images)])

                    image_num = image_num + 1



                elif message == "ih":

                    display.show(str(num))

                num = num + 1

                if num == 10:

                    num = 0

                if button_a.was_pressed():

                    display.clear()

                    radio.send("hi")

                elif button_b.was_pressed():

                    display.clear()

                    radio.send("ih")



        elif select_mode == 2:

            ## Jump mode

#            jump_fun(select_mode)

            display.scroll("Jump")

            sleep(500)

            while True:

                if button_a.was_pressed():

                    if moving_mode == True:

                        moving_mode = False

                        display.show(str(moving_count))

                    else:

                        moving_mode = True



                if moving_count > goal:

                    while True:

                        display.show(Image.HEART)

                        moving_mode = False



                if moving_mode == True:

                    reading_x = accelerometer.get_x()

                    reading_y = accelerometer.get_y()



                    if reading_x > 40:

                        display.show(boat_r)

                    elif reading_x > 20:

                        display.show(boat_lr)

                    elif reading_x < -40:

                        display.show(boat_l)

                    elif reading_x < -20:

                        display.show(boat_ll)

                    else:

                        display.show(boat_m)

                    if prev_x * reading_x < 0:

                        if prev_x - reading_x > moving_distance or reading_x - prev_x > moving_distance:

                            moving_count = moving_count + 1

                    prev_x = reading_x



        elif select_mode == 3:

            ## Sing mode
            tempo_cnt = tempo_cnt + 1

            sing_bpm = tempo_base + tempo_cnt * 40

            music.set_tempo(bpm=sing_bpm)
            music.play(music.BIRTHDAY)
            display.show(Image.ALL_ARROWS)

        elif select_mode == 4:
            ## Naming mode
#            display.scroll("MEGAN X MI X MING")
#            sleep(1000)
#            display.scroll("MEGAN")
            display.scroll("YAYA")

    sleep(200)

