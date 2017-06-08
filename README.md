# monoprice6z
Monoprice Six Zone WHA amp RS232 Python module based on Russound Rnet (https://github.com/laf/russound)


Implements a Python API for selected commands to the Monoprice system predominantly developed to provide Monoprice support within home-assistant.io. The class is designed to maintain a connection to the Monoprice controller, and reads the state directly from the controller via serial connection. In principle supported models include the Monoprice 10761. Function to control Monoprice implemented are:

####For a zone:

set_power
set_volume
set_source
toggle_mute
get_power
get_volume
get_source

####Controller level

all_on_off

test_harness.py shows some examples of usage.
