from misc_data import Company, key_words, key_words_dict, key_phrase
from fuzzywuzzy import fuzz
import copy
import pickle

tem_com = Company("Orange Inc.", "Cupertino, CA", "1 (800) 692-7755")
tem_com.settings.set_inv_mtd("WA")

# input_in = "receive investment, receive cash, 10000"
# tem_com.make_entry_n_add2book_n_tacnts(input_in)
#
# input_in = "borrow from bank, receive cash, 20000"
# tem_com.make_entry_n_add2book_n_tacnts(input_in)
#
# input_in = "purchase equipment, paid in cash, 12000"
# tem_com.make_entry_n_add2book_n_tacnts(input_in)
#
# input_in = "purchase merchandise, on credit, 6000"        # on credit is kind neutral
# input_extra = 'Inv001, 10, 600'
# tem_com.make_entry_n_add2book_n_tacnts(input_in, input_extra)
#
# input_in = "sell merchandise, 11000, receive cash, 9000"
# input_extra = 'Inv001, 500'
# tem_com.make_entry_n_add2book_n_tacnts(input_in, input_extra)
#
# input_in = "pay salaries, paid in cash, 3500"
# tem_com.make_entry_n_add2book_n_tacnts(input_in)
#
# input_in = "pay rent, paid in cash, 1500"
# tem_com.make_entry_n_add2book_n_tacnts(input_in)


def process_input(input_str):
    input_str = input_str.replace('.','')
    str_lst = input_str.split(' ')
    num_lst = []

    for i in range(len(str_lst)):
        j = str_lst[i].replace(',', '')
        if j[0] == "$":
            num_lst.extend([j.replace('$', '')])
            str_lst.pop(i)
            str_lst.insert(i, '')
    key_words_lst2store = []
    remove_empty(str_lst)

    for i in range(len(str_lst)):
        for j in key_words:
            if fuzz.ratio(str_lst[i], j) > 70:
                key_words_lst2store.extend([key_words_dict[j]])
                str_lst.pop(i)
                str_lst.insert(i, '')
                break
    remove_empty(str_lst)

    # print key_words_lst2store
    key_phrase_lst2store = []
    while key_words_lst2store:
        for i in key_phrase:
            try:
                if key_words_lst2store[0] in i:
                    # key_phrase_lst2store.extend([i])
                    # for k in reversed(range(len(key_words_lst2store))):
                    #     if key_words_lst2store[k] in i:
                    #         key_words_lst2store.pop(k)
                    # break
                    if set(i.split(' ')) & set(key_words_lst2store) == set(i.split(' ')):
                        key_phrase_lst2store.extend([i])
                        key_words_lst2store = list(set(key_words_lst2store) - set(i.split(' ')))
                        break
                    else:
                        start = copy.deepcopy(key_words_lst2store[1:])
                        end = copy.deepcopy(key_words_lst2store[0])
                        key_words_lst2store = start + [end]
                        # break
            except IndexError:
                break
        else:
            key_words_lst2store.pop(0)

    # extra_lst = []            TODO to be completed
    # if "purchase merchandise" in key_phrase_lst2store:
    #     for i in key_words_lst2store:
    #         if "Inv" in i:
    #             extra_lst.extend([i])
    #             for k in key_words_lst2store:
    #                 j = k.replace(',', '')
    #                 if j.isdigit():
    #                     extra_lst.extend()
    #                     extra_lst.extend([j])

    final_result = ''
    for i in key_phrase_lst2store + num_lst:
        final_result += i
        final_result += ','
    if final_result[-1] == ',':
        final_result = final_result[:-1]

    return final_result


def remove_empty(lst):
    for i in reversed(range(len(lst))):
        if not lst[i]:
            lst.pop(i)


input_lst = ["Company A receive investment of $100,000 in cash.",
             "Purchase equipment for $20,000 in cash.",
             "An amount of $36,000 was paid as advance rent for three months.",
             "Purchased office supplies costing $17,600 on account.",
             "Provided services to its customers and received $28,500 in cash.",
             "Paid wages to its employees for first two weeks of January, aggregating $19,100.",
             "Received $4,000 as an advance payment from customers.",
             "Purchased office supplies costing $5,200 on account."
             ]

for item in input_lst:
    input_in = process_input(item)
    # print input_in
    tem_com.make_entry_n_add2book_n_tacnts(input_in)

print tem_com.book.django_value()
print tem_com.t_accounts.django_value()
print tem_com.inv_table
print tem_com.get_income_statement('str')
income = tem_com.get_income_statement('num')
print tem_com.get_balance_sheet(income)

# pickle.dump(tem_com, open("save.p", "wb"))


