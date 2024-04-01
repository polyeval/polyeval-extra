from __future__ import annotations

from polyeval.target.utils import Naming, get_naming_function
from polyeval.target.base.naming import BaseTargetNaming


class VisualBasicTargetNaming(BaseTargetNaming):
    def __init__(self):
        self.func_naming = Naming.PASCAL_CASE
        self.var_naming = Naming.CAMEL_CASE
        pass
