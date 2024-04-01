from dataclasses import dataclass, field
from email.headerregistry import Address

from data_generators.contacts.email import Email
from data_generators.contacts.phone_number import PhoneNumber


@dataclass
class Contact:
    """Contact Data class."""

    first_name: str
    middle_name: str | None
    last_name: str | None
    nickname: str | None
    title: str | None
    birth_date: str | None
    notes: str | None
    phone_numbers: list[PhoneNumber] = field(default_factory=list)
    emails: list[Email] = field(default_factory=list)
    addresses: list[Address] = field(default_factory=list)

    @property
    def full_name(self) -> str:
        return (
            f"{self.first_name}"
            + (f" {self.middle_name}" if self.middle_name else "")
            + (f" {self.last_name}" if self.last_name else "")
        )

    def __str__(self) -> str:
        return (
            f"{self.full_name}"
            + (f" ({self.nickname})" if self.nickname else "")
            + (f" - {self.title}" if self.title else "")
        )
