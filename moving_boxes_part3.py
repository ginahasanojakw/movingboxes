# === Stage 3: Хранилище в памяти ===
# Project: MovingBoxes
from typing import Dict, List, Optional


class Box:
    def __init__(self, box_number: int, room: str, weight: float, fragile: bool):
        self.box_number = box_number
        self.room = room
        self.weight = weight
        self.fragile = fragile

    def __repr__(self):
        return (
            f"Box(number={self.box_number}, room={self.room!r}, "
            f"weight={self.weight}, fragile={self.fragile})"
        )


class BoxStore:
    def __init__(self):
        self._boxes: Dict[int, Box] = {}

    def add_box(self, box: Box) -> None:
        self._boxes[box.box_number] = box

    def get_box(self, box_number: int) -> Optional[Box]:
        return self._boxes.get(box_number)

    def list_boxes(self) -> List[Box]:
        return list(self._boxes.values())

    def __len__(self):
        return len(self._boxes)


if __name__ == "__main__":
    store = BoxStore()
    store.add_box(Box(1, "Гостиная", 12.5, False))
    store.add_box(Box(2, "Спальня", 3.0, True))
    print(store.list_boxes())
    print(store.get_box(2))
    print(len(store))
