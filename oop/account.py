import time


class Account(object):

    account_count = 0

    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        self.account_number = Account.account_count
        self.transaction_history = []
        Account.account_count += 1

    def withdraw(self, money):
        if self.balance < money:
            print("残高がたりません（口座名：{0.name} 口座番号：{0.account_number} 残高：{0.balance}）".format(self))
        else:
            self.balance -= money
            self.show_balance()
            self.add_transaction(-money)

    def deposit(self, money):
        self.balance += money
        self.show_balance()
        self.add_transaction(money)

    def show_balance(self):
        print("口座名：{0.name} 口座番号：{0.account_number} 残高：{0.balance}".format(self))

    def add_transaction(self, money):
        transaction = {
            "withdraw/deposit": money,
            "balance": self.balance,
            "time": Account.now_time()
        }
        self.transaction_history.append(transaction)

    @staticmethod
    def now_time():
        localtime = time.localtime()
        return "{0.tm_year}年{0.tm_mon}月{0.tm_mday}日{0.tm_hour}時{0.tm_min}分".format(localtime)

    def show_transaction_history(self):
        for transaction in self.transaction_history:
            transaction_str_list = []
            for k, v in transaction.items():
                transaction_str_list.append(f"{k}: {v}")
            print(", ".join(transaction_str_list))

account1 = Account(1000, "Kanai Yuko")
account1.withdraw(200)
account1.deposit(1000)
account1.show_transaction_history()