from __future__ import annotations

from polyeval.object.function import Function
from polyeval.object.type import StringType
from polyeval.target.base.code import BaseTargetCode
from polyeval_extra.target.reasonml.naming import ReasonMLTargetNaming
from polyeval_extra.target.reasonml.type import ReasonMLTargetType
from polyeval_extra.target.reasonml.value_stringify import ReasonMLTargetValueStringify


class ReasonMLTargetCode(BaseTargetCode):
    def __init__(self):
        self.naming = ReasonMLTargetNaming()
        self.type = ReasonMLTargetType()
        self.stringify = ReasonMLTargetValueStringify()
        pass

    def gen_signature(self, func: Function):
        name = self.naming.get_func_name(func.name)
        args = [
            f"({self.naming.get_var_name(arg.name)}: {self.type.by(arg.type)})"
            for arg in func.parameters
        ]
        args_str = ", ".join(args)
        return_type = self.type.by(func.return_type)
        return f"""\
let {name} = ({args_str}): {return_type} => {{
    // ...
}}

"""

    def gen_self_contain_code(
        self, func_name, arg_name, arg_type_str, return_type_str, ret_value_str
    ):
        return f"""\
let {func_name} = ({arg_name}: {arg_type_str}): {return_type_str} => {{
    {ret_value_str}
}}

"""
