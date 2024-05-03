# Car Rental System: ATM (Single Machine)
#   - Pseudocoded response, with data structures outlined

# Requirements:
#   - ATM Machine
#       - A user can scan their card -> if it's a valid card, they must input their PIN to access further account features. If not valid, throw error and return to menu.
#       - Once a user has been validated with card + PIN, they can 1) view account balances, 2) withdraw money, and 3) deposit money.

# class ATM:
#   - id: -> unique ID for this ATM
#   - location: -> location of the ATM
#   - current_user: Can be 1) not logged in (None) OR 2) logged in by a user (AccountHolder)
#   - current_cash_reserves: float -> This could be more complicated, such as allowing a user to select which bills to withdraw. This would require a different data structure (Dict) to track how many of each bill we have.
#   - Functionality required to validate a card + PIN, and then retrieve the account info needed (account_balance, name, etc.)
#       - Assuming an external API here:
#           - def login(self, card_number, PIN) -> When a cardholder tries to use the ATM, they will be "logged in" if they input correct info.
#               - Abstraction of Keypad to allow input of PIN
#               - Abstraction of swiping card to retrieve info from card
#               - If login is successful, log user in, and stay logged in for x minutes. -> return AccountHolder class which contains user's info incl. account balance.
#               - If unsuccessful, redirect to main screen with an error message saying "incorrect account info".

# Functionality for business:
#   - def add_cash_reserves(self, amount):
#       - Increases the current_cash_reserves of the ATM.


# class AccountHolder:
#   - account_balance: float
#   - name: str
#   - other_info.....

# If logged in, the ATM screen should show options to 1) view account balances, 2) withdraw money, and 3) deposit money.

#   - def view_balance(self):
#       - Allows user to view the balance of their account (assuming only 1 account for simplicity).
#   - def withdraw_money(self, amount):
#       - if full amount is available in BOTH the Account and the ATM, withdraw that amount and reduce each by that amount.
#       - if full amount isn't available, withdraw the max possible amount and send a message to the user containing the rationale.
#   - def deposit_cash(self, amount):
#       - Increase the ATM's and the AccountHolder's balances by amount.
#       - Some API needed to convert the cash inserted into a $ number via counting.
#       - Simplifying things here by assuming that cash doesn't need to be validated.
#   - def deposit_check(self, amount):
#       - Increase the AccountHolder's balance by amount. -> this will need to be sent to the bank, as well (to update that user's account).
#       - Some API needed to validate the check -> abstracted.
#       - DO NOT increase the ATM balance, because it isn't cash.


# Summary -> ATM allows user to "login" via API that connects to the bank/account_info for the user -> when a user logs in, the ATM status shows that the user is logged in ->
#   -> When a user is logged in, we can 1) view account balances, 2) withdraw money, and 3) deposit money.
#   - When a user withdraws money, we can only give the min balance between the user's balance and the ATM's balance (assuming no overdraft).