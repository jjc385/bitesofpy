from functools import total_ordering

@total_ordering
class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    # add dunder methods below

    def __len__(self):
        return len(self._transactions)


    def __gt__(self, account):
        return self.balance > account.balance
    def __eq__(self, account):
        return self.balance == account.balance


    def __getitem__(self, index):
        return self._transactions[index]

    
    def __iter__(self):
        return iter(self._transactions)


    ## TODO -- see whether there's a more concise way to do this
    def __add__(self, amount):
        if not isinstance(amount, int):
            raise ValueError("Expected amount added to be an integer, not {}".format(amount))
        self._transactions.append(amount)
    def __sub__(self, amount):
        if not isinstance(amount, int):
            raise ValueError("Expected amount subtracted to be an integer, not {}".format(amount))
        self._transactions.append(-amount)


    def __str__(self):
        return "{} account - balance: {}".format(self.name, self.balance)
