product_name, product_code = input().split()
product_code = int(product_code)

class product:
    def __init__(self, product_name, product_code):
        self.product_name = product_name
        self.product_code = product_code

product_1 = product('codetree', 50)
product_2 = product(product_name, product_code)

print(f'product {product_1.product_code} is {product_1.product_name}')
print(f'product {product_2.product_code} is {product_2.product_name}')