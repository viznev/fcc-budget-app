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
  totalSpent = 0
  categorySpent = {}
  finalStr = 'Percentage spent by category'
  for category in categories:
    categorySpent[category.name] = {}
    categorySpent[category.name]['amount'] = round(sum([abs(item['amount']) for item in category.ledger if item['amount'] < 0]), 2)
    totalSpent += categorySpent[category.name]['amount']
  categoryPercent = {k:(v['amount']/totalSpent*10*10) - ((v['amount']/totalSpent*10*10)%10) for k,v in categorySpent.items()}
  for i in range(100, -10, -10):
    finalStr += '\n' + str(i).rjust(3) + '| '
    for category, percent in categoryPercent.items():
      finalStr += 'o  ' if percent >= i else '   '
  finalStr += '\n    -' + '-'*3*len(categoryPercent.keys())
  for x in range(0, max(len(item) for item in categoryPercent)):
    finalStr += '\n     '
    for category in categoryPercent.keys():
      try:
        finalStr += category[x] + '  '
      except:
        finalStr += '   '
  return finalStr