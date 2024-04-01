from __future__ import annotations

from polyeval.object.function import Function
from polyeval.object.type import StringType
from polyeval.target.base.code import BaseTargetCode
from polyeval_extra.target.raku.naming import RakuTargetNaming
from polyeval_extra.target.raku.type import RakuTargetType
from polyeval_extra.target.raku.value_stringify import RakuTargetValueStringify


class RakuTargetCode(BaseTargetCode):
    def __init__(self):
        self.naming = RakuTargetNaming()
        self.type = RakuTargetType()
        self.stringify = RakuTargetValueStringify()
        pass

    def gen_signature(self, func: Function):
        name = self.naming.get_func_name(func.name)
        args = [f"{self.naming.get_var_name(arg.name)}" for arg in func.parameters]
        args_str = ", ".join(args)
        return_type = self.type.by(func.return_type)
        return f"""\
sub {name}({args_str}) returns {return_type} {{
    # ...
}}

"""

    def gen_self_contain_code(
        self, func_name, arg_name, arg_type_str, return_type_str, ret_value_str
    ):
        return f"""\
sub {func_name}({arg_type_str} {arg_name}) returns {return_type_str} {{
    return {ret_value_str};
}}

"""
