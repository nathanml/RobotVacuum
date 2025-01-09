import bt_library as btl
from ..globals import SPOT_CLEANING


class SpotCleaning(btl.Task):
    """
           Implementation of the condition "Spot Cleaning". This condition
           checks if there is spot cleaning was selected by user.
    """

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Checking Spot Cleaning ')

        # If SPOT CLEANING Sensor is True, succeed
        if blackboard.get_in_environment(SPOT_CLEANING, False):
            return self.report_succeeded(blackboard)
        # Else fail
        return self.report_failed(blackboard)
