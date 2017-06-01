@fields({"dollars": Int, "cents": Int})
class Cash:
  dollars = 0
  cents = 0

  def add_dollars(self, dollars):
    self.dollars += dollars

def get_cash()->Cash:
  c = Cash()
  c.add_dollars(3.14159)
  return c

get_cash()
