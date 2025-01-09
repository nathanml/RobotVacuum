import bt_library as btl


class Priority(btl.Composite):
    """
        Specific implementation of the priority composite.
    """
    orderedChildren: btl.NodeListType

    def __init__(self, children: btl.NodeListType, priorities: [int]):
        """
        Default constructor.

        :param children: List of children for this node
        :param priorities: List of priorities for each child node
        """
        super().__init__(children)
        # Default if no priorities provided
        self.orderedChildren = self.children
        # Sort children by priority
        for child_position in range(len(self.children)):
            self.orderedChildren[priorities[child_position]] = self.children[child_position]

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """

        # Create list of children ordered by priority
        # which is passed in with the child when created

        # Run children in order of priority
        for child_position in range(len(self.orderedChildren)):
            child = self.children[child_position]
            result_child = child.run(blackboard)
            # If any child succeeds, report SUCCESS
            if result_child == btl.ResultEnum.SUCCEEDED:
                return self.report_succeeded(blackboard, 0)
            # If any child is still running, report RUNNING
            if result_child == btl.ResultEnum.RUNNING:
                return self.report_running(blackboard, child_position)

        # If this condition is reached, all children have failed
        # Report failure
        return self.report_failed(blackboard, 0)
