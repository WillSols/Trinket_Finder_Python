from typing import List

class Trinket:
    def __init__(self, name: str, trinket_id: int, primary_attr: str, secondary_attr: str, 
                 drop_location: str, rarity: str, description: str):
        self.name = name
        self.trinket_id = trinket_id
        self.primary_attribute = primary_attr
        self.secondary_attribute = secondary_attr
        self.drop_location = drop_location
        self.rarity = rarity
        self.description = description

class Trinkets:
    def __init__(self):
        self._trinkets = []

    def create_trinket(self, data: Trinket) -> Trinket:
        self._trinkets.append(data)
        return data

    def edit_trinket(self, id: int, data: Trinket) -> bool:
        for t in self._trinkets:
            if t.trinket_id == id:
                t.name = data.name
                t.primary_attribute = data.primary_attribute
                t.secondary_attribute = data.secondary_attribute
                t.drop_location = data.drop_location
                t.rarity = data.rarity
                t.description = data.description
                return True
        return False

    def view_per_rarity(self, rarity: str) -> List[Trinket]:
        return [t for t in self._trinkets if t.rarity == rarity]

    def recommend_for_character(self, char) -> List[Trinket]:
        return [t for t in self._trinkets 
            if t.primary_attribute == char.primary_attr or t.secondary_attribute == char.secondary_attr]