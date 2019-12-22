#episode-03 (Destroying furnace bots)

import random

def find_parent_bot(number_of_bots):
    a = random.choice(number_of_bots)
    serial_number = s_no[a]
    var = furnace_value[a]
        
    for i in range(number_of_bots):
        if var == 0:
            return serial_number
        else:
            serial_number = var
            var = furnace_value[serial_number]
        


