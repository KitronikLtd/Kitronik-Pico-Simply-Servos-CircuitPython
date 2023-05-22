from array import array
from board import GP2, GP3, GP4, GP5, GP6, GP7, GP8, GP9
from rp2pio import StateMachine
from adafruit_pioasm import Program

p = Program("""
    pull            ;; don't start until first value available
    
.wrap_target
    pull noblock
    mov x, osr      ;; reload OSR with last value
    set pins, 0
    out y, 16       ;; off time
    
loop_off:
    jmp y--, loop_off
    set pins, 1
    out y, 16       ;; on time
    
loop_on:
    jmp y--, loop_on
.wrap
""")

class KitronikSimplyServos:
    degreesToUS = 2000 / 180
    
    def __init__(self):
        servoPins = [GP2, GP3, GP4, GP5, GP6, GP7, GP8, GP9]
        self.servos = []
        for i in range(len(servoPins)) :
            self.servos.append(StateMachine(p.assembled, frequency=1_000_000, first_set_pin=servoPins[i], **p.pio_kwargs))
    
    def goToPosition(self, servo, degrees):
        period = int(degrees * self.degreesToUS + 500)
        self.goToPeriod(servo, period)
    
    def goToPeriod(self, servo, period):
        if servo < 0:
            servo = 0
        if servo > 7:
            servo = 7
        if period < 500:
            period = 500
        if period > 2500:
            period = 2500
        
        self.servos[servo].background_write(memoryview(array('HH', [20_000 - period, period])).cast('L'))