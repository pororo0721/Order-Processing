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
This command should create an order in your system and print string “Order created with id
[order_id]”
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
This command should add product to the given order id with given product name and quantity.
● If the product is added then print “[product_quantity] [product_name] added to order
[order_id]”
● If the order id doesn’t exist in the system then print “Order with id [order_id] does not
exist”
● If the order product name doesn’t exist in the inventory then print “Product [product
name] does not exist”
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

