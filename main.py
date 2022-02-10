
from command.customer_service import CustomerService
from command.fx.add_customer_command import AddCustomerCommand
from command.fx.button import Button


def main():
    service = CustomerService()
    command = AddCustomerCommand(service)
    button = Button(command)
    button.click()


if __name__ == "__main__":
    main()
