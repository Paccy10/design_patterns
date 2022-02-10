from .command import Command
from ..customer_service import CustomerService


class AddCustomerCommand(Command):

    def __init__(self, service: CustomerService):
        self.__service = service

    def execute(self):
        return self.__service.add_customer()
