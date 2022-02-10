from abc import ABC, abstractmethod

from .audit_trail import AuditTrail


class Task(ABC):
    __audit_trail = None

    def __init__(self):
        self.__audit_trail = AuditTrail()

    def execute(self):
        self.__audit_trail.record()
        self._do_execute()

    @abstractmethod
    def _do_execute():
        pass
