import pytest

from data_generators.contacts.address import Address
from data_generators.contacts.contact import Contact
from data_generators.contacts.email import Email
from data_generators.contacts.phone_number import PhoneNumber


# Define a fixture for a PhoneNumber instance
@pytest.fixture
def phone_number():
    return PhoneNumber("home", 1, 123, 4567890)


# Define a fixture for an Email instance
@pytest.fixture
def email():
    return Email("work", "test@example.com")


# Define a fixture for an Address instance
@pytest.fixture
def address():
    return Address(
        type="home",
        unit="1A",
        street="123 Main St",
        city="Anytown",
        state="Anystate",
        postal_code="12345",
        country="USA",
    )


# Define a fixture for a Contact instance
@pytest.fixture
def contact(phone_number, email, address):
    return Contact(
        "John", None, "Doe", None, None, None, None, [phone_number], [email], [address]
    )


# Define a fixture for a Contact with all fields filled
@pytest.fixture
def contact_full():
    return Contact(
        first_name="John",
        middle_name="M",
        last_name="Doe",
        nickname="Johnny",
        title="Mr.",
        birth_date="01/01/2000",
        notes="Test contact",
        phone_numbers=[phone_number],
        emails=[email],
        addresses=[address],
    )


def test_contact_full_name(contact):
    assert contact.full_name == "John Doe"


def test_contact_full_name_w_middlename(contact_full):
    assert contact_full.full_name == "John M Doe"


def test_contact_phone_number(contact):
    assert str(contact.phone_numbers[0]) == "HOME: +1 (123) 4567890"


def test_contact_email(contact):
    assert contact.emails[0].address == "test@example.com"


def test_contact_address(contact):
    assert (
        str(contact.addresses[0]) == "HOME: 123 Main St, 1A Anytown, Anystate 12345 USA"
    )


def test_contact_str(contact_full):
    assert str(contact_full) == "John M Doe (Johnny) - Mr."
