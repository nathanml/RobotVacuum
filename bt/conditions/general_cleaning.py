import bt_library as btl
from ..globals import GENERAL_CLEANING


class GeneralCleaning(btl.Task):
    """
           Implementation of the condition "General Cleaning". This condition
           checks if there is general cleaning was selected by user.
    """

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Checking General Cleaning ')
        # If general cleaning selected, succeed
        if blackboard.get_in_environment(GENERAL_CLEANING, False):
            return self.report_succeeded(blackboard)
        #  Else fail
        return self.report_failed(blackboard)