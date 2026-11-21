from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.postgres_query_column import PostgresQueryColumn
    from ..models.postgres_query_response_rows_item_item import (
        PostgresQueryResponseRowsItemItem,
    )


T = TypeVar("T", bound="PostgresQueryResponse")


@_attrs_define
class PostgresQueryResponse:
    """
    Attributes:
        columns (list[PostgresQueryColumn] | Unset): Columns of the final result set, in order.
        row_count (int | Unset): Number of rows returned.
        rows (list[list[PostgresQueryResponseRowsItemItem]] | Unset): Rows of the final result set; each row holds one
            JSON value per column, with NULL as null and json/jsonb as decoded JSON.
    """

    columns: list[PostgresQueryColumn] | Unset = UNSET
    row_count: int | Unset = UNSET
    rows: list[list[PostgresQueryResponseRowsItemItem]] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        columns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.columns, Unset):
            columns = []
            for columns_item_data in self.columns:
                columns_item = columns_item_data.to_dict()
                columns.append(columns_item)

        row_count = self.row_count

        rows: list[list[dict[str, Any]]] | Unset = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = []
                for rows_item_item_data in rows_item_data:
                    rows_item_item = rows_item_item_data.to_dict()
                    rows_item.append(rows_item_item)

                rows.append(rows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if columns is not UNSET:
            field_dict["columns"] = columns
        if row_count is not UNSET:
            field_dict["row_count"] = row_count
        if rows is not UNSET:
            field_dict["rows"] = rows

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.postgres_query_column import PostgresQueryColumn
        from ..models.postgres_query_response_rows_item_item import (
            PostgresQueryResponseRowsItemItem,
        )

        d = dict(src_dict)
        _columns = d.pop("columns", UNSET)
        columns: list[PostgresQueryColumn] | Unset = UNSET
        if _columns is not UNSET:
            columns = []
            for columns_item_data in _columns:
                columns_item = PostgresQueryColumn.from_dict(columns_item_data)

                columns.append(columns_item)

        row_count = d.pop("row_count", UNSET)

        _rows = d.pop("rows", UNSET)
        rows: list[list[PostgresQueryResponseRowsItemItem]] | Unset = UNSET
        if _rows is not UNSET:
            rows = []
            for rows_item_data in _rows:
                rows_item = []
                _rows_item = rows_item_data
                for rows_item_item_data in _rows_item:
                    rows_item_item = PostgresQueryResponseRowsItemItem.from_dict(
                        rows_item_item_data
                    )

                    rows_item.append(rows_item_item)

                rows.append(rows_item)

        postgres_query_response = cls(
            columns=columns,
            row_count=row_count,
            rows=rows,
        )

        postgres_query_response.additional_properties = d
        return postgres_query_response

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
