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
from polyeval_extra.target.standardml.type import StandardMLTargetType

import json
import math


class StandardMLTargetValue(BaseTargetValue):
    def __init__(self):
        self.type = StandardMLTargetType()

    def by_null(self, vt: Type):
        return "NONE"

    def by_bool(self, v: bool):
        return "true" if v else "false"

    def by_int(self, v: int):
        return str(v).replace("-", "~")

    def by_double(self, v: float):
        vs = "{:.7f}".format(v)[:-1]
        if vs == "-0.000000":
            vs = "0.000000"
        return vs.replace("-", "~")

    def by_string(self, v: str):
        return json.dumps(v)

    def by_list(self, v: list, vt: Type):
        vs_lst = [self.by(tv) for tv in v]
        vs = ", ".join(vs_lst)
        return f"[{vs}]"

    def by_ulist(self, v: list, vt: Type):
        vs_lst = [self.by(tv) for tv in v]
        vs = ", ".join(vs_lst)
        return f"[{vs}]"

    def by_idict(self, v: list[tuple], vt: Type):
        vs_lst = [f"({self.by(k)}, {self.by(v)})" for k, v in v]
        vs = ", ".join(vs_lst)
        return f"(p_e_createIdict [{vs}])"

    def by_sdict(self, v: list[tuple], vt: Type):
        vs_lst = [f"({self.by(k)}, {self.by(v)})" for k, v in v]
        vs = ", ".join(vs_lst)
        return f"(p_e_createSdict [{vs}])"

    def by_option(self, tv: TypedValue):
        return f"(SOME {self.by(tv)})"
