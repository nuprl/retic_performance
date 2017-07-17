# Dynamically change method arity => same error in Python and Retic
# Dynamically change method to value => same error in Python and Retic

class A:
  def a(self):
    return 0

  def b(self, x):
    return True

  def reconfigure(self):
    self.a = self.b
    return

def f(obj:A):
  obj.a()
  obj.reconfigure()
  obj.a()
  return

f(A())
