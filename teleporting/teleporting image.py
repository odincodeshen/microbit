from microbit import display, button_a, button_b, Image

import radio

radio.on()

#display.show(Image.SILLY)

display.show('M')



num = 0

while True:

    message = radio.receive()

#    if message:

#        display.show(Image.HEART)

#        display.show(str(num))

#        num = num + 1

#        if num == 10:

#            num = 0

    if message == "hi":

        display.show(Image.HEART)

#        display.show(str(num))

#        num = num + 1

#        if num == 10:

#            num = 0

    elif message == "ih":

        display.show(str(num))

#        display.show(str(message))

        num = num + 1

        if num == 10:

            num = 0

    if button_a.was_pressed():

        display.clear()

        radio.send("hi")

    elif button_b.was_pressed():

        display.clear()

        radio.send("ih")