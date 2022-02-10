from .audit_trail import AuditTrail
from .task import Task


class TransferMoneyTask(Task):

    def _do_execute(self):
        print("Transfer money")
