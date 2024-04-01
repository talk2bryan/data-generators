from data_generators.contacts.phone_number import PhoneNumber


def test_str():
    phone_number = PhoneNumber(1, 123, 4567890)
    assert str(phone_number) == "+1 (123) 4567890"


def test_str_another():
    phone_number = PhoneNumber(44, 20, 1234567)
    assert str(phone_number) == "+44 (20) 1234567"
