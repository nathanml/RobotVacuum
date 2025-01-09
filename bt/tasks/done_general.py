import bt_library as btl
from ..globals import GENERAL_CLEANING, CLEAN_FLOOR


class DoneGeneral(btl.Task):
    """
        Implementation of the Task "Done General".
    """

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        blackboard.set_in_environment(GENERAL_CLEANING, False)
        blackboard.set_in_environment(CLEAN_FLOOR, True)
        self.print_message('General Cleaning Complete!')
        return self.report_succeeded(blackboard)
