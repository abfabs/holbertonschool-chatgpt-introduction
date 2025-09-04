#!/usr/bin/python3
class Checkbook:
    """Function Description:
    A simple checkbook that supports deposits, withdrawals, and balance queries.

    Parameters:
        None

    Returns:
        None
    """

    def __init__(self):
        """Function Description:
        Initialize the checkbook with a zero starting balance.

        Parameters:
            None

        Returns:
            None
        """
        self.balance = 0.0

    def deposit(self, amount):
        """Function Description:
        Deposit a non-negative amount into the checkbook.

        Parameters:
            amount (float): The amount to deposit; must be >= 0.

        Returns:
            None
        """
        if amount < 0:
            print("Amount must be non-negative.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """Function Description:
        Withdraw a non-negative amount if sufficient funds are available.

        Parameters:
            amount (float): The amount to withdraw; must be >= 0.

        Returns:
            None
        """
        if amount < 0:
            print("Amount must be non-negative.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Function Description:
        Print the current balance.

        Parameters:
            None

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def _read_amount(prompt):
    """Function Description:
    Repeatedly prompt the user for a monetary amount until a valid number is entered.

    Parameters:
        prompt (str): The prompt text shown to the user.

    Returns:
        float: A non-negative amount entered by the user.
               Returns None if input is interrupted (EOF/KeyboardInterrupt).
    """
    while True:
        try:
            raw = input(prompt).strip()
            # Allow optional $ and commas, e.g., "$1,234.56"
            cleaned = raw.replace("$", "").replace(",", "")
            amount = float(cleaned)
            if amount < 0:
                print("Amount must be non-negative. Try again.")
                continue
            return amount
        except ValueError:
            print("Invalid amount. Please enter a number (e.g., 12.34).")
        except (EOFError, KeyboardInterrupt):
            # Graceful abort back to main menu
            print()
            return None


def main():
    """Function Description:
    Run an interactive loop to operate the checkbook.

    Parameters:
        None

    Returns:
        None
    """
    cb = Checkbook()
    while True:
        try:
            action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if action == 'exit':
            break
        elif action == 'deposit':
            amount = _read_amount("Enter the amount to deposit: $")
            if amount is not None:
                cb.deposit(amount)
        elif action == 'withdraw':
            amount = _read_amount("Enter the amount to withdraw: $")
            if amount is not None:
                cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
