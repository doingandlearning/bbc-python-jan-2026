import pytest
from account import BankAccount


def test_account_stores_owner_and_starting_balance():
    account = BankAccount("Kevin", 100)
    assert account.owner == "Kevin"
    assert account.balance == 100


def test_deposit_increases_balance():
    account = BankAccount("Kevin", 100)
    new_balance = account.deposit(50)
    assert new_balance == 150
    assert account.balance == 150


def test_withdraw_decreases_balance():
    account = BankAccount("Kevin", 100)
    new_balance = account.withdraw(30)
    assert new_balance == 70
    assert account.balance == 70


def test_transfer_moves_money_between_accounts():
    a = BankAccount("A", 100)
    b = BankAccount("B", 10)

    a_balance, b_balance = a.transfer_to(b, 25)

    assert a_balance == 75
    assert b_balance == 35
    assert a.balance == 75
    assert b.balance == 35


def test_deposit_allows_negative_numbers_current_behaviour():
    account = BankAccount("Kevin", 100)
    account.deposit(-10)
    assert account.balance == 90


def test_withdraw_allows_overdraft_current_behaviour():
    account = BankAccount("Kevin", 10)
    account.withdraw(50)
    assert account.balance == -40


def test_transfer_allows_overdraft_current_behaviour():
    a = BankAccount("A", 5)
    b = BankAccount("B", 0)

    a.transfer_to(b, 10)

    assert a.balance == -5
    assert b.balance == 10

@pytest.mark.skip
def test_transfer_to_non_account_raises_attribute_error_current_behaviour():
    account = BankAccount("A", 100)

    with pytest.raises(AttributeError):
        account.transfer_to("not an account", 10)
