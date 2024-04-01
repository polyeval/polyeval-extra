from __future__ import annotations

from polyeval.object.function import Function
from polyeval.target.base.code import BaseTargetCode
from polyeval_extra.target.emacslisp.naming import EmacsLispTargetNaming
from polyeval_extra.target.emacslisp.type import EmacsLispTargetType
from polyeval_extra.target.emacslisp.value_stringify import EmacsLispTargetValueStringify


class EmacsLispTargetCode(BaseTargetCode):
    def __init__(self):
        self.naming = EmacsLispTargetNaming()
        self.type = EmacsLispTargetType()
        self.stringify = EmacsLispTargetValueStringify()
        pass

    def gen_signature(self, func: Function):
        name = self.naming.get_func_name(func.name)
        args = [f"{self.naming.get_var_name(arg.name)}" for arg in func.parameters]
        args_str = " ".join(args)
        return_type = self.type.by(func.return_type)
        return f"""\
(defun {name} ({args_str})
    ;; ...
)

"""

    def gen_self_contain_code(
        self, func_name, arg_name, arg_type_str, return_type_str, ret_value_str
    ):
        return f"""\
(defun {func_name} ({arg_name})
    {ret_value_str})

"""
