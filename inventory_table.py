from data_structure import InvLIFO, InvFIFO, InvWA


class InventoryTable:
    def __init__(self, owner):
        self._content = {}
        self.owner = owner

    def add_inventory(self, inv_list):
        if isinstance(inv_list, InventoryTableList):
            self._content[inv_list.id] = inv_list
        else:
            raise TypeError

    def __str__(self):
        to_return = ''
        for i in self._content:
            to_return += "%s:\n%s" % (i, str(self._content[i]))
        return to_return

    def __getitem__(self, item):
        return self._content[item]


class InventoryTableList:
    def __init__(self, company, id_n):
        self._name = None
        self.id = id_n
        if company.settings.get_inv_mth() == "LIFO":
            self._content = InvLIFO()
        elif company.settings.get_inv_mth() == "FIFO":
            self._content = InvFIFO()
        elif company.settings.get_inv_mth() == "WA":
            self._content = InvWA()

    def stock_in(self, unit_p, q):
        temp_inv_item = InventoryTableListItem(unit_p, q)
        self._content.add(temp_inv_item)

    def stock_out(self, qtity):
        try:
            q = round(float(qtity), 2)
            amount2return = self._content.sub(q)
        except ValueError:
            raise ValueError
        return amount2return

    def __str__(self):
        return str(self._content)


class InventoryTableListItem:
    def __init__(self, u_p, q):
        try:
            self.unit_price = round(float(u_p), 2)
            self.quantity = round(float(q), 2)
        except ValueError:
            raise ValueError
        self._date = None

# if __name__ == "__main__":
#     ''' Testing '''
#     tem_com = Company('CRF corp', 'room 640', '13456789')
#     tem_com.settings.set_inv_mtd("LIFO")
#     inv_lst = InventoryTableList(tem_com, "inv 002")
#     inv_lst.stock_in(5.5, 200)
#     inv_lst.stock_in(6, 300)
#     inv_lst.stock_out(100)
#     inv_lst.stock_in(2, 100)
#     tem_com.inv_table.add_inventory(inv_lst)
#     print tem_com.inv_table
