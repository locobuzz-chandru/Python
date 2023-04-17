import yaml

data = {
    "name": "ABC",
    "age": 25,
    "lang": ["Python", "C", "Java"],
    "address": {
        "city": "Bangalore",
        "zip": 123456,
        "country": "India"
    }
}

with open("yaml_writer_file.yml", 'w') as f:
    yaml.dump(data, f, default_flow_style=False)
