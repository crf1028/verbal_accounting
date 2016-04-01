from datetime import datetime
from general_ledger import GeneralLedgerRecord, GeneralLedgerBook
from accounts import accounts_dict
from constant import *
from inventory_table import InventoryTableList


def trans_merchant_inv_increase(glr_instance, num, com):
    num = abs(round(float(num), 2))
    general_trans(glr_instance, num, com, MERCHANT_INV)


def trans_merchant_inv_decrease(glr_instance, num, com):
    num = -abs(round(float(num), 2))
    general_trans(glr_instance, num, com, MERCHANT_INV)


def trans_cash_decrease(glr_instance, num, com):
    num = -abs(round(float(num), 2))
    general_trans(glr_instance, num, com, CASH)


def trans_cash_increase(glr_instance, num, com):
    num = abs(round(float(num), 2))
    general_trans(glr_instance, num, com, CASH)


def trans_cash_neutral(glr_instance, num, com):
    num = round(float(num), 2)
    general_trans(glr_instance, num, com, CASH)


def trans_revenue_increase(glr_instance, num, com):
    num = abs(round(float(num), 2))
    general_trans(glr_instance, num, com, REV)


def trans_cogs_increase(glr_instance, num, com):
    num = abs(round(float(num), 2))
    general_trans(glr_instance, num, com, COGS)


def trans_initial_invest_increase(glr_instance, num, com):
    num = abs(round(float(num), 2))
    general_trans(glr_instance, num, com, INT_INVST)


def trans_equipment_increase(glr_instance, num, com):
    num = abs(round(float(num), 2))
    general_trans(glr_instance, num, com, EQUIP)


def trans_accounts_payable_increase(glr_instance, num, com):
    num = abs(round(float(num), 2))
    general_trans(glr_instance, num, com, AP)


def trans_accounts_payable_neutral(glr_instance, num, com):
    num = round(float(num), 2)
    general_trans(glr_instance, num, com, AP)


def trans_salary_exp_increase(glr_instance, num, com):
    num = abs(round(float(num), 2))
    general_trans(glr_instance, num, com, SALA_EXP)


def trans_rent_exp_increase(glr_instance, num, com):
    num = abs(round(float(num), 2))
    general_trans(glr_instance, num, com, RENT_EXP)


def general_trans(glr_instance, num, com, account_code):
    temp_acnt = accounts_dict[account_code](num)
    glr_instance.add_dr_cr_content(temp_acnt)
    acnt_code_lst = temp_acnt.get_account_type().values()
    for i in acnt_code_lst:
        if i is not None:
            com.t_accounts.content[i].add(temp_acnt)


def extra_add_inventory(com, lst):
    [id_n, unit_p, q] = lst
    try:
        com.inv_table[id_n]
    except:
        com.inv_table.add_inventory(InventoryTableList(com, id_n))
    com.inv_table[id_n].stock_in(unit_p, q)


def extra_sell_inventory(com, lst):
    [id_n, q] = lst
    num = com.inv_table[id_n].stock_out(q)
    tem_glr = GeneralLedgerRecord()
    trans_cogs_increase(tem_glr, num, com)
    trans_merchant_inv_decrease(tem_glr, num, com)
    if tem_glr.balance_check():
        com.book.add_record(tem_glr)


temp_dict = {"by cash": trans_cash_neutral, "receive cash": trans_cash_increase, AP: trans_accounts_payable_neutral,
             "receive investment": trans_initial_invest_increase, CASH: trans_cash_neutral,
             "borrow from bank": trans_accounts_payable_increase, "purchase equipment": trans_equipment_increase,
             "paid in cash": trans_cash_decrease, "purchase merchandise": trans_merchant_inv_increase,
             "on credit": trans_accounts_payable_increase, "sell merchandise": trans_revenue_increase,
             "pay salaries": trans_salary_exp_increase, "pay rent": trans_rent_exp_increase}
extra_dict = {"purchase merchandise": extra_add_inventory, "sell merchandise": extra_sell_inventory}


def handler(glr, com):
    acnts_type_lst = glr.get_accounts_type(SECOND)
    acnts_lst = glr.get_content()
    missing_acnt_type = None
    for item in handler_dict.values():
        counts = 0
        for j in acnts_type_lst:
            if j in item:
                counts += 1
            else:
                break
        if counts == len(item)-1:
            missing_acnt_type = list(set(item)-set(acnts_type_lst))[0]
    if missing_acnt_type is not None:
        missing_acnt = accounts_dict[missing_acnt_type](0)
        for item in acnts_lst:
            missing_acnt -= item
        glr.add_dr_cr_content(missing_acnt)
        acnt_code_lst = missing_acnt.get_account_type().values()
        for i in acnt_code_lst:
            if i is not None:
                com.t_accounts.content[i].add(missing_acnt)
        return True
    else:
        return False


handler_dict = {REV: [REV, CASH, AR]}



# def check_pos_neg(num, pos_or_neg):
#     if num > 0 and pos_or_neg == POS:
#         return True
#     elif num < 0 and pos_or_neg == NEG:
#         return True
#     else:
#         raise ValueError


def init_transaction_id():
    return datetime.now().strftime('%Y%m%d%H%M')


if __name__ == "__main__":
    ''' Testing '''
# temp_glr = GeneralLedgerRecord()
# PurMerchantInv(temp_glr, 5000)
# WithCash(temp_glr, -5000)
# print temp_glr.get_content()["dr"][0].get_amount(), temp_glr.get_content()["cr"][0].get_amount()
# print temp_glr.balance_check()
# print temp_glr, temp_glr.get_content()
# print handler([REV, AR])