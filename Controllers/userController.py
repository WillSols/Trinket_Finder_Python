from Models.User import User
from Models.Character import Character
import hashlib
import secrets
from typing import Optional, List, Dict

class UserController:
    def __init__(self):
        self._users = []
        self._logged_users = {}

    # Métodos de autenticação
    def register(self, username: str, password: str) -> Optional[User]:
        """Registra um novo usuário"""
        if self._find_user_by_username(username) is not None:
            return None

        new_user = User(username, password)
        self._users.append(new_user)
        return new_user

    def login(self, username: str, password: str) -> Optional[str]:
        """Realiza login e retorna o token de sessão"""
        user = self._find_user_by_username(username)
        if user and user.login(username, password):
            token = user.token
            self._logged_users[token] = user
            return token
        return None

    def logout(self, token: str) -> bool:
        """Realiza logout do usuário"""
        if token in self._logged_users:
            del self._logged_users[token]
            return True
        return False

    def validate_token(self, token: str) -> Optional[User]:
        """Valida se o token corresponde a um usuário logado"""
        return self._logged_users.get(token)

    # Métodos de gerenciamento de usuário eu vou me matar se isso não rodar
    def update_user(self, token: str, new_username: Optional[str] = None, new_password: Optional[str] = None) -> bool:
        user = self.validate_token(token)
        if not user:
            return False

        if new_username and self._find_user_by_username(new_username) is None:
            user.username = new_username

        if new_password:
            user.password = new_password

        return True

    # Métodos de personagens (versão sem trinket e specialization, ajustar  na entrega final)
    def create_character(self, token: str, name: str) -> bool:
        user = self.validate_token(token)
        if not user:
            return False

        character = Character(name=name, user_id=user.user_id)
        return user.create_character(character)

    def get_user_characters(self, token: str) -> Optional[List[Character]]:
        user = self.validate_token(token)
        return user.characters if user else None

    def edit_character(self, token: str, character_id: int, new_name: str) -> bool:
        user = self.validate_token(token)
        if not user:
            return False

        if 0 <= character_id < len(user.characters):
            user.characters[character_id].name = new_name
            return True
        return False

    # Métodos auxiliares
    def _find_user_by_username(self, username: str) -> Optional[User]:
        for user in self._users:
            if user.username == username:
                return user
        return None

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        for user in self._users:
            if user.user_id == user_id:
                return user
        return None

    def user_to_dict(self, token: str) -> Optional[Dict]:
        user = self.validate_token(token)
        return user.to_dictionary() if user else None