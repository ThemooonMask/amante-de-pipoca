let X = 0
input.onGesture(Gesture.Shake, function () {
    X = randint(0, 2)
    if (X == 0) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (X == 1) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
})
basic.forever(function () {
	
})
