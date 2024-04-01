from __future__ import annotations

import copy
from polyeval.misc.utils import add_indent
from polyeval.object.function import Function, Parameter, Testcase
from polyeval.object.type import (
    Type,
    IntType,
    DoubleType,
    BoolType,
    StringType,
    ListType,
    UListType,
    IdictType,
    SdictType,
    OptionType,
)
from polyeval.object.typed_value import TypedValue
from polyeval.target.base.tests import BaseTargetTests
from polyeval_extra.target.visualbasic.type import VisualBasicTargetType
from polyeval_extra.target.visualbasic.value import VisualBasicTargetValue
from polyeval_extra.target.visualbasic.naming import VisualBasicTargetNaming
from polyeval_extra.target.visualbasic.value_stringify import VisualBasicTargetValueStringify

import json


class VisualBasicTargetTests(BaseTargetTests):
    def __init__(self):
        self.naming = VisualBasicTargetNaming()
        self.type = VisualBasicTargetType()
        self.value = VisualBasicTargetValue()
        self.stringify = VisualBasicTargetValueStringify()
        pass

    def gen_code(self, funcs: list[Function]):
        result = ""
        test_entry_ret = ""
        tests = self.gen_all_tests(funcs)
        for func_signature, func_tests in tests:
            test_entry_ret += f'vbLf & "{func_signature}" & vbLf & '
            for test_item_name, test_item_code in func_tests:
                test_entry_ret += f"{test_item_name}() & "
                result += test_item_code
        test_entry_ret += "vbLf"
        test_entry = f"""\
Function p_e_entry() As String
    Return {test_entry_ret}
End Function

"""
        return result + test_entry

    def gen_function_test(
        self,
        func_name: str,
        idx: int,
        func_params: list[Parameter],
        func_ret_type: Type,
        func_test: Testcase,
    ):
        test_item_func_name = func_name + f"_test_{idx}"
        test_item_func_name = "p_e_" + self.naming.get_func_name(test_item_func_name)
        test_inputs = func_test.inputs
        test_expected = func_test.output
        input_types = [tv.type for tv in test_inputs]
        target_func_name = self.naming.get_func_name(func_name)
        params_names = [
            self.naming.get_var_name(f"var_{idx}") for idx in range(len(func_params))
        ]

        test_code = f"""\
Function {test_item_func_name}() As String
    {add_indent(self.gen_assign_vars_cmds(params_names, test_inputs), 1)}
    {self.gen_input_str_cmd(params_names, input_types)}
    {self.gen_expected_str_cmd(test_expected)}    
    {self.gen_output_cmd(target_func_name, params_names)}
    {self.gen_output_str_cmd(func_ret_type)}
    {self.gen_side_str_cmd(params_names, input_types)}
    Return "-" & vbLf & iStr & oStr & eStr & sStr
End Function

"""
        return (test_item_func_name, test_code)

    def gen_assign_vars_cmds(
        self, params_names: list[str], test_inputs: list[TypedValue]
    ):
        result = []
        for name, value in zip(params_names, test_inputs):
            result.append(
                f"Dim {name} As {self.type.by(value.type)} = {self.value.by(value)}"
            )
        return "\n".join(result)

    def gen_input_str_cmd(self, params_names: list[str], input_types: list[Type]):
        val_str = ' & ", " & '.join(
            [self.stringify.get(t, name) for name, t in zip(params_names, input_types)]
        )
        return f'Dim iStr = "input: (" & {val_str} & ")" & vbLf'

    def gen_side_str_cmd(self, params_names: list[str], input_types: list[Type]):
        val_str = ' & ", " & '.join(
            [self.stringify.get(t, name) for name, t in zip(params_names, input_types)]
        )
        return f'Dim sStr = "side-effect: (" & {val_str} & ")" & vbLf'

    def gen_output_cmd(self, func_name: str, params_names: list[str]):
        return f"Dim res = {func_name}({', '.join(params_names)})"

    def gen_output_str_cmd(self, t: Type):
        val_str = self.stringify.get(t, "res")
        return f'Dim oStr = "output: " & {val_str} & vbLf'

    def gen_expected_str_cmd(self, v: TypedValue):
        val_str = self.stringify.get(v.type, self.value.by(v))
        return f'Dim eStr = "expected: " & {val_str} & vbLf'
