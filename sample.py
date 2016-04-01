from misc_data import Company


tem_com = Company("Orange Inc.", "Cupertino, CA", "1 (800) 692-7755")
tem_com.settings.set_inv_mtd("WA")

input_in = "receive investment, by cash, 10000"
tem_com.make_entry_n_add2book_n_tacnts(input_in)

input_in = "borrow from bank, receive cash, 20000"
tem_com.make_entry_n_add2book_n_tacnts(input_in)

input_in = "purchase equipment, paid in cash, 12000"
tem_com.make_entry_n_add2book_n_tacnts(input_in)

input_in = "purchase merchandise, on credit, 6000"
input_extra = 'Inv001, 10, 600'
tem_com.make_entry_n_add2book_n_tacnts(input_in, input_extra)

input_in = "sell merchandise, 11000, receive cash, 9000"
input_extra = 'Inv001, 500'
tem_com.make_entry_n_add2book_n_tacnts(input_in, input_extra)

input_in = "pay salaries, paid in cash, 3500"
tem_com.make_entry_n_add2book_n_tacnts(input_in)

input_in = "pay rent, paid in cash, 1500"
tem_com.make_entry_n_add2book_n_tacnts(input_in)


tem_com.book.get_contant()
tem_com.t_accounts.get_content()
print tem_com.inv_table

