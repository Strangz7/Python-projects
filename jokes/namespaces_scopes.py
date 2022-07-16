import datetime
import uuid

# for name in sorted(datetime.__dict__):
#     print(name)


class Product:
    def __init__(self, product_name, product_id, price):
        # self.product_id = self.get_id()
        self.product_name = product_name
        self.product_id = product_id
        self.price = price

    def __repr__(self):
        return f"Product(product_name = {self.product_name}, price = {self.price}"

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[-6]


product = Product("Mobile Phone","54274", 2900 )
# for name in Product.__dict__:
#     print(name)

print(product.__dict__)