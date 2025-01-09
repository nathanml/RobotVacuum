import bt_library as btl
from ..globals import CHARGING
from ..globals import BATTERY_LEVEL


class Charge(btl.Task):
    """
        Implementation of the Task "Charge".
        Charges battery 10% each run. BT should default
        to this state when no command entered.
    """

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        blackboard.set_in_environment(CHARGING, True)
        self.print_message('Vacuum charging')
        # If the battery is not yet charged, report running
        if blackboard.get_in_environment(BATTERY_LEVEL, 0) != 100:
            return self.report_running(blackboard)
        # Iff battery is fully charged, stop charging and report success
        else:
            blackboard.set_in_environment(CHARGING, False)
            return self.report_succeeded(blackboard)
