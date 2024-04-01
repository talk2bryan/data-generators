"""Phone Number Data class."""

from dataclasses import dataclass


@dataclass
class PhoneNumber:
    """Phone Number Data class.

    We are using the North American Numbering Plan (NANP)
    for the phone numbers.
    """

    country_code: int
    area_code: int
    subscriber_number: int

    def __str__(self) -> str:
        return (
            f"+{self.country_code} " f"({self.area_code}) " f"{self.subscriber_number}"
        )
