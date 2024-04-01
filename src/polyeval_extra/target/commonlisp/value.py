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
from polyeval_extra.target.commonlisp.type import CommonLispTargetType

import json
import math


class CommonLispTargetValue(BaseTargetValue):
    def __init__(self):
        self.type = CommonLispTargetType()

    def by_null(self, vt: Type):
        return "nil"

    def by_bool(self, v: bool):
        return "t" if v else "nil"

    def by_int(self, v: int):
        return str(v)

    def by_double(self, v: float):
        vs = "{:.7f}".format(v)[:-1]
        if vs == "-0.000000":
            vs = "0.000000"
        return f"{vs}d0"

    def by_string(self, v: str):
        return '"' + v.replace("\\", "\\\\").replace('"', '\\"') + '"'

    def by_list(self, v: list, vt: Type):
        vs_lst = [self.by(tv) for tv in v]
        vs = " ".join(vs_lst)
        return f"(list {vs})"

    def by_ulist(self, v: list, vt: Type):
        vs_lst = [self.by(tv) for tv in v]
        vs = " ".join(vs_lst)
        return f"(list {vs})"

    def by_idict(self, v: list[tuple], vt: Type):
        vs_lst = [f"(cons {self.by(k)} {self.by(v)})" for k, v in v]
        vs = " ".join(vs_lst)
        return f"(p_e_create-dict (list {vs}))"

    def by_sdict(self, v: list[tuple], vt: Type):
        vs_lst = [f"(cons {self.by(k)} {self.by(v)})" for k, v in v]
        vs = " ".join(vs_lst)
        return f"(p_e_create-dict (list {vs}))"

    def by_option(self, tv: TypedValue):
        return self.by(tv)
