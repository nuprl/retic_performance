@fields({"a": List(A)})
class A:
  def __init__(self:A)->Void:
    self.a = []

  def geta(self:A)->A:
    return self.a[0]

