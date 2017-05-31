@fields({"dollars": Int, "cents": Int})
class Cash:
  def __init__(self, d, c):
    self.dollars = d
    self.cents = c

  def __str__(self):
    return "Cash(%s, %s)" % (self.dollars, self.cents)

  def add_dollars(self, dollars):
    self.dollars += dollars

def main()->Cash:
  c = Cash(5, 0)
  c.add_dollars(3.14159)
  return c

print(main())
