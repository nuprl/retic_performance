from Scope import Scope

class Global:
    def __init__(self):
        self.global_scope = Scope([]).add_definitions()

    def setter(self,s):
        self.global_scope = s
        # print str(self.global_scope)

    def getter(self):
        #print('ggg')
        return self.global_scope

foo = Global()