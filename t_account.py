from accounts import *
from datetime import datetime


class TAccountCollection:       # income statement & other maybe
    def __init__(self, owner=None):
        self._open_date = datetime.now().strftime('%Y-%m-%d %H:%M')
        self._close_date = None
        self._owner = owner
        self.content = {}
        for key, value in t_accounts_dict.items():
            self.content[key] = value()

    def __str__(self):
        return "Date Opened: %r \nDate Closed: %r\nOwner: %r \n" % (self._open_date, self._close_date, self._owner.name)

    def add_tacnt(self, name, tacnt):
        try:
            self.content[name]
        except:
            self.content[name] = tacnt         # avoid multiple tacnts

    def get_content(self):
        for key, value in self.content.items():
            if value.get_balance() != 0:
                print "%s: %d\n" % (key, value.get_balance())


class TAccount:
    def __init__(self):
        self._dr_side = []
        self._cr_side = []
        self._begin = Account(0.00)
        self._ending = Account(0.00)
        self._name = "none"
        self._t_account_type = {"main": "none", "2nd": "none", "3rd": None}

    def add(self, acnt):            # maybe could be better
        if isinstance(acnt, Account):
            # acnt_type = acnt.get_account_type()     # check all types here, can be modified to only check some types
            if acnt.get_account_type()[MAIN] == self._t_account_type[MAIN]:
                if acnt.check_ledger_side() == "dr":
                    self._dr_side.extend([acnt])
                elif acnt.check_ledger_side() == "cr":
                    self._cr_side.extend([acnt])
                self._ending.set_amount(self._ending.get_amount() + acnt.get_amount())
            else:
                raise ValueError
        else:
            raise TypeError

    def set_begin(self, acnt):
        if isinstance(acnt, Account):
            self._begin = acnt
        else:
            raise TypeError

    def get_balance(self):
        return self._ending.get_amount()

    def get_account_type(self, layer=None):
        if layer is not None:
            type2show = layer.split('_')
            dict2return = {}
            try:
                for item in type2show:
                    dict2return[item] = self._t_account_type[item]
            except KeyError:
                raise KeyError
            else:
                return dict2return
        else:
            return self._t_account_type


# ---------------------T-account for Asset starts------------------
class TAcntAsset(TAccount):
    def __init__(self):
        TAccount.__init__(self)
        self._t_account_type["main"] = A
        self._begin.set_account_type("main", A)
        self._ending.set_account_type("main", A)


class TAcntCash(TAcntAsset):
    def __init__(self):
        TAcntAsset.__init__(self)
        self._t_account_type["2nd"] = CASH
        self._begin.set_account_type("2nd", CASH)
        self._ending.set_account_type("2nd", CASH)


class TAcntAccountsReceivable(TAcntAsset):
    def __init__(self):
        TAcntAsset.__init__(self)
        self._t_account_type["2nd"] = AR
        self._begin.set_account_type("2nd", AR)
        self._ending.set_account_type("2nd", AR)


class TAcntInventory(TAcntAsset):
    def __init__(self):
        TAcntAsset.__init__(self)
        self._t_account_type["2nd"] = INV
        self._begin.set_account_type("2nd", INV)
        self._ending.set_account_type("2nd", INV)


class TAcntMerchandiseInventory(TAcntInventory):
    def __init__(self):
        TAcntInventory.__init__(self)
        self._t_account_type[THIRD] = MERCHANT_INV
        self._begin.set_account_type(THIRD, MERCHANT_INV)
        self._ending.set_account_type(THIRD, MERCHANT_INV)


class TAcntSupplies(TAcntAsset):
    def __init__(self):
        TAcntAsset.__init__(self)
        self._t_account_type["2nd"] = SUP
        self._begin.set_account_type("2nd", SUP)
        self._ending.set_account_type("2nd", SUP)


class TAcntPrepaidExpenses(TAcntAsset):
    def __init__(self):
        TAcntAsset.__init__(self)
        self._t_account_type["2nd"] = PRE_EXP
        self._begin.set_account_type("2nd", PRE_EXP)
        self._ending.set_account_type("2nd", PRE_EXP)


class TAcntLand(TAcntAsset):
    def __init__(self):
        TAcntAsset.__init__(self)
        self._t_account_type["2nd"] = LAND
        self._begin.set_account_type("2nd", LAND)
        self._ending.set_account_type("2nd", LAND)


class TAcntBuildings(TAcntAsset):
    def __init__(self):
        TAcntAsset.__init__(self)
        self._t_account_type["2nd"] = BUILD
        self._begin.set_account_type("2nd", BUILD)
        self._ending.set_account_type("2nd", BUILD)


class TAcntEquipment(TAcntAsset):
    def __init__(self):
        TAcntAsset.__init__(self)
        self._t_account_type["2nd"] = EQUIP
        self._begin.set_account_type("2nd", EQUIP)
        self._ending.set_account_type("2nd", EQUIP)


class TAcntGoodwill(TAcntAsset):
    def __init__(self):
        TAcntAsset.__init__(self)
        self._t_account_type["2nd"] = GOODWILL
        self._begin.set_account_type("2nd", GOODWILL)
        self._ending.set_account_type("2nd", GOODWILL)
# ---------------------T-account for Asset ends----------------------------


# ---------------------T-account for Liability ends------------------------
class TAcntLiability(TAccount):
    def __init__(self):
        TAccount.__init__(self)
        self._t_account_type["main"] = L


class TAcntAccountsPayable(TAcntLiability):
    def __init__(self):
        TAcntLiability.__init__(self)
        self._t_account_type[SECOND] = AP
        self._begin.set_account_type(SECOND, AP)
        self._ending.set_account_type(SECOND, AP)


class TAcntOwnersEquity(TAccount):
    def __init__(self):
        TAccount.__init__(self)
        self._t_account_type["main"] = OE


class TAcntRevenue(TAcntOwnersEquity):
    def __init__(self):
        TAcntOwnersEquity.__init__(self)
        self._t_account_type[SECOND] = REV
        self._begin.set_account_type(SECOND, REV)
        self._ending.set_account_type(SECOND, REV)


class TAcntInitialInvestment(TAcntOwnersEquity):
    def __init__(self):
        TAcntOwnersEquity.__init__(self)
        self._t_account_type[SECOND] = INT_INVST
        self._begin.set_account_type(SECOND, INT_INVST)
        self._ending.set_account_type(SECOND, INT_INVST)


class TAcntExpense(TAccount):
    def __init__(self):
        TAccount.__init__(self)
        self._t_account_type["main"] = E


class TAcntCostOfGoodsSold(TAcntExpense):
    def __init__(self):
        TAcntExpense.__init__(self)
        self._t_account_type[SECOND] = COGS
        self._begin.set_account_type(SECOND, COGS)
        self._ending.set_account_type(SECOND, COGS)


class TAcntSalariesExpense(TAcntExpense):
    def __init__(self):
        TAcntExpense.__init__(self)
        self._t_account_type[SECOND] = SALA_EXP
        self._begin.set_account_type(SECOND, SALA_EXP)
        self._ending.set_account_type(SECOND, SALA_EXP)


class TAcntRentExpense(TAcntExpense):
    def __init__(self):
        TAcntExpense.__init__(self)
        self._t_account_type[SECOND] = RENT_EXP
        self._begin.set_account_type(SECOND, RENT_EXP)
        self._ending.set_account_type(SECOND, RENT_EXP)


t_accounts_dict = {A: TAcntAsset, CASH: TAcntCash, AR: TAcntAccountsReceivable, INV: TAcntInventory,
                   MERCHANT_INV: TAcntMerchandiseInventory, SUP: TAcntSupplies, PRE_EXP: TAcntPrepaidExpenses,
                   LAND: TAcntLand, BUILD: TAcntBuildings, EQUIP: TAcntEquipment, GOODWILL: TAcntGoodwill,
                   L: TAcntLiability, AP: TAcntAccountsPayable, OE: TAcntOwnersEquity, REV: TAcntRevenue,
                   INT_INVST: TAcntInitialInvestment, E: TAcntExpense, COGS: TAcntCostOfGoodsSold,
                   SALA_EXP: TAcntSalariesExpense, RENT_EXP: TAcntRentExpense}


if __name__ == "__main__":
    # testing
    A001 = Cash(1000)
    E001 = Expense(200)
    L001 = Liability('70')
    OE001 = OwnersEquity('6.789')
    A002 = AccountsReceivable(-800)
    lst = [A001, E001, L001, OE001]
    # for i in lst:
    #     print i._amount, i._account_type
    #
    # print A001 + E001, A001 + L001, OE001 - A001, A001 + A002

    TA_A001 = TAcntCash()
    TA_A001.add(A001)
    print TA_A001.get_balance()


