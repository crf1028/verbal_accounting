from constant import *


class Account:
    def __init__(self, amount):
        try:
            self._amount = round(float(amount), 2)
        except ValueError:
            raise ValueError
        self._account_type = {"main": "none", "2nd": "none", "3rd": None}

    def __add__(self, other):
        if isinstance(other, Account):
            if self._account_type["main"] != "none" and other._account_type["main"] != "none":
                if self._account_type["main"] == A or self._account_type["main"] == E:
                    if other._account_type["main"] == A or other._account_type["main"] == E:
                        return self.__class__(self._amount + other._amount)
                    else:
                        return self.__class__(self._amount - other._amount)
                else:
                    if other._account_type["main"] == A or other._account_type["main"] == E:
                        return self.__class__(self._amount - other._amount)
                    else:
                        return self.__class__(self._amount + other._amount)
            else:
                raise ValueError
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Account):
            if self._account_type["main"] != "none" and other._account_type["main"] != "none":
                if self._account_type["main"] == A or self._account_type["main"] == E:
                    if other._account_type["main"] == A or other._account_type["main"] == E:
                        return self.__class__(self._amount - other._amount)
                    else:
                        return self.__class__(self._amount + other._amount)
                else:
                    if other._account_type["main"] == A or other._account_type["main"] == E:
                        return self.__class__(self._amount + other._amount)
                    else:
                        return self.__class__(self._amount - other._amount)
            else:
                raise ValueError
        else:
            raise TypeError

    def get_account_type(self, layer=None):
        # return the current account type of select account, parameter could be none, 'main', '2nd', 'main_2nd'
        # return type: dict
        if layer is not None:
            type2show = layer.split('_')
            dict2return = {}
            try:
                for item in type2show:
                    dict2return[item] = self._account_type[item]
            except KeyError:
                raise KeyError
            else:
                return dict2return
        else:
            return self._account_type

    def set_account_type(self, layer, act_type):
        try:
            self._account_type[layer]
        except KeyError:
            raise KeyError
        else:
            self._account_type[layer] = act_type

    def set_amount(self, amount):
        try:
            self._amount = round(float(amount), 2)
        except ValueError:
            raise ValueError

    def get_amount(self):
        return self._amount

    def check_ledger_side(self):            # can be added to previous written code
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

    def __str__(self):
        return "Account Type: %r \nBalance: %r\n" % (self._account_type, self._amount)


# ---------------------Asset starts------------------
class Asset(Account):
    def __init__(self, amount):
        Account.__init__(self, amount)
        self._account_type["main"] = A


class Cash(Asset):
    def __init__(self, amount):
        Asset.__init__(self, amount)
        self._account_type["2nd"] = CASH


class AccountsReceivable(Asset):
    def __init__(self, amount):
        Asset.__init__(self, amount)
        self._account_type["2nd"] = AR


class Inventory(Asset):  # active account
    def __init__(self, amount):
        Asset.__init__(self, amount)
        self._account_type["2nd"] = INV


class MerchandiseInventory(Inventory):
    def __init__(self, amount):
        Inventory.__init__(self, amount)
        self._account_type["3rd"] = MERCHANT_INV


class Supplies(Asset):
    def __init__(self, amount):
        Asset.__init__(self, amount)
        self._account_type["2nd"] = SUPPLY


class PrepaidExpenses(Asset):
    def __init__(self, amount):
        Asset.__init__(self, amount)
        self._account_type["2nd"] = PRE_EXP


class Land(Asset):
    def __init__(self, amount):
        Asset.__init__(self, amount)
        self._account_type["2nd"] = LAND


class Buildings(Asset):
    def __init__(self, amount):
        Asset.__init__(self, amount)
        self._account_type["2nd"] = BUILD


class Equipment(Asset):
    def __init__(self, amount):
        Asset.__init__(self, amount)
        self._account_type["2nd"] = EQUIP


class Goodwill(Asset):
    def __init__(self, amount):
        Asset.__init__(self, amount)
        self._account_type["2nd"] = GOODWILL
# ---------------------Asset ends------------------------


# ---------------------Liability starts------------------
class Liability(Account):
    def __init__(self, amount):
        Account.__init__(self, amount)
        self._account_type["main"] = L


class AccountsPayable(Liability):
    def __init__(self, amount):
        Liability.__init__(self, amount)
        self._account_type["2nd"] = AP


class NotesPayable(Liability):
    def __init__(self, amount):
        Liability.__init__(self, amount)
        self._account_type["2nd"] = NOTE_P


class SalariesPayable(Liability):
    def __init__(self, amount):
        Liability.__init__(self, amount)
        self._account_type["2nd"] = SALA_P


class WagesPayable(Liability):
    def __init__(self, amount):
        Liability.__init__(self, amount)
        self._account_type["2nd"] = WAG_P


class InterestPayable(Liability):
    def __init__(self, amount):
        Liability.__init__(self, amount)
        self._account_type["2nd"] = INT_P


class IncomeTaxesPayable(Liability):
    def __init__(self, amount):
        Liability.__init__(self, amount)
        self._account_type["2nd"] = I_TAX_P


class UnearnedRevenue(Liability):
    def __init__(self, amount):
        Liability.__init__(self, amount)
        self._account_type["2nd"] = UR
# ------------------Liability ends------------------


# -------------OwnersEquity starts------------------
class OwnersEquity(Account):
    def __init__(self, amount):
        Account.__init__(self, amount)
        self._account_type["main"] = OE


class Revenue(OwnersEquity):
    def __init__(self, amount):
        OwnersEquity.__init__(self, amount)
        self._account_type["2nd"] = REV


class InitialInvestment(OwnersEquity):
    def __init__(self, amount):
        OwnersEquity.__init__(self, amount)
        self._account_type["2nd"] = INT_INVST


class Expense(Account):
    def __init__(self, amount):
        Account.__init__(self, amount)
        self._account_type["main"] = E


class SalariesExpense(Expense):
    def __init__(self, amount):
        Expense.__init__(self, amount)
        self._account_type["2nd"] = SALA_EXP


class RentExpense(Expense):
    def __init__(self, amount):
        Expense.__init__(self, amount)
        self._account_type["2nd"] = RENT_EXP


class WagesExpense(Expense):
    def __init__(self, amount):
        Expense.__init__(self, amount)
        self._account_type["2nd"] = WAG_EXP


class CostOfGoodsSold(Expense):
    def __init__(self, amount):
        Expense.__init__(self, amount)
        self._account_type["2nd"] = COGS


accounts_dict = {A: Asset, CASH: Cash, AR: AccountsReceivable, INV: Inventory, MERCHANT_INV: MerchandiseInventory,
                 SUPPLY: Supplies, PRE_EXP: PrepaidExpenses, LAND: Land, BUILD: Buildings, EQUIP: Equipment,
                 GOODWILL: Goodwill, L: Liability, AP: AccountsPayable, NOTE_P: NotesPayable,
                 SALA_P: SalariesPayable, WAG_P: WagesPayable, INT_P: InterestPayable, I_TAX_P: IncomeTaxesPayable,
                 UR: UnearnedRevenue, OE: OwnersEquity, REV: Revenue, INT_INVST: InitialInvestment, E: Expense,
                 COGS: CostOfGoodsSold, SALA_EXP: SalariesExpense, RENT_EXP: RentExpense, WAG_EXP: WagesExpense}


if __name__ == "__main__":
    ''' Testing '''
    # A001 = Cash(1000)
    # E001 = Expense(200)
    # L001 = Liability('70')
    # OE001 = OwnersEquity('6.789')
    # A004 = Buildings(700)
    # A003 = MerchandiseInventory(500)
    # lst = [A001, E001, L001, OE001]

    # print isinstance(A001, Account), isinstance(A001, Asset), isinstance(A001, Cash)
    #
    # for i in lst:
    #     print i._amount, i._account_type
    #
    # print A001 + E001, A001 + L001
    #
    # acnt = Account(90)
    # print acnt.get_account_type().values() == ['none', 'none']
    # # A002 = Account(70)
    # # print A001.__class__, A002.__class__
    #
    # print A001 + E001 + L001 + OE001 - A004 - A003
    # print reduce(lambda x,y: x+y, [Cash(-50)])
    # A001 -= L001
    # print A001

    A001 = Cash(9000)
    R001 = Revenue(11000)
    Ar001 = AccountsReceivable(0)
    print Ar001-A001
    print Ar001-R001
    print Ar001-A001-R001
    print Ar001-R001-A001
    Ar001-=A001
    Ar001-=R001
    print Ar001