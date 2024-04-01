from data_generators.contacts.email import Email


def test_str():
    email = Email(type="Work", address="workemail@company.com")
    assert str(email) == "WORK: workemail@company.com"
