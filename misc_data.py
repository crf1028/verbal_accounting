from general_ledger import GeneralLedgerBook, GeneralLedgerRecord
from t_account import TAccountCollection
from transaction import temp_dict, extra_dict, handler
from inventory_table import InventoryTable


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
        extra = split_extra_input(extra_lst)
        for i in lst:
            try:
                extra_dict[i](self, extra)
            except:
                continue
            else:
                break


def split_input(str_input):
    temp_lst = del_space(str_input.split(','))
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
    return del_space(str_input.split(','))


def del_space(lst_2_process):
    for i in range(len(lst_2_process)):
        if lst_2_process[i][0] == " ":
            lst_2_process[i] = lst_2_process[i][1:]
    return lst_2_process


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
