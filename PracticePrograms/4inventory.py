# Write a Python class Inventory with attributes like item_id, item_name, stock_count, and price, and methods like
# add_item, update_item, and check_item_details.
class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_id, item_name, stock_count, price):
        self.inventory[item_id] = {"item_name": item_name, "stock_count": stock_count, "price": price}

    def update_item(self, item_id, stock_count, price):
        if item_id in self.inventory:
            self.inventory[item_id]["stock_count"] = stock_count
            self.inventory[item_id]["price"] = price
            return 'Item updated'
        return "Item not found in inventory."

    def check_item_details(self, item_id):
        if item_id in self.inventory:
            item = self.inventory[item_id]
            return f"Product Name: {item['item_name']}, Stock Count: {item['stock_count']}, Price: {item['price']}"
        return "Item not found in inventory."


if __name__ == '__main__':
    inventory = Inventory()

    inventory.add_item("1", "Laptop", 100, 500)
    inventory.add_item("2", "Mobile", 110, 450)
    inventory.add_item("3", "Desktop", 120, 500)
    inventory.add_item("4", "Tablet", 90, 550)
    print(inventory.check_item_details("1"))
    print(inventory.update_item("1", 100, 505))
    print(inventory.check_item_details("1"))
    print(inventory.update_item("1", 115, 500))
    print(inventory.check_item_details("1"))
