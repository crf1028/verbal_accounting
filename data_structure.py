from collections import deque


class InvLIFO:
    def __init__(self):
        self._content = []

    def add(self, inv_item):
        self._content.extend([inv_item])

    def sub(self, qtity):       # TODO when qtity is greater than total inv in stock
        amt2return = 0
        while qtity > 0:
            qtity_copy = qtity
            qtity -= self._content[-1].quantity
            if qtity <= 0:
                amt2return += qtity_copy*self._content[-1].unit_price
                self._content[-1].quantity -= qtity_copy
            else:
                amt2return += self._content[-1].quantity*self._content[-1].unit_price
                self._content.pop()
        return amt2return

    def __str__(self):
        to_return = ''
        for i in self._content:
            to_return += "unit price: %r, quantity: %d\n" % (i.unit_price, i.quantity)
        return to_return


class InvFIFO:
    def __init__(self):
        self._content = deque([])

    def add(self, inv_item):
        self._content.extend([inv_item])

    def sub(self, qtity):
        amt2return = 0
        while qtity > 0:
            qtity_copy = qtity
            qtity -= self._content[0].quantity
            if qtity <= 0:
                amt2return += qtity_copy * self._content[0].unit_price
                self._content[0].quantity -= qtity_copy
            else:
                amt2return += self._content[0].quantity * self._content[-1].unit_price
                self._content.popleft()
        return amt2return

    def __str__(self):
        to_return = ''
        for i in self._content:
            to_return += "unit price: %r, quantity: %d\n" % (i.unit_price, i.quantity)
        return to_return


class InvWA:
    def __init__(self):
        self._content = deque([])
        self.wa_u_p = 0
        self.wa_q = 0

    def add(self, inv_item):
        self._content.extend([inv_item])
        temp_total = self.wa_q * self.wa_u_p
        temp_total += inv_item.quantity * inv_item.unit_price
        self.wa_q += inv_item.quantity
        self.wa_u_p = temp_total / self.wa_q
        for i in self._content:
            i.unit_price = self.wa_u_p

    def sub(self, qtity):
        self.wa_q -= qtity
        amt2return = qtity * self.wa_u_p
        while qtity > 0:
            qtity_copy = qtity
            qtity -= self._content[0].quantity
            if qtity <= 0:
                self._content[0].quantity -= qtity_copy
            else:
                self._content.popleft()
        return amt2return

    def __str__(self):
        to_return = ''
        to_return += "weight average unit price: %r, total quantity: %d\n" % (self.wa_u_p, self.wa_q)
        for i in self._content:
            to_return += "unit price: %r, quantity: %d\n" % (i.unit_price, i.quantity)
        return to_return
