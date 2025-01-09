import bt_library as btl
from ..globals import DUSTY_SPOT_SENSOR


class DustySpot(btl.Task):
    """
       Implementation of the condition "Dusty Spot". This condition
       checks if there is dust sensed in the current location.
    """

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Checking if dusty spot')
        # If dusty spot is detected, succeed
        if blackboard.get_in_environment(DUSTY_SPOT_SENSOR, False):
            return self.report_succeeded(blackboard)
        # Else fail
        return self.report_failed(blackboard)
