from typing import List, Optional
from User import UserId
from Trinkets import Trinket
from Specialization import Specialization

class Character:
    def __init__(self, character_id: int, name: str, char_class: str, 
                 specialization: str, role: str, UserId: int):
        self.character_id = character_id
        self.name = name
        self.char_class = char_class
        self.specialization = specialization
        self.role = role
        self.equipped_trinkets = []
        self.UserId = UserId

    def equip_trinket(self, trinket) -> bool:
        if len(self.equipped_trinkets) < 3:
            self.equipped_trinkets.append(trinket)
            return True
        return False

    def remove_trinket(self, slot: int) -> bool:
        if 0 <= slot < len(self.equipped_trinkets):
            self.equipped_trinkets.pop(slot)
            return True
        return False

    def edit_character(self, new_name: Optional[str] = None, new_class: Optional[str] = None,new_spec: Optional[str] = None, new_role: Optional[str] = None, new_trinkets: Optional[List[Trinket]] = None) -> bool:

        if new_name:
            self.name = new_name
        if new_class:
            self.char_class = new_class
        if new_spec:
            self.specialization = new_spec
        if new_role:
            self.role = new_role
        if new_trinkets:
            self.equipped_trinkets = new_trinkets
        return True

    def change_spec(self, new_spec: str) -> bool:
        self.specialization = new_spec
        return True