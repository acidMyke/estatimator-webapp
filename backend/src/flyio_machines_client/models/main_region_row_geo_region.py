from enum import StrEnum


class MainRegionRowGeoRegion(StrEnum):
    AFRICA = "africa"
    ASIA_PACIFIC = "asia_pacific"
    EUROPE = "europe"
    NORTH_AMERICA = "north_america"
    SOUTH_AMERICA = "south_america"

    def __str__(self) -> str:
        return str(self.value)
