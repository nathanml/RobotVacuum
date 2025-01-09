"""
   Specific implementation of the robot behavior tree.
"""

import bt as bt
import bt_library as btl

# Instantiate the tree according to the assignment

# Charge Sequence
charge_sequence = bt.Sequence(
    [
        bt.BatteryLessThan30(),
        bt.FindHome(),
        bt.GoHome(),
        bt.Charge()
    ]
)

# Spot Cleaning Sequence
spot_cleaning_sequence = bt.Sequence(
    [
        bt.SpotCleaning(),
        bt.Timer(20, bt.CleanSpot()),
        bt.DoneSpot()
    ]
)

# Dusty Spot Sequence
dusty_spot_sequence = bt.Sequence(
    [
        bt.DustySpot(),
        bt.Timer(35, bt.CleanSpot()),
        bt.AlwaysFail()
    ]
)

# Clean floor priority node
clean_floor_pattern = bt.Priority(
    [
        dusty_spot_sequence,
        bt.UntilFails(bt.CleanFloor())
    ],
    [0, 1]
)

general_cleaning_sequence = bt.Sequence(
    [
        bt.GeneralCleaning(),
        bt.Sequence(
            [
                clean_floor_pattern,
                bt.DoneGeneral()
            ]
        )
    ]
)

user_selection = bt.Selection(
    [
        spot_cleaning_sequence,
        general_cleaning_sequence
    ]
)

tree_root = bt.Priority(
    [
        charge_sequence,
        user_selection,
        bt.DoNothing()
    ],
    [0, 1, 2]
)

#

# Store the root node in a behavior tree instance
robot_behavior = btl.BehaviorTree(tree_root)
