import bt_library as btl
import bt.decorators.timer as tm
from ..globals import SPOT_CLEANING, DUSTY_SPOT_SENSOR


class CleanSpot(btl.Task):
    """
    Implementation of the Task "Clean Spot".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Cleaning Spot.")
        return self.report_succeeded(blackboard)
