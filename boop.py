from machine import Pin, Timer
import time
import math
led_pins = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19] # These are the pins in use!
_sweep = [i for i in led_pins]
_skip_one = [
    [led_pins[i%len(led_pins)],
     led_pins[(i+2)%len(led_pins)],
     led_pins[(i+ 4)%len(led_pins)]
     ] for i in range(0, len(led_pins),1)
    ]
#Some Display Functions
_bounce = [
        led_pins[0]
    ]
_bounce_two = [[led_pins[0 + j], led_pins[0 - j]] for j in range(1, math.ceil((len(led_pins)/2)+1),1)]
for entry in _bounce_two:
    _bounce.append(entry)
_reverse_bounce = _bounce.copy()
_reverse_bounce.reverse()
_full_bounce = _bounce.copy()
for entry in _reverse_bounce[1:-1]:# Remove the Start and End States to get a full cycle with no duplicates
    _full_bounce.append(entry)
led_objects = {}
for led in led_pins:
    led_objects[led] = (Pin(led, Pin.OUT))


# Reset the Current Execution State to all off
def reset_state():
    for led in led_objects.keys():
        led_objects[led].off()
    

def process_function(recipe, delay):
    for stage in recipe:
        reset_state()
        if type(stage) == list:
            # We have multiple Lights on at this stage
            for light in stage:
                led_objects[light].on()
        else:
            light = stage
            led_objects[light].on()
        time.sleep(delay)
    reset_state()
    
time_delay = [0.1, 0.2, 0.3]

# #TODO: Process a Button to switch state on command
enabled_functions = [_full_bounce]
while True:
    for f in enabled_functions:
        for t in time_delay:
            process_function(f,t)

reset_state()


            
