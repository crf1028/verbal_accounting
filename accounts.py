from constant import *


class Account:
    """Base type of all accounts, has 2 main attribute: amount and account types."""
    def __init__(self, amount):
        try:
            self._amount = round(float(amount), 2)
        except ValueError:
            raise ValueError
        self._account_type = {MAIN: None, SECOND: None, THIRD: None}

    def __add__(self, other):
        """The result of arithmetic operating between two accounts are determined by the account types."""
        if isinstance(other, Account):
            if self._account_type[MAIN] == A or self._account_type[MAIN] == E:
                if other._account_type[MAIN] == A or other._account_type[MAIN] == E:
                    return self.__class__(self._amount + other._amount)
                else:
                    return self.__class__(self._amount - other._amount)
            else:
                if other._account_type[MAIN] == A or other._account_type[MAIN] == E:
                    return self.__class__(self._amount - other._amount)
                else:
                    return self.__class__(self._amount + other._amount)
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Account):
            if self._account_type[MAIN] == A or self._account_type[MAIN] == E:
                if other._account_type[MAIN] == A or other._account_type[MAIN] == E:
                    return self.__class__(self._amount - other._amount)
                else:
                    return self.__class__(self._amount + other._amount)
            else:
                if other._account_type[MAIN] == A or other._account_type[MAIN] == E:
                    return self.__class__(self._amount + other._amount)
                else:
                    return self.__class__(self._amount - other._amount)
        else:
            raise TypeError

    def __str__(self):
        if self.check_ledger_side() == "dr":
            return "Dr.{: >20}{: >15,.2f}\n".format(self._account_type[SECOND], abs(self._amount))
        else:
            return "Cr.{: >25}{: >15,.2f}\n".format(self._account_type[SECOND], abs(self._amount))

    def __nonzero__(self):
        """Check if the account amount is 0 or not."""
        return bool(self._amount)

    def get_account_type(self):
        """Return the account types of an account"""
        return self._account_type[MAIN], self._account_type[SECOND], self._account_type[THIRD]

    def get_amount(self):
        return self._amount

    def check_ledger_side(self):            # can be added to previous written code
        """Check an account is on the dr side or cr side."""
        if self._account_type[MAIN] == A or self._account_type[MAIN] == E:
            if self._amount > 0:
                return "dr"
            else:
                return "cr"
        elif self._account_type[MAIN] == OE or self._account_type[MAIN] == L:
            if self._amount > 0:
                return "cr"
            else:
                return "dr"
        else:
            raise ValueError


# ---------------------Asset starts------------------
class Asset(Account):
    def __init__(self, amount):
        Account.__init__(self, amount)
        self._account_type[MAIN] = A


class Cash(Asset):
    def __init__(self, amount):
        Asset.__init__(self, amount)
        self._account_type[SECOND] = CASH


class AccountsReceivable(Asset):
    def __init__(self, amount):
        Asset.__init__(self, amount)
        self._account_type[SECOND] = AR


class Inventory(Asset):  # active account
    def __init__(self, amount):
        Asset.__init__(self, amount)
        self._account_type[SECOND] = INV


class MerchandiseInventory(Inventory):
    def __init__(self, amount):
        Inventory.__init__(self, amount)
        self._account_type[THIRD] = MERCHANT_INV


class Supplies(Asset):
    def __init__(self, amount):
        Asset.__init__(self, amount)
        self._account_type[SECOND] = SUPPLY


class PrepaidExpenses(Asset):
    def __init__(self, amount):
        Asset.__init__(self, amount)
        self._account_type[SECOND] = PRE_EXP


class Land(Asset):
    def __init__(self, amount):
        Asset.__init__(self, amount)
        self._account_type[SECOND] = LAND


class Buildings(Asset):
    def __init__(self, amount):
        Asset.__init__(self, amount)
        self._account_type[SECOND] = BUILD


class Equipment(Asset):
    def __init__(self, amount):
        Asset.__init__(self, amount)
        self._account_type[SECOND] = EQUIP


class Goodwill(Asset):
    def __init__(self, amount):
        Asset.__init__(self, amount)
        self._account_type[SECOND] = GOODWILL
# ---------------------Asset ends------------------------


# ---------------------Liability starts------------------
class Liability(Account):
    def __init__(self, amount):
        Account.__init__(self, amount)
        self._account_type[MAIN] = L


class AccountsPayable(Liability):
    def __init__(self, amount):
        Liability.__init__(self, amount)
        self._account_type[SECOND] = AP


class NotesPayable(Liability):
    def __init__(self, amount):
        Liability.__init__(self, amount)
        self._account_type[SECOND] = NOTE_P


class SalariesPayable(Liability):
    def __init__(self, amount):
        Liability.__init__(self, amount)
        self._account_type[SECOND] = SALA_P


class WagesPayable(Liability):
    def __init__(self, amount):
        Liability.__init__(self, amount)
        self._account_type[SECOND] = WAG_P


class InterestPayable(Liability):
    def __init__(self, amount):
        Liability.__init__(self, amount)
        self._account_type[SECOND] = INT_P


class IncomeTaxesPayable(Liability):
    def __init__(self, amount):
        Liability.__init__(self, amount)
        self._account_type[SECOND] = I_TAX_P


class UnearnedRevenue(Liability):
    def __init__(self, amount):
        Liability.__init__(self, amount)
        self._account_type[SECOND] = UR
# ------------------Liability ends------------------


# -------------OwnersEquity starts------------------
class OwnersEquity(Account):
    def __init__(self, amount):
        Account.__init__(self, amount)
        self._account_type[MAIN] = OE


class Revenue(OwnersEquity):
    def __init__(self, amount):
        OwnersEquity.__init__(self, amount)
        self._account_type[SECOND] = REV


class InitialInvestment(OwnersEquity):
    def __init__(self, amount):
        OwnersEquity.__init__(self, amount)
        self._account_type[SECOND] = INT_INVST


class Expense(Account):
    def __init__(self, amount):
        Account.__init__(self, amount)
        self._account_type[MAIN] = E


class SalariesExpense(Expense):
    def __init__(self, amount):
        Expense.__init__(self, amount)
        self._account_type[SECOND] = SALA_EXP


class RentExpense(Expense):
    def __init__(self, amount):
        Expense.__init__(self, amount)
        self._account_type[SECOND] = RENT_EXP


class WagesExpense(Expense):
    def __init__(self, amount):
        Expense.__init__(self, amount)
        self._account_type[SECOND] = WAG_EXP


class CostOfGoodsSold(Expense):
    def __init__(self, amount):
        Expense.__init__(self, amount)
        self._account_type[SECOND] = COGS


accounts_dict = {A: Asset, CASH: Cash, AR: AccountsReceivable, INV: Inventory, MERCHANT_INV: MerchandiseInventory,
                 SUPPLY: Supplies, PRE_EXP: PrepaidExpenses, LAND: Land, BUILD: Buildings, EQUIP: Equipment,
                 GOODWILL: Goodwill, L: Liability, AP: AccountsPayable, NOTE_P: NotesPayable,
                 SALA_P: SalariesPayable, WAG_P: WagesPayable, INT_P: InterestPayable, I_TAX_P: IncomeTaxesPayable,
                 UR: UnearnedRevenue, OE: OwnersEquity, REV: Revenue, INT_INVST: InitialInvestment, E: Expense,
                 COGS: CostOfGoodsSold, SALA_EXP: SalariesExpense, RENT_EXP: RentExpense, WAG_EXP: WagesExpense}


if __name__ == "__main__":
    ''' Testing '''
    acnt1 = Cash(500000)
    lia = UnearnedRevenue(80)
