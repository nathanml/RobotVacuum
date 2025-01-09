import bt_library
from bt_library.blackboard import Blackboard
from bt_library.common import ResultEnum
from bt_library.tree_node import TreeNode


class UntilFails(bt_library.Decorator):
    """
       Specific implementation of the until fails decorator.
    """

    def __init__(self, child: TreeNode):
        """
        Default constructor.
        :param child: Child associated to the decorator
        """
        super().__init__(child)

    def run(self, blackboard: Blackboard) -> ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """
        child_status = self.child.run(blackboard)
        # If child fails, succeed
        if child_status == ResultEnum.FAILED:
            return self.report_succeeded(blackboard)
        # Else, continue running
        else:
            return self.report_running(blackboard)
