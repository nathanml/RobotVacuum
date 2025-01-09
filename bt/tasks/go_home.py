import bt_library as btl
from ..globals import HOME_PATH


class GoHome(btl.Task):
    """
    Implementation of the Task "Go Home".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        # Read home path from blackboard
        path = blackboard.get_in_environment(HOME_PATH, None)
        self.print_message('Going home : ' + path)
        return self.report_succeeded(blackboard)
