import secrets
import hashlib
from Models.Character import Character

class User:
    _id_counter = 1

    def __init__(self, username: str, password: str):
        self._username = username
        self._user_id = User._id_counter
        User._id_counter += 1
        self._password = hashlib.sha256(password.encode()).hexdigest()
        self._token = secrets.token_hex(16)
        self._characters = []

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value: str):
        self._username = value

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: str):
        self._password = hashlib.sha256(value.encode()).hexdigest()

    @property
    def token(self) -> str:
        return self._token

    @property
    def characters(self) -> list:
        return self._characters

    #Métodos
    def create_character(self, character: Character) -> bool:
        if len(self._characters) < 3:
            self._characters.append(character)
            return True
        return False

    def view_characters(self) -> list:
        return self._characters

    def edit(self, new_username: str = None, new_password: str = None):
        if new_username:
            self._username = new_username
        if new_password:
            self.password = new_password

    def edit_character(self, id: int, data: Character) -> bool:
        if 0 <= id < len(self._characters):
            self._characters[id] = data
            return True
        return False

    def login(self, input_username: str, input_password: str) -> bool:
        hashed_input = hashlib.sha256(input_password.encode()).hexdigest()
        return self._username == input_username and self._password == hashed_input

    def to_dictionary(self):
        return {
            "username": self._username,
            "user_id": self._user_id,
            "characters": [{"id": char.character_id, "name": char.name} 
                        for char in self._characters]
        }