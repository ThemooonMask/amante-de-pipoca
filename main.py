X = 0

def on_gesture_shake():
    global X
    X = randint(0, 2)
    if X == 0:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif X == 1:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pass
basic.forever(on_forever)
