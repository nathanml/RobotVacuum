import bt_library as btl
import bt.decorators.until_fails as uf
import random
from ..globals import CLEAN_FLOOR_PROBABILITY


class CleanFloor(btl.Task):
    """
        Implementation of the Task "Clean Spot".
    """

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        # Else floor is still not clean, report running
        self.print_message("Cleaning floor")
        # Random number generator to check when floor is clean
        if random.randint(0, 100) < CLEAN_FLOOR_PROBABILITY:
            # No more floor to clean, report fail
            return self.report_failed(blackboard)
        # Else continue running
        else:
            return self.report_running(blackboard)
