# Kitronik-Pico-Simply-Servos-CircuitPython
A CircuitPython class and example code to use the Kitronik Simply Servos board for Raspberry Pi Pico. (www.kitronik.co.uk/5339)

To use, save SimpyServos.py file onto the Pico so it can be imported.

## Import SimplyServos.py and construct an instance:
``` python
from SimplyServos import KitronikSimplyServos
board = KitronikSimplyServos()
```

This will initialise the PIO and set them to drive the servo pins.

## Drive a Servo by degrees:
``` python
board.goToPosition(servo, degrees)
```
where:
* servo => 0 to 7
* degrees => 0 - 180

## Drive a Servo by pulse width:
``` python
board.goToPeriod(servo, period)
```
where:
* servo => 0 to 7
* period => 500 - 2500 
	* period is the pulse width in microseconds
