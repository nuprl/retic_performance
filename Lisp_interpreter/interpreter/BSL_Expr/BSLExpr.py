from abc import abstractmethod
import DirPaths
from BSLError import BSLError

class BSLExpr:

    def eval(ast, s):
        try:
            return [ast.eval_internal(s),s] #X IS A VALUE
        except BSLError:
            print("Interpreter Error")
            return [None, s]

    @abstractmethod
    def eval_internal(self, defs):
        """
        Evaluates this expression
        :param defs: Scope
        :return: Value of this expresson
        """
        raise NotImplementedError('Method not yet implemented')



