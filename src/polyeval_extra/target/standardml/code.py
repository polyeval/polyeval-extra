from __future__ import annotations

from polyeval.object.function import Function
from polyeval.object.type import StringType
from polyeval.target.base.code import BaseTargetCode
from polyeval_extra.target.standardml.naming import StandardMLTargetNaming
from polyeval_extra.target.standardml.type import StandardMLTargetType
from polyeval_extra.target.standardml.value_stringify import StandardMLTargetValueStringify


class StandardMLTargetCode(BaseTargetCode):
    def __init__(self):
        self.naming = StandardMLTargetNaming()
        self.type = StandardMLTargetType()
        self.stringify = StandardMLTargetValueStringify()
        pass

    def gen_signature(self, func: Function):
        name = self.naming.get_func_name(func.name)
        args = [
            f"({self.naming.get_var_name(arg.name)}: {self.type.by(arg.type)})"
            for arg in func.parameters
        ]
        args_str = " ".join(args)
        return_type = self.type.by(func.return_type)
        return f"""\
fun {name} {args_str} : {return_type} =
    (* ... *)

"""

    def gen_self_contain_code(
        self, func_name, arg_name, arg_type_str, return_type_str, ret_value_str
    ):
        return f"""\
fun {func_name} ({arg_name}: {arg_type_str}) : {return_type_str} =
    {ret_value_str};

"""
