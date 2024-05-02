import json

def matrix_to_json(matrix: list[list[int]]):
    json_data = json.dumps(matrix)
    return json_data
