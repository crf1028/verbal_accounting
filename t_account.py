from accounts import Account, accounts_dict
from constant import *
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

    # def add_tacnt(self, name, tacnt):
    #     try:
    #         self.content[name]
    #     except:
    #         self.content[name] = tacnt         # avoid multiple tacnts

    def get_content(self):
        for key, value in self.content.items():
            if value.get_balance() != 0:
                print "%s: %d\n" % (key, value.get_balance())

    def django_value(self):
        to_return = ''
        for key, value in self.content.items():
            if value.get_balance() != 0:
                to_return += "%20s: %20d\n" % (key, value.get_balance())
        return to_return


class TAccount:
    def __init__(self):
        self._dr_side = []
        self._cr_side = []
        self._begin = None
        self._ending = None
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

    def get_ending_acnt(self):
        return self._ending


# ---------------------T-account for Asset starts------------------
class TAcntAsset(TAccount):
    def __init__(self):
        TAccount.__init__(self)
        self._t_account_type["main"] = A
        self._begin = accounts_dict[A](0.00)
        self._ending = accounts_dict[A](0.00)


class TAcntCash(TAcntAsset):
    def __init__(self):
        TAcntAsset.__init__(self)
        self._t_account_type["2nd"] = CASH
        self._begin = accounts_dict[CASH](0.00)
        self._ending = accounts_dict[CASH](0.00)


class TAcntAccountsReceivable(TAcntAsset):
    def __init__(self):
        TAcntAsset.__init__(self)
        self._t_account_type["2nd"] = AR
        self._begin = accounts_dict[AR](0.00)
        self._ending = accounts_dict[AR](0.00)


class TAcntInventory(TAcntAsset):
    def __init__(self):
        TAcntAsset.__init__(self)
        self._t_account_type["2nd"] = INV
        self._begin = accounts_dict[INV](0.00)
        self._ending = accounts_dict[INV](0.00)


class TAcntMerchandiseInventory(TAcntInventory):
    def __init__(self):
        TAcntInventory.__init__(self)
        self._t_account_type[THIRD] = MERCHANT_INV
        self._begin = accounts_dict[MERCHANT_INV](0.00)
        self._ending = accounts_dict[MERCHANT_INV](0.00)


class TAcntSupplies(TAcntAsset):
    def __init__(self):
        TAcntAsset.__init__(self)
        self._t_account_type["2nd"] = SUPPLY
        self._begin = accounts_dict[SUPPLY](0.00)
        self._ending = accounts_dict[SUPPLY](0.00)


class TAcntPrepaidExpenses(TAcntAsset):
    def __init__(self):
        TAcntAsset.__init__(self)
        self._t_account_type["2nd"] = PRE_EXP
        self._begin = accounts_dict[PRE_EXP](0.00)
        self._ending = accounts_dict[PRE_EXP](0.00)


class TAcntLand(TAcntAsset):
    def __init__(self):
        TAcntAsset.__init__(self)
        self._t_account_type["2nd"] = LAND
        self._begin = accounts_dict[LAND](0.00)
        self._ending = accounts_dict[LAND](0.00)


class TAcntBuildings(TAcntAsset):
    def __init__(self):
        TAcntAsset.__init__(self)
        self._t_account_type["2nd"] = BUILD
        self._begin = accounts_dict[BUILD](0.00)
        self._ending = accounts_dict[BUILD](0.00)


class TAcntEquipment(TAcntAsset):
    def __init__(self):
        TAcntAsset.__init__(self)
        self._t_account_type["2nd"] = EQUIP
        self._begin = accounts_dict[EQUIP](0.00)
        self._ending = accounts_dict[EQUIP](0.00)


class TAcntGoodwill(TAcntAsset):
    def __init__(self):
        TAcntAsset.__init__(self)
        self._t_account_type["2nd"] = GOODWILL
        self._begin = accounts_dict[GOODWILL](0.00)
        self._ending = accounts_dict[GOODWILL](0.00)
# ---------------------T-account for Asset ends----------------------------


# ---------------------T-account for Liability ends------------------------
class TAcntLiability(TAccount):
    def __init__(self):
        TAccount.__init__(self)
        self._t_account_type["main"] = L
        self._begin = accounts_dict[L](0.00)
        self._ending = accounts_dict[L](0.00)


class TAcntAccountsPayable(TAcntLiability):
    def __init__(self):
        TAcntLiability.__init__(self)
        self._t_account_type[SECOND] = AP
        self._begin = accounts_dict[AP](0.00)
        self._ending = accounts_dict[AP](0.00)


class TAcntUnearnedRevenue(TAcntLiability):
    def __init__(self):
        TAcntLiability.__init__(self)
        self._t_account_type[SECOND] = UR
        self._begin = accounts_dict[UR](0.00)
        self._ending = accounts_dict[UR](0.00)


class TAcntOwnersEquity(TAccount):
    def __init__(self):
        TAccount.__init__(self)
        self._t_account_type["main"] = OE
        self._begin = accounts_dict[OE](0.00)
        self._ending = accounts_dict[OE](0.00)


class TAcntRevenue(TAcntOwnersEquity):
    def __init__(self):
        TAcntOwnersEquity.__init__(self)
        self._t_account_type[SECOND] = REV
        self._begin = accounts_dict[REV](0.00)
        self._ending = accounts_dict[REV](0.00)


class TAcntInitialInvestment(TAcntOwnersEquity):
    def __init__(self):
        TAcntOwnersEquity.__init__(self)
        self._t_account_type[SECOND] = INT_INVST
        self._begin = accounts_dict[INT_INVST](0.00)
        self._ending = accounts_dict[INT_INVST](0.00)


class TAcntExpense(TAccount):
    def __init__(self):
        TAccount.__init__(self)
        self._t_account_type["main"] = E
        self._begin = accounts_dict[E](0.00)
        self._ending = accounts_dict[E](0.00)


class TAcntCostOfGoodsSold(TAcntExpense):
    def __init__(self):
        TAcntExpense.__init__(self)
        self._t_account_type[SECOND] = COGS
        self._begin = accounts_dict[COGS](0.00)
        self._ending = accounts_dict[COGS](0.00)


class TAcntSalariesExpense(TAcntExpense):
    def __init__(self):
        TAcntExpense.__init__(self)
        self._t_account_type[SECOND] = SALA_EXP
        self._begin = accounts_dict[SALA_EXP](0.00)
        self._ending = accounts_dict[SALA_EXP](0.00)


class TAcntWagesExpense(TAcntExpense):
    def __init__(self):
        TAcntExpense.__init__(self)
        self._t_account_type[SECOND] = WAG_EXP
        self._begin = accounts_dict[WAG_EXP](0.00)
        self._ending = accounts_dict[WAG_EXP](0.00)


class TAcntRentExpense(TAcntExpense):
    def __init__(self):
        TAcntExpense.__init__(self)
        self._t_account_type[SECOND] = RENT_EXP
        self._begin = accounts_dict[RENT_EXP](0.00)
        self._ending = accounts_dict[RENT_EXP](0.00)


t_accounts_dict = {A: TAcntAsset, CASH: TAcntCash, AR: TAcntAccountsReceivable, INV: TAcntInventory,
                   MERCHANT_INV: TAcntMerchandiseInventory, SUPPLY: TAcntSupplies, PRE_EXP: TAcntPrepaidExpenses,
                   LAND: TAcntLand, BUILD: TAcntBuildings, EQUIP: TAcntEquipment, GOODWILL: TAcntGoodwill,
                   L: TAcntLiability, AP: TAcntAccountsPayable, OE: TAcntOwnersEquity, REV: TAcntRevenue,
                   INT_INVST: TAcntInitialInvestment, E: TAcntExpense, COGS: TAcntCostOfGoodsSold,
                   SALA_EXP: TAcntSalariesExpense, RENT_EXP: TAcntRentExpense, WAG_EXP: TAcntWagesExpense,
                   UR: TAcntUnearnedRevenue}
t_accounts_2nd_level_dict = {CASH: TAcntCash, AR: TAcntAccountsReceivable, INV: TAcntInventory,
                             SUPPLY: TAcntSupplies, PRE_EXP: TAcntPrepaidExpenses, COGS: TAcntCostOfGoodsSold,
                             LAND: TAcntLand, BUILD: TAcntBuildings, EQUIP: TAcntEquipment, GOODWILL: TAcntGoodwill,
                             AP: TAcntAccountsPayable, REV: TAcntRevenue, INT_INVST: TAcntInitialInvestment,
                             SALA_EXP: TAcntSalariesExpense, RENT_EXP: TAcntRentExpense, WAG_EXP: TAcntWagesExpense,
                             UR: TAcntUnearnedRevenue}

# if __name__ == "__main__":
#     testing
#     A001 = Cash(1000)
#     E001 = Expense(200)
#     L001 = Liability('70')
#     OE001 = OwnersEquity('6.789')
#     A002 = AccountsReceivable(-800)
#     lst = [A001, E001, L001, OE001]
#     for i in lst:
#         print i._amount, i._account_type
#
#     print A001 + E001, A001 + L001, OE001 - A001, A001 + A002
#
#     TA_A001 = TAcntCash()
#     TA_A001.add(A001)
#     print TA_A001.get_balance()


