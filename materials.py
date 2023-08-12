from dataclasses import dataclass
from typing import Any

@dataclass
class Material:
    id: int
    name: str
    symbol: str

class Materials():
    materials = [
        Material(0, "Empty", "."),
        Material(1, "Food", "*"),
    ]

    def __getattribute__(self, __name: str) -> Material:
        return next((x for x in Materials.materials if x.name == __name), None)
    
    def __getitem__(self, __name: str) -> Material:
        return next((x for x in Materials.materials if x.name == __name), None)
    
    def __iter__(self):
        return iter(Materials.materials)
    
    def __len__(self):
        return len(Materials.materials)
    
    def __contains__(self, item):
        return item in Materials.materials

materials = Materials()