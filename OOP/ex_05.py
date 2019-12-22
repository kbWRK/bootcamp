class CashMachine:
    def __init__(self, ):
        self._money = []

    def put_money(self, *args):
        self._money = [*args]

    def is_available(self):
        return bool(self._money)

    def withdraw_money(self, robbery):
        self._money.sort(reverse=True)
        colected_money = 0
        colected_bills = []
        if sum(self._money) < robbery:
            return False
        for bill in self._money:
            if bill + colected_money == robbery:
                colected_money += bill
                colected_bills.append(bill)
        if colected_money == robbery:
            for bill in colected_bills:
                self._money.remove(bill)
                return colected_bills

        # for bill in self._money:
        #     if bill % robbery == 1:
        #         self._money.pop(self._money.index(bill))
        # ...


def test_CashMachine_is_available():
    machine = CashMachine()
    assert machine.is_available() == False

# Przykład
# uzycia:
# >> > cash_machine = CashMachine()
# >> > cash_machine.is_available()
# False
# >> > cash_machine.put_money([200, 100, 100, 50])
# >> > cash_machine.is_available()
# True
# >> > cash_machine.withdraw_money(150)
