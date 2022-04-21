import unittest
import shopping


class ShoppingTest(unittest.TestCase):
    def test_that_basket_can_be_created(self):
        cart = shopping.Shopping(3)
        self.assertIsNotNone(cart)

    def test_that_item_can_enter_cart(self):
        cart = shopping.Shopping(3)
        cart.add(1)

if __name__ == '__main__':
    unittest.main()