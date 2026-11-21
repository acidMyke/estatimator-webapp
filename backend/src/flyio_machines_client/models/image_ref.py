from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_ref_labels import ImageRefLabels


T = TypeVar("T", bound="ImageRef")


@_attrs_define
class ImageRef:
    """
    Attributes:
        digest (str | Unset): Content digest of the image (`sha256:...`).
        labels (ImageRefLabels | Unset): The image's OCI labels.
        registry (str | Unset): Registry host of the image, such as `registry.fly.io`.
        repository (str | Unset): Repository of the image within the registry, such as `library/nginx`.
        tag (str | Unset): Tag the image was referenced by, if any.
    """

    digest: str | Unset = UNSET
    labels: ImageRefLabels | Unset = UNSET
    registry: str | Unset = UNSET
    repository: str | Unset = UNSET
    tag: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        digest = self.digest

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        registry = self.registry

        repository = self.repository

        tag = self.tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if digest is not UNSET:
            field_dict["digest"] = digest
        if labels is not UNSET:
            field_dict["labels"] = labels
        if registry is not UNSET:
            field_dict["registry"] = registry
        if repository is not UNSET:
            field_dict["repository"] = repository
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.image_ref_labels import ImageRefLabels

        d = dict(src_dict)
        digest = d.pop("digest", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: ImageRefLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = ImageRefLabels.from_dict(_labels)

        registry = d.pop("registry", UNSET)

        repository = d.pop("repository", UNSET)

        tag = d.pop("tag", UNSET)

        image_ref = cls(
            digest=digest,
            labels=labels,
            registry=registry,
            repository=repository,
            tag=tag,
        )

        image_ref.additional_properties = d
        return image_ref

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
