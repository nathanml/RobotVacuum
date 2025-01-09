## CS131 Assignment 01 - Behavior Trees

#### Instructions to run and test

From the root directory, run the following command in the 
command line:
```
python main.py
```

#### User Interface
Once running, the user will be prompted with the following
menu to select the type of cleaning they would like the 
vacuum to perform:

```
A. Spot Cleaning
B. General Cleaning
What kind of cleaning would you like to do? Enter A or B: 
```
If the user inputs 'A', the vacuum will perform a 20-second
clean of the current spot and then prompt the user with the
menu once done. If the user inputs 'B', the vacuum will 
clean until the entire room is clean or until
there are no more cycles. Spot cleaning and general cleaning
will both be interrupted if the vacuum requires
charging (drops below 30%). Any other input sends the 
vacuum to the Do Nothing state.

Each cycle, the user will see the current battery level,
the cycle number, and the current evaluation of the tree:

```----------------------------------------------------------------------
CYCLE :  1
CHARGE :  30
A. Spot Cleaning
B. General Cleaning
What kind of cleaning would you like to do? Enter A or B: B
BatteryLessThan30(0): Checking battery < 30
BatteryLessThan30(0): FAILED
Sequence(4): FAILED
SpotCleaning(5): Checking Spot Cleaning 
SpotCleaning(5): FAILED
Sequence(9): FAILED
GeneralCleaning(18): Checking General Cleaning 
GeneralCleaning(18): SUCCEEDED
DustySpot(10): Checking if dusty spot
DustySpot(10): SUCCEEDED
Timer(12): time-to-expiration = 34
CleanSpot(11): Cleaning Spot.
CleanSpot(11): SUCCEEDED
Timer(12): RUNNING
Sequence(14): RUNNING
Priority(17): RUNNING
Sequence(20): RUNNING
Sequence(21): RUNNING
Selection(22): RUNNING
Priority(24): RUNNING
----------------------------------------------------------------------
```

### Design/Assumptions

#### Charging
CURRENT_BATTERY is set by the environment (in main.py) 
based on whether the battery is charging or not. If the
battery isn't charging, the vacuum loses 1% battery. If 
it is charging, it gains 5% charge. Battery level is 
initialized to 50%.

#### Termination
This program will terminate when the vacuum determines
the entire floor is clean. It does this in the state
Done General, which is entered based on a
random probability. 

#### Global Variables

Global variables are configured in globals.py. These variables can be 
adjusted to help with testing.

DUSTY_SPOT_PROBABILITY: Probability (out of 100) that
the sensor will detect a dusty spot. 

CLEAN_FLOOR_PROBABILITY: Probability that the vacuum
will complete its general cleaning in a given cycle.


#### Priority Node
The priority node is created by passing in an array
of priorities along with the children when the node
is instantiated. The priorities array is used to 
sort the children into an ordered list that is used
for node evaluation. These are set in robot_behavior.py.

#### External Libraries
This implementation uses two external libraries:

<i>Random</i> for simulating random environment factors like the dusty
spot sensor and the clean floor status. 

<i>Time</i> to have 1 cycle take 1 second. Line 25 of main.py can be 
commented out for faster execution.

#### Performance Measure
Vacuum executes every state expected and never runs out of charge.

#### Environment
Environment is configured in main.py and defines the "room" the vacuum is cleaning.

#### Actuators
States are represented by print statements.

#### Sensors
The environment includes a battery sensor, a dusty spot sensor, and the user interface that
determines spot or general cleaning.
