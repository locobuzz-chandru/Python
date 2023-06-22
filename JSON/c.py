import json


class Address:
    def __init__(self, street, city, pincode):
        self.street = street
        self.city = city
        self.pincode = pincode


address = Address(street="STREET", city="CITY", pincode=582103)


class AddressEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Address):
            return obj.__dict__
        return super().default(obj)


with open('person.json', 'w') as file:
    json.dump({'name': 'NAME', 'age': 25, 'address': address}, file, cls=AddressEncoder)


def check(obj):
    address_keys = list(obj.keys())
    address_fields = ["street", "city", "pincode"]
    if len(address_keys) == len(address_fields) and all([True for key in address_keys if key in address_fields]):
        return True
    return False


def object_hook(dct):
    if check(dct):
        dct["address"] = Address(*dct)
        return dct
    return dct


with open('person.json', 'r') as file:
    print(json.load(file, object_hook=object_hook))
