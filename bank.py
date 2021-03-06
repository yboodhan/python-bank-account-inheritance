class BankAccount:
  def __init__(self):
    self.balance = 0

  def deposit(self, amount = 0):
    if amount < 0:
      return False
    self.balance = self.balance + amount
    return self.balance

  def withdraw(self, amount = 0):
    if amount < 0:
      return False
    self.balance = self.balance - amount
    return self.balance

  def accumulate_interest(self):
    self.balance = self.balance + (self.balance * 0.02)
    return self.balance


class ChildrensAccount(BankAccount):
  def __init__(self):
    super(ChildrensAccount, self).__init__()

  def accumulate_interest(self):
    self.balance = self.balance + 10
    return self.balance

class OverdraftAccount(BankAccount):
  def __init__(self, overdraft_penalty = 40):
    self.overdraft_penalty = overdraft_penalty
    super(OverdraftAccount, self).__init__()

  def withdraw(self, amount = 0):
    if self.balance - amount < 0:
      self.balance = self.balance - self.overdraft_penalty
      return False
    self.balance = self.balance + amount
    return self.balance
  

basic_account = BankAccount()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
print()

childs_account = ChildrensAccount()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
print()

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))
