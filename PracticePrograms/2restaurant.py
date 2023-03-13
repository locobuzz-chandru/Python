# Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders, and methods like
# add_item_to_menu, book_tables, and customer_order.
class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = []

    def add_item_to_menu(self, item, price):
        self.menu_items[item] = price

    def book_tables(self, table_number):
        self.book_table.append(table_number)

    def customer_order(self, table_number, order):
        order_details = {'table_number': table_number, 'order': order}
        self.customer_orders.append(order_details)

    def print_menu_items(self):
        for item, price in self.menu_items.items():
            return f"item: {item}, price: {price}"

    def print_table_reservations(self):
        for table in self.book_table:
            return f"Table: {table}"

    def print_customer_orders(self):
        for order in self.customer_orders:
            return f"Table: {order['table_number']}, order: {order['order']}"


if __name__ == '__main__':
    restaurant = Restaurant()

    restaurant.add_item_to_menu("A", 80)
    restaurant.add_item_to_menu("B", 120)
    restaurant.add_item_to_menu("C", 55)

    restaurant.book_tables(1)
    restaurant.book_tables(2)
    restaurant.book_tables(3)

    restaurant.customer_order(1, "A")
    print(restaurant.print_menu_items())
    print(restaurant.print_table_reservations())
    print(restaurant.print_customer_orders())
