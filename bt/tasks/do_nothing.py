import bt_library as btl


class DoNothing(btl.Task):
    """
        Implementation of the Task "Do Nothing".
    """

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('All Done!')
        return self.report_succeeded(blackboard)
