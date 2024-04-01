from __future__ import annotations

from polyeval.object.function import Function
from polyeval.object.type import StringType
from polyeval.target.base.code import BaseTargetCode
from polyeval_extra.target.visualbasic.naming import VisualBasicTargetNaming
from polyeval_extra.target.visualbasic.type import VisualBasicTargetType
from polyeval_extra.target.visualbasic.value_stringify import VisualBasicTargetValueStringify


class VisualBasicTargetCode(BaseTargetCode):
    def __init__(self):
        self.naming = VisualBasicTargetNaming()
        self.type = VisualBasicTargetType()
        self.stringify = VisualBasicTargetValueStringify()
        pass

    def gen_signature(self, func: Function):
        name = self.naming.get_func_name(func.name)
        args = [
            f"{self.naming.get_var_name(arg.name)} As {self.type.by(arg.type)}"
            for arg in func.parameters
        ]
        args_str = ", ".join(args)
        return_type = self.type.by(func.return_type)
        return f"""\
Function {name}({args_str}) As {return_type}
    ' ...
End Function

"""

    def gen_self_contain_code(
        self, func_name, arg_name, arg_type_str, return_type_str, ret_value_str
    ):
        return f"""\
Function {func_name}({arg_name} As {arg_type_str}) As {return_type_str}
    Return {ret_value_str}
End Function

"""
