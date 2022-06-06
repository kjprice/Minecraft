import json

def read_json(fp: str) -> object:
    with open(fp, 'r') as f:
        return json.load(f)

def write_json(fp: str, data: object) -> None:
    with open(fp, 'w') as f:
        json.dump(data, f, indent=2)