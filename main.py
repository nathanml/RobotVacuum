import random
import time

import bt_library as btl
from bt.globals import (BATTERY_LEVEL, GENERAL_CLEANING, SPOT_CLEANING, DUSTY_SPOT_SENSOR, HOME_PATH, CHARGING,
                        DUSTY_SPOT_PROBABILITY, CLEAN_FLOOR, BATTERY_LEVEL_START)
from bt.robot_behavior import robot_behavior

# Main body of the assignment
current_blackboard = btl.Blackboard()

current_blackboard.set_in_environment(BATTERY_LEVEL, BATTERY_LEVEL_START)
current_blackboard.set_in_environment(SPOT_CLEANING, False)
current_blackboard.set_in_environment(GENERAL_CLEANING, False)
current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, False)
current_blackboard.set_in_environment(HOME_PATH, "")
current_blackboard.set_in_environment(CHARGING, False)
current_blackboard.set_in_environment(CLEAN_FLOOR, False)

cycle = 0
while current_blackboard.get_in_environment(CLEAN_FLOOR, False) is not True:
    cycle += 1
    print('----------------------------------------------------------------------')
    print('CYCLE : ', cycle)
    time.sleep(1)
    # Each cycle in this while-loop is equivalent to 1 second time

    # Step 1: Change the environment
    # Battery charges 5% each cycle or loses 1% each cycle

    current_battery = current_blackboard.get_in_environment(BATTERY_LEVEL, 0)

    # If vacuum currently charging
    if current_blackboard.get_in_environment(CHARGING, False) is True:
        # Increment 5% each cycle
        new_battery = current_battery + 5
        # Adjust battery level in blackboard
        if new_battery < 100:
            print('CHARGE : ', new_battery)
            current_blackboard.set_in_environment(BATTERY_LEVEL, new_battery)
        else:
            print('CHARGE : 100')
            current_blackboard.set_in_environment(BATTERY_LEVEL, 100)

    # If battery is not currently charging, decrement charge by 1 in blackboard
    else:
        new_battery = current_blackboard.get_in_environment(BATTERY_LEVEL, 0) - 1
        current_blackboard.set_in_environment(BATTERY_LEVEL, new_battery)
        print('CHARGE : ', new_battery)

    # Simulate Dusty Spot Sensor with random number generator
    # 10% chance of dusty spot
    if random.randint(0, 100) < DUSTY_SPOT_PROBABILITY:
        current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, True)
    else:
        current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, False)

    # Simulate User Input
    # If user hasn't made selection, prompt
    if current_blackboard.get_in_environment(SPOT_CLEANING,
                                             False) is False and current_blackboard.get_in_environment(
            GENERAL_CLEANING, False) is False:
        print("A. Spot Cleaning")
        print("B. General Cleaning")
        user_input = input("What kind of cleaning would you like to do? Enter A or B: ")
        if user_input == "A":
            current_blackboard.set_in_environment(SPOT_CLEANING, True)
            current_blackboard.set_in_environment(GENERAL_CLEANING, False)
        if user_input == "B":
            current_blackboard.set_in_environment(GENERAL_CLEANING, True)
            current_blackboard.set_in_environment(SPOT_CLEANING, False)
        else:
            print("Invalid selection. Please select A or B")

    # Step 2: Evaluating the behavior tree
    result = robot_behavior.evaluate(current_blackboard)
