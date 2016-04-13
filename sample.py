from misc_data import Company, key_words, key_words_dict, key_phrase
import copy
import re
import pickle

tem_com = Company("Orange Inc.", "Cupertino, CA", "1 (800) 692-7755")
tem_com.settings.set_inv_mtd("WA")


def process_input(input_str):
    input_str = input_str.replace('.','')
    str_lst = input_str.split(' ')
    num_lst = []

    extra_lst = []
    temp_unit_p_lst = []
    if re.search(r'(urchase|[S|s]ell|[S|s]old).*merchandise', input_str):
        while True:
            for i in str_lst:
                if re.search(r'Inv\d{3}', i):
                    extra_lst.extend([i])
                    str_lst.remove(i)
                    break
            else:
                break
            for i in str_lst:
                if i.isdigit():
                    extra_lst.extend([int(i)])
                    str_lst.remove(i)
                    break
            if re.search(r'([S|s]ell|[S|s]old).*merchandise', input_str):
                break
            for i in str_lst:
                if i.startswith("$"):
                    temp_unit_p_lst.extend([int(i.replace('$','').replace(',',''))])
            if len(extra_lst) == 1:
                extra_lst.extend([max(temp_unit_p_lst)/min(temp_unit_p_lst)])
            if len(temp_unit_p_lst) == 2:       # TODO check for input accuracy
                str_lst.remove("$"+'{0:,}'.format(min(temp_unit_p_lst)))
                extra_lst[1:1] = [min(temp_unit_p_lst)]
            elif len(temp_unit_p_lst) == 1:
                extra_lst[1:1] = [int(temp_unit_p_lst[0]) / extra_lst[1]]
            break

    for i in range(len(str_lst)):
        j = str_lst[i].replace(',', '')
        if j[0] == "$":
            num_lst.extend([j.replace('$', '')])
            str_lst.pop(i)
            str_lst.insert(i, '')
    key_words_lst2store = []
    remove_empty(str_lst)

    for i in range(len(str_lst)):
        if str_lst[i]:
            for j in key_words:
                if str_lst[i].lower().startswith(j):
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

    # final_result = ''
    # for i in key_phrase_lst2store + num_lst:
    #     final_result += i
    #     final_result += ','
    # if final_result[-1] == ',':
    #     final_result = final_result[:-1]

    final_result = []
    if len(num_lst) == 1:
        for i in key_phrase_lst2store:
            final_result.extend([(i, num_lst[0])])
    else:
        for i, j in zip(key_phrase_lst2store, num_lst):
            final_result.extend([(i, j)])

    if not extra_lst:
        return final_result
    else:
        return final_result, extra_lst


def remove_empty(lst):
    for i in reversed(range(len(lst))):
        if not lst[i]:
            lst.pop(i)


input_lst = ["Company receive investment of $100,000 in cash.",
             "Purchase equipment for $20,000 in cash.",
             "An amount of $36,000 was paid as advance rent for three months.",
             "Purchased office supplies costing $17,600 on account.",
             "Provided services to its customers and received $28,500 in cash.",
             "Paid wages to its employees for first two weeks of January, aggregating $19,100.",
             "Received $4,000 as an advance payment from customers.",
             "Purchased office supplies costing $5,200 on account.",
             "Purchased merchandise Inv001 for $6,000 on account at $10 per unit.",
             "Sold 200 units of merchandise Inv001 for $3,000, receive $2,000 cash."
             ]

for item in input_lst:
    print item
    input_in = process_input(item)
    print input_in
    if type(input_in) is not list:
        tem_com.make_entry_n_add2book_n_tacnts(input_in[0], extra_lst=input_in[1])
    else:
        tem_com.make_entry_n_add2book_n_tacnts(input_in)

print tem_com.book
print tem_com.t_accounts
print tem_com.inv_table
print tem_com.get_income_statement('str')
income = tem_com.get_income_statement('num')
print tem_com.get_balance_sheet(income)

# pickle.dump(tem_com, open("save.p", "wb"))


