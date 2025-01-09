import bt_library as btl
from ..globals import SPOT_CLEANING


class DoneSpot(btl.Task):
    """
    Implementation of the Task "Done Spot".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        # Reset SPOT cleaning in blackboard to false
        blackboard.set_in_environment(SPOT_CLEANING, False)
        self.print_message("Spot cleaning complete.")
        return self.report_succeeded(blackboard)
