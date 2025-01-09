import bt_library as btl


class Sequence(btl.Composite):
    """
    Specific implementation of the selection composite.
    """

    def __init__(self, children: btl.NodeListType) -> object:
        """
        Default constructor.

        :param children: List of children for this node
        """
        super().__init__(children)

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """
        running_child = self.additional_information(blackboard, 0)

        for child_position in range(running_child, len(self.children)):
            child = self.children[child_position]

            result_child = child.run(blackboard)
            # If next child fails, report failed
            if result_child == btl.ResultEnum.FAILED:
                return self.report_failed(blackboard, 0)
            # If child reports running, report RUNNING
            if result_child == btl.ResultEnum.RUNNING:
                return self.report_running(blackboard, child_position)
        # Report success
        return self.report_succeeded(blackboard, 0)
