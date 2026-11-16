# === Stage 2: Проверка полей ===
# Project: MovingBoxes
box_field_validator = {
    "number": (str, bool),
    "room": (str, bool),
    "weight": (int, float),
    "fragile": bool,
}

box_field_validator_messages = {
    "number": "Поле «номер» должно быть строкой.",
    "room": "Поле «комната» должно быть строкой.",
    "weight": "Поле «вес» должно быть числом.",
    "fragile": "Поле «хрупкость» должно быть булевым.",
}

def normalize_box_field(value, field):
    if field == "number":
        return str(value)
    if field == "room":
        return str(value).strip()
    if field == "weight":
        return float(value)
    if field == "fragile":
        return bool(value)
    return value

def validate_box_fields(box_data):
    for field, expected_types in box_field_validator.items():
        if field not in box_data:
            print(box_field_validator_messages[field])
            continue
        value = box_data[field]
        if not isinstance(value, expected_types):
            print(box_field_validator_messages[field])
            continue
        normalized = normalize_box_field(value, field)
        if field == "weight":
            if normalized < 0:
                print("Поле «вес» не может быть отрицательным.")
            else:
                box_data[field] = normalized
        elif field == "fragile":
            box_data[field] = normalized
        elif field == "number":
            if not value.strip():
                print("Поле «номер» не может быть пустым.")
            else:
                box_data[field] = value
        elif field == "room":
            if not value:
                print("Поле «комната» не может быть пустым.")
            else:
                box_data[field] = value
    return box_data

def validate_box(box):
    if not isinstance(box, dict):
        print("Коробка должна быть словарём.")
        return False
    valid = validate_box_fields(box)
    if "number" in valid and not valid["number"]:
        print("Коробка без номера невалидна.")
    if "room" in valid and not valid["room"]:
        print("Коробка без комнаты невалидна.")
    if "weight" in valid and not valid["weight"]:
        print("Коробка без веса невалидна.")
    if "fragile" in valid and not valid["fragile"]:
        print("Коробка без хрупкости невалидна.")
    return True
