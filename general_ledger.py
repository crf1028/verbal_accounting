from accounts import *
from datetime import datetime


class GeneralLedgerBook:        # TODO maybe validate before added to book
    def __init__(self, owner=None):
        self._open_date = datetime.now().strftime('%Y-%m-%d %H:%M')
        self._close_date = None
        self._owner = owner
        self._content = {}

    def __str__(self):
        return "Date Opened: %r \nDate Closed: %r\nOwner: %r \n" % (self._open_date, self._close_date, self._owner.name)

    def add_record(self, glr):
        if isinstance(glr, GeneralLedgerRecord):
            today = datetime.now().strftime('%Y-%m-%d')
            try:
                self._content[today].extend([glr])
            except:
                self._content[today] = [glr]

    def get_content(self):
        for item in self._content.values():
            for j in item:
                print j

    def django_value(self):
        to_return = ''
        for item in self._content.values():
            for j in item:
                to_return += str(j)
                to_return += '\n'
        return to_return


class GeneralLedgerRecord:
    def __init__(self):
        self._date = datetime.now().strftime('%Y-%m-%d %H:%M')
        self._dr_side = []
        self._cr_side = []
        self.memo = None
        self._balanced = False               # check if gl is balanced # TODO accounting equation balance
        self.customer = None
        # self._sold_by = "none"

    def balance_check(self):            # maybe can be simplified
        if not self._cr_side or not self._dr_side:
            self._balanced = False
            return False
        elif reduce(lambda x, y: x + y, self._dr_side + self._cr_side).get_amount() == 0:
            self._balanced = True
            return True
        else:
            self._balanced = False
            return False

    def check_side_acnt_type(self, dr_or_cr):       # check the main account type of either side
        if dr_or_cr == "dr":            # parameter should be "dr" or "cr"
            to_check = self._dr_side
        elif dr_or_cr == "cr":
            to_check = self._cr_side
        else:
            raise ValueError
        if not to_check:
            raise KeyError
        else:
            answer = []
            for item in to_check:
                answer.extend([item.get_account_type(MAIN)])
            return answer

    def add_dr_cr_content(self, temp_acnt):
        if temp_acnt.check_ledger_side() is "dr":
            self._dr_side.extend([temp_acnt])
        elif temp_acnt.check_ledger_side() is "cr":
            self._cr_side.extend([temp_acnt])
        else:
            raise ValueError

    def __str__(self):
        if self._cr_side and self._dr_side:
            to_return_exp = ""
            to_return_data = ()
            for item in self._dr_side:
                to_return_exp += 'Dr.%20s%15s\n'
                to_return_data += (item.get_account_type(SECOND)['2nd'], abs(item.get_amount()),)
            for j in self._cr_side:
                to_return_exp += 'Cr.%25s%15s\n'
                to_return_data += (j.get_account_type(SECOND)['2nd'], abs(j.get_amount()),)
            return to_return_exp % to_return_data
        else:
            return "nothing in entry"

    def get_accounts_type(self, para):
        to_return = []
        for item in self._dr_side + self._cr_side:
            to_return.extend([item.get_account_type(para)[para]])
        return to_return

    def get_content(self):
        return self._dr_side + self._cr_side