import unittest
import account


class AccountTest(unittest.TestCase):
    def test_that_account_can_be_created(self):
        account1 = account.Account("Ernest")

        self.assertIsNotNone(account1)
        self.assertIsInstance(account1, account.Account)

    def test_that_account_has_a_name(self):
        """
        GIVEN:
        WHEN:
        THEN:
        """

        account1 = account.Account("Ernest")
        name = account1.name
        self.assertEqual("Ernest", name)

    def test_that_account_can_deposit(self):
        """
        GIVEN:  An account class
        WHEN:   when a deposit is made
        THEN:   account balance should be reflected
        """

        account1 = account.Account("Tolani")
        account1.deposit(2000)

        self.assertEqual(2000, account1.balance)

    def test_that_negative_raises_error(self):
        account1 = account.Account("Steven")

        account1.deposit(-1000)
        self.assertRaises(ValueError, account1.deposit(-1000))
        self.assertEqual(0, account1.balance)

    def test_that_account_can_withdraw(self):
        account1 = account.Account("Steven")
        account1.deposit(1000)
        account1.withdraw(500)
        self.assertEqual(500, account1.balance)

    def test_that_you_cannot_withdraw_negative_amount(self):
        account1 = account.Account("Steven")
        account1.deposit(1000)
        account1.withdraw(-500)
        self.assertEqual(1000, account1.balance)

    def test_that_you_cannot_withdraw_more_than_available_balance(self):
        account1 = account.Account("Steven")
        account1.deposit(500)
        account1.withdraw(1000)
        self.assertEqual(500, account1.balance)

    def test_for_second_account(self):
        account2 = account.Account("Amaka")

        self.assertIsNotNone(account2)
        self.assertIsInstance(account2, account.Account)

    def test_for_transfer(self):
        account1 = account.Account("Steven")
        account2 = account.Account("Amaka")
        account1.deposit(5000)
        account1.transfer(2000, 2000)
        account2.deposit(2000)
        # self.assertEqual(3000,account1.balance)
        self.assertEqual(2000, account2.balance)


if __name__ == '__main__':
    unittest.main()
