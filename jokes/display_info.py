# def display_info(company='Amazon', price=1140):
#     return f"Company name: {company} Price: ${price}"

def display_info(company, **kwargs):
    print(f"Conpany name: {company}")
    if 'price' in kwargs:
        print(f"Price: $ {kwargs['price']}")


display_info("CD projekt", price=100)
