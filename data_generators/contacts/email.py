from dataclasses import dataclass


@dataclass
class Email:
    """Email Data class."""

    email_type: str
    address: str

    def __post_init__(self):
        self.email_type = self.email_type.upper()

    def __str__(self):
        return f"{self.email_type}: {self.address}"
