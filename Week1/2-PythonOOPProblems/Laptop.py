class Product:
    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self. final_price = final_price

    def profit(self):
        profit = self.final_price - self.stock_price
        return profit


class Laptop(Product):
    def __init__(self, name, stock_price, final_price, diskspace, RAM):
        super().__init__(self, name, stock_price, final_price)
        self.diskspace = diskspace
        self.RAM = RAM


class Smartphone(Product):
    def __init__(self, name, stock_price, final_price, display_size, mega_pixels):
        super().__init__(self, name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store:
    def __init__(self, name):
        self.name = name
        self.products = {}

    def load_new_products(self, product, count):
        self.products.append(product)
        self.products[product] = count

    def list_products(self, product_class):


    def sell_product(self, product):
        return True if self.products[product] > 0 else False

    def total_income(self)