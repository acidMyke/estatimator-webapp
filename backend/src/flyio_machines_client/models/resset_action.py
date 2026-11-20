from enum import IntEnum


class RessetAction(IntEnum):
    ACTION_READ = 1
    ACTION_WRITE = 2
    ACTION_CREATE = 4
    ACTION_DELETE = 8
    ACTION_CONTROL = 16
    ACTION_ALL = 31
    ACTION_NONE = 0

    def __str__(self) -> str:
        return str(self.value)
