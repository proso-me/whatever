from loan import Loan
from reject_loan import reject_loan


def test_reject_loan():
    loan = Loan(amount=100_000)
    assert not reject_loan(loan).rejected()

    loan = Loan(amount=250_001)
    assert reject_loan(loan).rejected()

    loan = Loan(amount=250_000)
    assert not reject_loan(loan).rejected()

