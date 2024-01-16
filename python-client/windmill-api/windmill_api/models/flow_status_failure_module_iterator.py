from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from ..types import UNSET, Unset
from typing import cast, List






T = TypeVar("T", bound="FlowStatusFailureModuleIterator")


@_attrs_define
class FlowStatusFailureModuleIterator:
    """ 
        Attributes:
            index (Union[Unset, int]):
            itered (Union[Unset, List[Any]]):
            args (Union[Unset, Any]):
     """

    index: Union[Unset, int] = UNSET
    itered: Union[Unset, List[Any]] = UNSET
    args: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        index = self.index
        itered: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.itered, Unset):
            itered = self.itered




        args = self.args

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if index is not UNSET:
            field_dict["index"] = index
        if itered is not UNSET:
            field_dict["itered"] = itered
        if args is not UNSET:
            field_dict["args"] = args

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        index = d.pop("index", UNSET)

        itered = cast(List[Any], d.pop("itered", UNSET))


        args = d.pop("args", UNSET)

        flow_status_failure_module_iterator = cls(
            index=index,
            itered=itered,
            args=args,
        )

        flow_status_failure_module_iterator.additional_properties = d
        return flow_status_failure_module_iterator

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties