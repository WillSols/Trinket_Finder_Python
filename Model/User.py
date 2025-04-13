import secrets
import hashlib

class User:
    _id_counter = 0

    def __init__(self, username: str, user_id: int, password: str, token: str = None):
        self._username = username
        self._user_id = User.user_id
        self._password = password
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
        self._password = value

    @property
    def token(self) -> str:
        return self._token

    @property
    def characters(self) -> list:
        return self._characters

    ## Métodos
    def create(self, username: str, password: str):
        _id_counter += 1
        self._username = username
        self._password = hashlib.sha256(password.encode()).hexdigest()

    def create_character(self, character):
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
            self._password = hashlib.sha256(new_password.encode()).hexdigest()

    def login(self, input_username: str, input_password: str) -> bool:
        return (self._username == input_username and 
                self._password == hashlib.sha256(input_password.encode()).hexdigest())
