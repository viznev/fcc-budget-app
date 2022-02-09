class Category:
  def __init__(self, name: str):
    self.name = name
    self.ledger = []

  def __str__(self):
    titleLineStars = (30-len(self.name))//2
    strReturn = '*' * titleLineStars + self.name + '*' * titleLineStars
    for item in self.ledger:
      strReturn += '\n' + item['description'][:23].ljust(23) + str(format(item['amount'], '.2f')).rjust(7)
    strReturn += '\n' + 'Total: ' + str(format(self.get_balance(),'.2f'))
    return strReturn

  def deposit(self, amount: float, description: str=''):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount: float, description: str=''):
    if self.check_funds(amount):
      self.ledger.append({"amount": -abs(amount), "description": description})
      return True
    else:
      return False

  def get_balance(self):
    return sum([item['amount'] for item in self.ledger])

  def transfer(self, amount: float, category: object):
    if self.withdraw(amount, "Transfer to "+category.name):
      category.deposit(amount, "Transfer from "+self.name)
      return True
    else:
      return False
    pass

  def check_funds(self, amount: float):
    return not (amount > self.get_balance())

def create_spend_chart(categories):
  return None