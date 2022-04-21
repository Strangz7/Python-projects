print("""
****************************************************
            Florence & sons company
****************************************************""")
headings = ['Product', 'Quantity', 'Price', 'Total']
products = ['Maggi', 'Salt', 'Rice']
print("Available products MAGGI, SALT, RICE")

maggi_quantity = int(input("Enter the quantity of maggi: "))
maggi_price = 20
maggi_total = maggi_quantity * maggi_price
maggi = ['Maggi', maggi_quantity, maggi_price, maggi_total]

salt_quantity = int(input('Enter the quantity of salt: '))
salt_price = 100
salt_total = salt_quantity * salt_price
salt = ['Salt', salt_quantity, salt_price, salt_total]

rice_quantity = int(input("Enter the quantity of rice: "))
rice_price = 800
rice_total = rice_quantity * rice_price
rice = ['Rice', rice_quantity, rice_price, rice_total]

for heading in headings:
    print(heading, end='\t')
print(" ")
for i in rice:
    print(i, end='\t\t')
print(" ")
for i in salt:
    print(i, end='\t\t')
print(" ")
for i in maggi:
    print(i, end='\t\t')

print(f' \nThe total is:   {salt_total+ rice_total+ maggi_total}')
print("""
***************************************************
            Thanks for your patronage
***************************************************
""")
