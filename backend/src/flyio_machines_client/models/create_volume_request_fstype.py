from enum import StrEnum


class CreateVolumeRequestFstype(StrEnum):
    EXT4 = "ext4"
    RAW = "raw"

    def __str__(self) -> str:
        return str(self.value)
