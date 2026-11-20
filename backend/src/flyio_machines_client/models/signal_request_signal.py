from enum import StrEnum


class SignalRequestSignal(StrEnum):
    SIGABRT = "SIGABRT"
    SIGALRM = "SIGALRM"
    SIGFPE = "SIGFPE"
    SIGHUP = "SIGHUP"
    SIGILL = "SIGILL"
    SIGINT = "SIGINT"
    SIGKILL = "SIGKILL"
    SIGPIPE = "SIGPIPE"
    SIGQUIT = "SIGQUIT"
    SIGSEGV = "SIGSEGV"
    SIGTERM = "SIGTERM"
    SIGTRAP = "SIGTRAP"
    SIGUSR1 = "SIGUSR1"
    SIGUSR2 = "SIGUSR2"

    def __str__(self) -> str:
        return str(self.value)
