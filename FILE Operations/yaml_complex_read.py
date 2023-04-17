import yaml

with open('yaml_complex.yml', 'r') as f:
    data = yaml.safe_load(f)

print(data)
