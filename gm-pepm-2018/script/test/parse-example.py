def untyped_function(x,y):
  return 2

def typed_function(x:int,y:List(Void))->Int:
  return 2

def gradual_function(x:int,y):
  return 2

class without_fields:
  def untyped_method(self,x,y):
    return 2

  def typed_method(self:without_fields,x:int,y:List(Void))->Int:
    return 2

  def gradual_method(self:without_fields,x:int,y):
    return 2



@fields({"f1" : List(List(Int))})
class with_fields:

  def __init__(self:with_fields):
    self.f1 = [[42]]
    self.f2 = 3

  def m(self:with_fields, x:int)->int:
    return x
