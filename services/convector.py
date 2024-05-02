import json

def matrix_to_json(matrix: list[list[int]]) -> str:
    json_data = json.dumps(matrix)
    return json_data

def json_to_matrix(field_json: str) -> list[list[int]]:
    matrix: list[list[int]] = json.loads(field_json)
    return matrix
