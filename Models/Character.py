from typing import List, Optional

class Character:
    _id_counter = 1
    
    def __init__(self, name: str, char_class: Optional[str] = None, 
                 specialization: Optional[str] = None, role: Optional[str] = None, 
                 user_id: Optional[int] = None):
        self.name = name
        self.character_id = Character._id_counter
        Character._id_counter += 1
        self.char_class = char_class
        self.specialization = specialization
        self.role = role
        self.equipped_trinkets: List[str] = []
        self.user_id = user_id

    def equip_trinket(self, trinket: str) -> bool:
        if len(self.equipped_trinkets) < 3:
            self.equipped_trinkets.append(trinket)
            return True
        return False

    def remove_trinket(self, slot: int) -> bool:
        if 0 <= slot < len(self.equipped_trinkets):
            self.equipped_trinkets.pop(slot)
            return True
        return False

    def change_spec(self, new_spec: str) -> bool:
        self.specialization = new_spec
        return True

    def to_dict(self) -> dict:
        return {
            "name": self.name
        }
