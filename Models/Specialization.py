from typing import List

class Specialization:
    def __init__(self, spec_id: int, name: str, role: str, primary_attr: str, secondary_attr: str):
        self.spec_id = spec_id
        self.name = name
        self.role = role
        self.primary_attribute = primary_attr
        self.secondary_attribute = secondary_attr

    def create_spec(self, spec_id: int, name: str, role: str, primary_attr: str, secondary_attr: str) -> 'Specialization':
        return Specialization(spec_id, name, role, primary_attr, secondary_attr)

    def edit_spec(self, new_name: str = None, new_role: str = None, 
                 new_primary_attr: str = None, new_secondary_attr: str = None) -> bool:
        if new_name:
            self.name = new_name
        if new_role:
            self.role = new_role
        if new_primary_attr:
            self.primary_attribute = new_primary_attr
        if new_secondary_attr:
            self.secondary_attribute = new_secondary_attr
        return True

    def remove_spec(self) -> bool:
        return True

    def view_spec_list(self) -> List['Specialization']:
        return [self]