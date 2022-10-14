# Order-Processing
Order management system

Build an order management system that can store orders along with their products
referred as orderlines henceforth. System should also be capable of showing all the
orders taken so far and also the details of a given order along with their orderlines.


Order Processing:

An order contains different products with quantities to buy. We will call it an order line. So an
order has multiple order line(s) & one order line has product name and quantity.
Whenever a user adds an orderline it’s status is marked as DRAFT
Possible Statuses of Order & Order Line
- DRAFT [ base status ]: This means we want to order this product but the order line is not
booked yet.

On starting the application, it should display the available commands that
are executable via command line / STDIO
Commands of multiple types:
1. CREATE_ORDER
2. ADD_PRODUCT_ORDER [order_id] [product_name] [product_quantity]
3. SHOW_ORDER [order_id]
4. SHOW_ORDERS


Commands:
Type 1: CREATE_ORDER
This command should create an order in your system and print string “Order
created with id [order_id]”

Example:

CREATE_ORDER

Order created with id 1


### Answer
```
class Order:
    
    def __init__(self, order_id):
        self.order_id = order_id
        self.order_status = 'DRAFT'
        self.order_items = {}

    def create_order(self):
            print("CREATE ORDER")
            print(f"Order created with id {self.order_id}")


```

Type 2: ADD_ORDERLINE [order_id] [product_name] [product_quantity]
This command should add product to the given order id with given product 
name and quantity.
-  If the product is added then print “[product_quantity] [product_name] 
added to order
[order_id]”
-  If the order id doesn’t exist in the system then print “Order with id 
[order_id] does not exist”
-  If the order product name doesn’t exist in the inventory then print“Product [product name] does not exist”

Example:

ADD_ORDERLINE 1 Apples 5

5 Apples added to order 1

### Answer
```
    def add_product(self, product_name, product_quantity):
        if product_name in self.order_items:
            self.order_items[product_name] += product_quantity
        else:
            self.order_items[product_name] = product_quantity
        
        print(f"ADD_ORDERLINE {self.order_id} {product_name} {product_quantity}")
        print(f"{product_quantity} {product_name} added to order {self.order_id}")    

```

Type 3: SHOW_ORDER [order_id]

This command should print the current state of the given order in the
following format:
Order [order_id] {order_status} {total count of items} [product_name]
[quantity] [status of order line]
… other order lines

Example:

SHOW_ORDER 1

Order 1 DRAFT 8

Apples 5 DRAFT

Oranges 3 DRAFT


### Answer
```
    def show_order(self):
        print(f"SHOW_ORDER {self.order_id}")
        print(f"Order {self.order_id} {self.order_status} {sum(self.order_items.values())}")
        for product, quantity in self.order_items.items():
            print(f"{product} {quantity} {self.order_status}")
```

Type 4: SHOW_ORDERS

This command should print the current state of the all the orders in the 
following format:

Order [order_id] {Order status} {total count of items}
[product_name] [quantity] [status of order line]

Example:

SHOW_ORDERS

Order 1 DRAFT 8

Apples 5 DRAFT

Oranges 3 DRAFT

Order 2 DRAFT 5

Peaches 3 DRAFT

Orange 2 DRAFT

### Answer
```
    def show_orders(self):
        print(f"SHOW_ORDERS")
        print(f"Order {self.order_id} {self.order_status} {sum(self.order_items.values())}")
        for product, quantity in self.order_items.items():
            print(f"{product} {quantity} {self.order_status}")


```


### Answer with Test
```
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

```

