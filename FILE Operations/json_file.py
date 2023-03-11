import json


def loads_fun1():
    person = '{"name": "Bob", "languages": ["English", "French"]}'
    person_dict = json.loads(person)
    return person_dict


def dumps_fun():
    person_dict = {'name': 'Bob',
                   'age': 12,
                   'children': None
                   }
    person_json = json.dumps(person_dict, indent=4, sort_keys=True)
    return person_json


def write_json():
    person_dict = {"name": "Bob",
                   "languages": ["English", "French"],
                   "married": True,
                   "age": 32
                   }

    with open('person.json', 'w') as json_file:
        json.dump(person_dict, json_file)
    with open('person.json', 'r') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    # print(loads_fun1())
    # print(dumps_fun())
    print(write_json())
