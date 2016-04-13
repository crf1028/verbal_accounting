from accounts import *
from datetime import datetime


class GeneralLedgerBook:        # TODO maybe validate before added to book
    def __init__(self, owner=None):
        self._open_date = datetime.now().strftime('%Y-%m-%d %H:%M')
        self._close_date = None
        self._owner = owner
        self._content = {}

    def __str__(self):
        to_return = '\n'
        for item in self._content.values():
            for j in item:
                to_return += str(j)
        return "\nDate Opened: %s \nDate Closed: %s\nOwner: %s\n" % (self._open_date, self._close_date, self._owner.name) + to_return

    def add_record(self, glr):
        if isinstance(glr, GeneralLedgerRecord):
            today = datetime.now().strftime('%Y-%m-%d')
            try:
                self._content[today].extend([glr])
            except:
                self._content[today] = [glr]

    # def get_content(self):
    #     for item in self._content.values():
    #         for j in item:
    #             print j


class GeneralLedgerRecord:
    def __init__(self):
        self._date = datetime.now().strftime('%Y-%m-%d %H:%M')
        self._dr_side = []
        self._cr_side = []
        self.memo = None
        self._balanced = False               # check if gl is balanced # TODO accounting equation balance
        self.customer = None
        # self._sold_by = "none"

    def __nonzero__(self):
        return bool(self._dr_side) and bool(self._cr_side)

    def balance_check(self):            # maybe can be simplified
        if not self._cr_side or not self._dr_side:
            self._balanced = False
            return False
        elif not reduce(lambda x, y: x + y, self._dr_side + self._cr_side):
            self._balanced = True
            return True
        else:
            self._balanced = False
            return False

    def add_dr_cr_content(self, temp_acnt):
        if temp_acnt.check_ledger_side() is "dr":
            self._dr_side.extend([temp_acnt])
        elif temp_acnt.check_ledger_side() is "cr":
            self._cr_side.extend([temp_acnt])
        else:
            raise ValueError

    def __str__(self):
        if self._cr_side or self._dr_side:
            to_return = ''
            for i in self._dr_side + self._cr_side:
                to_return += str(i)
            to_return += '\n'
            return to_return
        else:
            return "nothing in entry"

    def get_accounts_type(self):
        to_return = []
        for item in self._dr_side + self._cr_side:
            to_return.extend([item.get_account_type()[1]])
        return to_return

    def get_content(self):
        return self._dr_side + self._cr_side


if __name__ == "__main__":
    pass