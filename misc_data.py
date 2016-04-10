from general_ledger import GeneralLedgerBook, GeneralLedgerRecord
from t_account import TAccountCollection
from transaction import temp_dict, extra_dict, handler
from inventory_table import InventoryTable
from constant import *


class Company:
    def __init__(self, name=None, add=None, tel=None):
        self.name = name
        self.address = add
        self.tel = tel

        self.settings = Settings()
        self.book = GeneralLedgerBook(self)
        self.t_accounts = TAccountCollection(self)
        self.inv_table = InventoryTable(self)

    def __str__(self):
        return "Company Name: %r \nCompany Address: %r\nCompany Tel: %r \n" % (self.name, self.address, self.tel)

    def make_entry_n_add2book_n_tacnts(com, lst, extra_lst=None):
        lst = split_input(lst)
        tem_glr = GeneralLedgerRecord()
        for (i, j) in lst:
            temp_dict[i](tem_glr, j, com)
        tem_glr.memo = lst
        if tem_glr.balance_check():
            com.book.add_record(tem_glr)
            if extra_lst:
                com.add_extra([i[0] for i in lst], extra_lst)
        else:
            if handler(tem_glr, com):
                com.book.add_record(tem_glr)
                if extra_lst:
                    com.add_extra([i[0] for i in lst], extra_lst)
            else:
                raise ValueError

    def add_extra(self, lst, extra_lst):
        extra = extra_lst
        for i in lst:
            try:
                extra_dict[i](self, extra)
            except:
                continue
            else:
                break

    def get_income_statement(self, str_or_num):
        sales_revenue = self.t_accounts.content[REV].get_ending_acnt().get_amount()
        cost_of_goods_sold = self.t_accounts.content[COGS].get_ending_acnt().get_amount()
        gross_profit = sales_revenue - cost_of_goods_sold
        operating_expense = sum([self.t_accounts.content[SALA_EXP].get_ending_acnt().get_amount(),
                                 self.t_accounts.content[RENT_EXP].get_ending_acnt().get_amount(),
                                 self.t_accounts.content[WAG_EXP].get_ending_acnt().get_amount()])
        operating_income = gross_profit - operating_expense
        other_income_expense = 0
        net_income = operating_income - other_income_expense
        if str_or_num == 'str':
            return "Income Statement\n%20s:%20s\n%20s:%20s\n%20s:%20s\n%20s:%20s\n%20s:%20s\n%20s:%20s\n%20s:%20s\n" % (
                "sales revenue", sales_revenue, COGS, cost_of_goods_sold, "gross profit", gross_profit, "operating enpense",
                operating_expense, "operating income", operating_income, "other income(expense)", other_income_expense,
                "net income", net_income)
        elif str_or_num == 'num':
            return net_income

    def get_balance_sheet(self, net_income):
        cash_n_cash_equivalents = self.t_accounts.content[CASH].get_ending_acnt().get_amount()
        accounts_receivable = self.t_accounts.content[AR].get_ending_acnt().get_amount()
        pre_paid_expense = self.t_accounts.content[PRE_EXP].get_ending_acnt().get_amount()
        inventory = self.t_accounts.content[INV].get_ending_acnt().get_amount()
        supplies = self.t_accounts.content[SUPPLY].get_ending_acnt().get_amount()
        current_asset = cash_n_cash_equivalents + accounts_receivable + pre_paid_expense + inventory + supplies
        pp_n_e = sum([self.t_accounts.content[LAND].get_ending_acnt().get_amount(),
                      self.t_accounts.content[BUILD].get_ending_acnt().get_amount(),
                      self.t_accounts.content[EQUIP].get_ending_acnt().get_amount()])
        good_will = self.t_accounts.content[GOODWILL].get_ending_acnt().get_amount()
        total_assets = current_asset + pp_n_e + good_will

        accounts_payable = self.t_accounts.content[AP].get_ending_acnt().get_amount()
        unearned_revenue = self.t_accounts.content[UR].get_ending_acnt().get_amount()
        total_liability = accounts_payable + unearned_revenue

        paid_in_capital = self.t_accounts.content[INT_INVST].get_ending_acnt().get_amount()
        retained_earning = net_income
        total_owners_equity = paid_in_capital + retained_earning

        total_l_n_oe = total_liability + total_owners_equity

        return "Balance Sheet\nAssets\n%20s:%20s\n%20s:%20s\n%20s:%20s\n%20s:%20s\n%20s:%20s\n%20s:%20s\n%20s:%20s\n%20s:%20s\n" \
               "%20s:%20s\n\nLiability and Owner's Equity\n%20s:%20s\n%20s:%20s\n%20s:%20s\n\n%20s:%20s\n%20s:%20s\n%20s:%20s\n%20s:%20s\n" % (
                   "cash and equivalents", cash_n_cash_equivalents, AR, accounts_receivable, PRE_EXP, pre_paid_expense,
                   INV, inventory, SUPPLY, supplies, "current assets", current_asset, "PP&E", pp_n_e, GOODWILL,
                   good_will, "total assets", total_assets, AP, accounts_payable, UR, unearned_revenue,
                   "total  liability", total_liability, "paid in capital", paid_in_capital,
                   "retained earnings", retained_earning, "total owner's equity", total_owners_equity,
                   "total liability and oe", total_l_n_oe)


def split_input(str_input):
    temp_lst = [i.lstrip() for i in str_input.split(',')]
    str_lst = []
    num_lst = []
    for i in temp_lst:
        if i.isdigit():
            num_lst.extend([i])
        else:
            str_lst.extend([i])
    temp_lst = []
    if len(num_lst) == 1:
        for i in str_lst:
            temp_lst.extend([(i, num_lst[0])])
    else:
        for i, j in zip(str_lst, num_lst):
            temp_lst.extend([(i, j)])
    return temp_lst


def split_extra_input(str_input):
    return [i.lstrip() for i in str_input.split(',')]


class CustomerTable:
    def __init__(self):
        self._content = []


class CustomerTableItem:
    def __init__(self):
        self._name = "none"
        self._address = "none"
        self._tel = "none"
        self._approval_status = False
        self._id = "none"


class Settings:
    def __init__(self):
        self._inventory_mtd = None

    def set_inv_mtd(self, mtd):
        if self._inventory_mtd is None:
            if mtd == "FIFO" or mtd == "LIFO" or mtd == "WA" or mtd == "SPECIFIC":
                self._inventory_mtd = mtd
        elif mtd == "Authorised Change":
            pass
        else:
            raise TypeError

    def get_inv_mth(self):
        return self._inventory_mtd


key_words = ["purchase", "account", "suppl", 'provide', 'service', 'receive', "advance", "investment",
             "payment", "equipment", "credit", "merchandise", 'wage', "rent", 'paid', "buy", 'cash', 'pay', "on", "in"]
key_words_dict = {"purchase": "purchase", "account": "account", "on": "on", "office": "office", "suppl": "supply",
                  'provide': 'provide', 'service': 'service', "equipment": "equipment", "buy": "purchase",
                  'receive': 'receive', 'cash': 'cash', 'pay': 'pay', 'paid': 'pay', 'wage': 'wage',
                  "credit": "account",
                  "advance": "advance", "rent": "rent", "in": "in", "investment": "investment", "payment": "payment",
                  "merchandise": "merchandise"}
key_phrase = ['purchase supply', "purchase equipment", "receive investment", 'provide service',
              "receive advance payment", "purchase merchandise",
              'pay wage', 'pay cash', 'on account', "pay advance rent", "pay rent", "in cash", "receive cash"]
