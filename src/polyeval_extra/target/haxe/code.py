from __future__ import annotations

from polyeval.object.function import Function
from polyeval.object.type import StringType
from polyeval.target.base.code import BaseTargetCode
from polyeval_extra.target.haxe.naming import HaxeTargetNaming
from polyeval_extra.target.haxe.type import HaxeTargetType
from polyeval_extra.target.haxe.value_stringify import HaxeTargetValueStringify


class HaxeTargetCode(BaseTargetCode):
    def __init__(self):
        self.naming = HaxeTargetNaming()
        self.type = HaxeTargetType()
        self.stringify = HaxeTargetValueStringify()
        pass

    def gen_signature(self, func: Function):
        name = self.naming.get_func_name(func.name)
        args = [
            f"{self.naming.get_var_name(arg.name)}: {self.type.by(arg.type)}"
            for arg in func.parameters
        ]
        args_str = ", ".join(args)
        return_type = self.type.by(func.return_type)
        return f"""\
static function {name}({args_str}): {return_type} {{
    // ...
}}

"""

    def gen_self_contain_code(
        self, func_name, arg_name, arg_type_str, return_type_str, ret_value_str
    ):
        return f"""\
static function {func_name}({arg_name}: {arg_type_str}): {return_type_str} {{
    return {ret_value_str};
}}

"""
