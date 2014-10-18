class CashDesk:
    def __init__(self):
        self.money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    def take_money(self, income_money):
        for coins in income_money:
            self.money[coins] += income_money[coins]

    def total(self):
        total_money = 0
        for coins in self.money:
            total_money += coins * self.money[coins]
        return total_money

    def can_withdraw_money(self, amount_of_money):
        # current_available = 0
        # banknotes = reversed(sorted(self.money.keys()))
        # for banknote in banknotes:
        #     if current_available == amount_of_money:
        #         return True
        #     if current_available != amount_of_money:
        #         banknote_count = self.money[banknote]
        #         if banknote_count > 0:
        #             current_available += self.money[banknote] * banknote
        # return False
        remainder = amount_of_money
        for coins in reversed(sorted(self.money.keys())):
            if remainder == 0:
                return True
            if coins <= remainder:
                amount_count = self.money[coins]                
                amount_availabe = amount_count * coins
                if amount_availabe <= remainder:
                    remainder -= amount_availabe
                    self.money[coins] -= amount_count
        self.money = self.money
        return False


my_cash_desk = CashDesk()
my_cash_desk.take_money({1: 2, 50: 1, 20: 1})
# print (my_cash_desk.total())
print (my_cash_desk.can_withdraw_money(30))
print (my_cash_desk.can_withdraw_money(70))
print(my_cash_desk.money)