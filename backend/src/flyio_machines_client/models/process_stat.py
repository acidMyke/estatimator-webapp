from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listen_socket import ListenSocket


T = TypeVar("T", bound="ProcessStat")


@_attrs_define
class ProcessStat:
    """
    Attributes:
        command (str | Unset): The process's command line, with arguments separated by spaces.
        cpu (int | Unset): Average CPU usage over the process's lifetime, in percent of one CPU. May exceed 100
            on Machines with more than one CPU.
        directory (str | Unset): The process's working directory.
        listen_sockets (list[ListenSocket] | Unset): TCP sockets the process is listening on.
        pid (int | Unset): Process ID inside the Machine.
        rss (int | Unset): Resident set size: the physical memory the process uses, in bytes.
        rtime (int | Unset): How long the process has been running, in seconds.
        stime (int | Unset): When the process started, in seconds since the Machine booted.
    """

    command: str | Unset = UNSET
    cpu: int | Unset = UNSET
    directory: str | Unset = UNSET
    listen_sockets: list[ListenSocket] | Unset = UNSET
    pid: int | Unset = UNSET
    rss: int | Unset = UNSET
    rtime: int | Unset = UNSET
    stime: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        command = self.command

        cpu = self.cpu

        directory = self.directory

        listen_sockets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.listen_sockets, Unset):
            listen_sockets = []
            for listen_sockets_item_data in self.listen_sockets:
                listen_sockets_item = listen_sockets_item_data.to_dict()
                listen_sockets.append(listen_sockets_item)

        pid = self.pid

        rss = self.rss

        rtime = self.rtime

        stime = self.stime

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if command is not UNSET:
            field_dict["command"] = command
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if directory is not UNSET:
            field_dict["directory"] = directory
        if listen_sockets is not UNSET:
            field_dict["listen_sockets"] = listen_sockets
        if pid is not UNSET:
            field_dict["pid"] = pid
        if rss is not UNSET:
            field_dict["rss"] = rss
        if rtime is not UNSET:
            field_dict["rtime"] = rtime
        if stime is not UNSET:
            field_dict["stime"] = stime

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.listen_socket import ListenSocket

        d = dict(src_dict)
        command = d.pop("command", UNSET)

        cpu = d.pop("cpu", UNSET)

        directory = d.pop("directory", UNSET)

        _listen_sockets = d.pop("listen_sockets", UNSET)
        listen_sockets: list[ListenSocket] | Unset = UNSET
        if _listen_sockets is not UNSET:
            listen_sockets = []
            for listen_sockets_item_data in _listen_sockets:
                listen_sockets_item = ListenSocket.from_dict(listen_sockets_item_data)

                listen_sockets.append(listen_sockets_item)

        pid = d.pop("pid", UNSET)

        rss = d.pop("rss", UNSET)

        rtime = d.pop("rtime", UNSET)

        stime = d.pop("stime", UNSET)

        process_stat = cls(
            command=command,
            cpu=cpu,
            directory=directory,
            listen_sockets=listen_sockets,
            pid=pid,
            rss=rss,
            rtime=rtime,
            stime=stime,
        )

        process_stat.additional_properties = d
        return process_stat

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
