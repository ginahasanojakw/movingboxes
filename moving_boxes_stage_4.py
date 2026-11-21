# === Stage 4: Редактирование записей ===
# Project: MovingBoxes
from typing import Any, Dict


def is_valid_box_number(value: Any) -> bool:
    return isinstance(value, str) and value.strip() != ""


def is_valid_room(value: Any) -> bool:
    return isinstance(value, str) and value.strip() != ""


def is_valid_weight(value: Any) -> bool:
    return isinstance(value, (int, float)) and value > 0


def is_valid_fragility(value: Any) -> bool:
    return value in (True, False)


ALLOWED_FIELDS = {
    "number": is_valid_box_number,
    "room": is_valid_room,
    "weight": is_valid_weight,
    "fragile": is_valid_fragility,
}


def validate_box_update(current: Dict[str, Any], changes: Dict[str, Any]) -> Dict[str, Any]:
    errors: Dict[str, str] = {}
    for field, validator in ALLOWED_FIELDS.items():
        if field not in changes:
            continue
        new_value = changes[field]
        if not validator(new_value):
            errors[field] = "Недопустимое значение для поля '{}'".format(field)
    return errors


def apply_box_update(current: Dict[str, Any], changes: Dict[str, Any]) -> Dict[str, Any]:
    updated = dict(current)
    for field, new_value in changes.items():
        if field in ALLOWED_FIELDS:
            updated[field] = new_value
    return updated
