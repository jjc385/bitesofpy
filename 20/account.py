class Account:

    def __init__(self):
        self._transactions = []
        self._safeMode = False

    @property
    def balance(self):
        return sum(self._transactions)

    def _doTransaction(self, amount):
        if self._safeMode and self.balance + amount < 0:
            return False
        self._transactions.append(amount)
        return True

    def __add__(self, amount):
        self._doTransaction(amount)

    def __sub__(self, amount):
        self._doTransaction(-amount)

    # add 2 dunder methods here to turn this class 
    # into a 'rollback' context manager

    def __enter__(self):
        self._safeMode = True
        return self


    def __exit__(self, type, value, traceback):
        self._safeMode = False

