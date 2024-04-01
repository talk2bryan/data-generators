from data_generators.contacts.email import Email


def test_str():
    email = Email("Work", "workemail@company.com")
    assert str(email) == "WORK: workemail@company.com"
