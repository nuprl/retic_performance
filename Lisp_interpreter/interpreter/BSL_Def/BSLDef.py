import DirPaths
from BSLError import BSLError
from Closure import Closure
from abc import abstractmethod

class BSLDef:
    """
    To represent a BSL Defintion
    """

    def __init__(self, name, params):
        """
        :param name: String
        :param params: [String]
        """
        if len(params) != len(set(params)):
            raise BSLError\
                ('Duplicate Params are not allowed in Function definitions')
        self.params = params
        self.name = name

    def eval(self, s):
        """
        evaluates this expression by updating the current scope to new_scope
        :param s: current scope
        :return: [None, new_scope]
        """
        return [None,self.update(s)]

    @abstractmethod
    def update(self, s):
        """
        Updates the current scope with the new definition
        :param s: Current scope
        :return: New scope
        """
        raise NotImplementedError('Method not yet implemented')