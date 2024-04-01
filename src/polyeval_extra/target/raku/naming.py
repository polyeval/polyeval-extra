from __future__ import annotations

from polyeval.target.utils import Naming, get_naming_function
from polyeval.target.base.naming import BaseTargetNaming


class RakuTargetNaming(BaseTargetNaming):
    def __init__(self):
        self.func_naming = Naming.KEBAB_CASE
        self.var_naming = Naming.KEBAB_CASE
        pass

    def get_func_name(self, name):
        ret = list(get_naming_function(self.var_naming)(name))
        for i in range(len(ret)):
            if ret[i] == "-" and ret[i + 1] in "0123456789":
                ret[i] = "_"
        return "".join(ret)

    def get_var_name(self, name):
        ret = list(get_naming_function(self.var_naming)(name))
        for i in range(len(ret)):
            if ret[i] == "-" and ret[i + 1] in "0123456789":
                ret[i] = "_"
        return "$" + "".join(ret)
