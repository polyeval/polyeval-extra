from __future__ import annotations
from polyeval.target.base.type import BaseTargetType
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


class VisualBasicTargetType(BaseTargetType):
    def __init__(self):
        pass

    def by_bool(self, t: BoolType):
        return "Boolean"

    def by_int(self, t: IntType):
        return "Integer"

    def by_double(self, t: DoubleType):
        return "Double"

    def by_string(self, t: StringType):
        return "String"

    def by_list(self, t: ListType):
        return f"List(Of {self.by(t.value_type)})"

    def by_ulist(self, t: UListType):
        return f"List(Of {self.by(t.value_type)})"

    def by_idict(self, t: IdictType):
        return f"Dictionary(Of Integer, {self.by(t.value_type)})"

    def by_sdict(self, t: SdictType):
        return f"Dictionary(Of String, {self.by(t.value_type)})"

    def by_option(self, t: OptionType):
        return f"{self.by(t.value_type)}?"
