# === Stage 5: Удаление и восстановление ===
# Project: MovingBoxes
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Box:
    number: str
    room: str
    weight: float
    fragile: bool = False

    def __post_init__(self) -> None:
        self.deleted: bool = False
        self.deleted_reason: Optional[str] = None

    @property
    def is_active(self) -> bool:
        return not self.deleted

    def soft_delete(self, reason: str) -> None:
        self.deleted = True
        self.deleted_reason = reason

    def restore(self) -> None:
        self.deleted = False
        self.deleted_reason = None

    def remove(self) -> None:
        self.deleted = True
        self.deleted_reason = "removed"

    def to_dict(self) -> Dict:
        return {
            "number": self.number,
            "room": self.room,
            "weight": self.weight,
            "fragile": self.fragile,
            "deleted": self.deleted,
            "deleted_reason": self.deleted_reason,
        }


class MovingStore:
    def __init__(self) -> None:
        self._boxes: Dict[str, Box] = {}
        self._deleted_boxes: Dict[str, Box] = {}

    def add_box(self, box: Box) -> None:
        self._boxes[box.number] = box

    def get_box(self, number: str) -> Optional[Box]:
        return self._boxes.get(number)

    def iter_active_boxes(self) -> List[Box]:
        return [b for b in self._boxes.values() if b.is_active]

    def soft_delete_box(self, number: str, reason: str) -> bool:
        box = self._boxes.get(number)
        if box is None or box.is_active:
            return False
        box.soft_delete(reason)
        return True

    def restore_box(self, number: str) -> bool:
        box = self._boxes.get(number)
        if box is None or not box.deleted:
            return False
        box.restore()
        return True

    def remove_box(self, number: str) -> bool:
        box = self._boxes.get(number)
        if box is None or box.is_active:
            return False
        box.remove()
        self._deleted_boxes[number] = box
        del self._boxes[number]
        return True

    def get_deleted_box(self, number: str) -> Optional[Box]:
        return self._deleted_boxes.get(number)

    def recover_deleted_box(self, number: str) -> bool:
        box = self._deleted_boxes.get(number)
        if box is None:
            return False
        box.restore()
        self._boxes[number] = box
        del self._deleted_boxes[number]
        return True

    def list_deleted(self) -> List[Box]:
        return list(self._deleted_boxes.values())
