from __future__ import annotations

import copy
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
from polyeval.target.base.value import BaseTargetValue
from polyeval_extra.target.visualbasic.type import VisualBasicTargetType

import json
import math


class VisualBasicTargetValue(BaseTargetValue):
    def __init__(self):
        self.type = VisualBasicTargetType()

    def by_null(self, vt: Type):
        return "Nothing"

    def by_bool(self, v: bool):
        return "True" if v else "False"

    def by_int(self, v: int):
        return str(v)

    def by_double(self, v: float):
        vs = "{:.7f}".format(v)[:-1]
        if vs == "-0.000000":
            vs = "0.000000"
        return vs

    def by_string(self, v: str):
        res = '"'
        for c in v:
            if c == "\n":
                res += '" & vbLf & "'
            elif c == "\t":
                res += '" & vbTab & "'
            elif c == '"':
                res += '""'
            else:
                res += c
        res += '"'
        return res

    def by_list(self, v: list, vt: Type):
        vs_lst = [self.by(tv) for tv in v]
        vs = ", ".join(vs_lst)
        return f"New List(Of {self.type.by(vt)}) From {{{vs}}}"

    def by_ulist(self, v: list, vt: Type):
        vs_lst = [self.by(tv) for tv in v]
        vs = ", ".join(vs_lst)
        return f"New List(Of {self.type.by(vt)}) From {{{vs}}}"

    def by_idict(self, v: list[tuple], vt: Type):
        vs_lst = [f"{{{self.by(k)}, {self.by(v)}}}" for k, v in v]
        vs = ", ".join(vs_lst)
        return f"New Dictionary(Of Integer, {self.type.by(vt)}) From {{{vs}}}"

    def by_sdict(self, v: list[tuple], vt: Type):
        vs_lst = [f"{{{self.by(k)}, {self.by(v)}}}" for k, v in v]
        vs = ", ".join(vs_lst)
        return f"New Dictionary(Of String, {self.type.by(vt)}) From {{{vs}}}"

    def by_option(self, tv: TypedValue):
        return self.by(tv)
