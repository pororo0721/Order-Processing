class Order:
    
    def __init__(self, order_id):
        self.order_id = order_id
        self.order_status = 'DRAFT'
        self.order_items = {}

    def create_order(self):
            print("CREATE ORDER")
            print(f"Order created with id {self.order_id}")

    def add_product(self, product_name, product_quantity):
        if product_name in self.order_items:
            self.order_items[product_name] += product_quantity
        else:
            self.order_items[product_name] = product_quantity
        
        print(f"ADD_ORDERLINE {self.order_id} {product_name} {product_quantity}")
        print(f"{product_quantity} {product_name} added to order {self.order_id}")    



    def show_order(self):
        print(f"SHOW_ORDER {self.order_id}")
        print(f"Order {self.order_id} {self.order_status} {sum(self.order_items.values())}")
        for product, quantity in self.order_items.items():
            print(f"{product} {quantity} {self.order_status}")

    def show_orders(self):
        print(f"SHOW_ORDERS")
        print(f"Order {self.order_id} {self.order_status} {sum(self.order_items.values())}")
        for product, quantity in self.order_items.items():
            print(f"{product} {quantity} {self.order_status}")



# Test Code
order1 = Order(1)
order1.create_order()
order1.add_product('Apples', 5)
order1.add_product('Oranges', 3)
order1.show_order()

order2 = Order(2)
order2.create_order()
order2.add_product('Peaches', 3)
order2.add_product('Orange', 2)
order2.show_order()

order1.show_orders()
order2.show_orders()