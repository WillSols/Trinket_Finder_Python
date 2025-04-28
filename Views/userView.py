from Controllers.userController import UserController
from Models.User import User
from typing import Optional

class UserView:
    def __init__(self, controller: UserController):
        self.controller = controller
        self.current_user = None
        self.token = None

    def show_main_menu(self):
        while True:
            print("\n=== MENU PRINCIPAL ===")
            print("1. Registrar")
            print("2. Login")
            print("3. Sair")
            
            choice = input("Escolha uma opção: ")
            
            if choice == "1":
                self.register_view()
            elif choice == "2":
                self.login_view()
            elif choice == "3":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida!")

    def register_view(self):
        print("\n--- REGISTRO ---")
        username = input("Nome de usuário: ")
        password = input("Senha: ")
        
        user = self.controller.register(username, password)
        if user:
            print(f"Usuário {username} registrado com sucesso!")
        else:
            print("Nome de usuário já existe!")

    def login_view(self):
        print("\n--- LOGIN ---")
        username = input("Nome de usuário: ")
        password = input("Senha: ")
        
        token = self.controller.login(username, password)
        if token:
            self.token = token
            self.current_user = self.controller.validate_token(token)
            print(f"Bem-vindo, {username}!")
            self.show_user_menu()
        else:
            print("Credenciais inválidas!")

    def show_user_menu(self):
        while self.token and self.controller.validate_token(self.token):
            print("\n=== MENU DO USUÁRIO ===")
            print("1. Criar personagem")
            print("2. Listar personagens")
            print("3. Editar personagem")
            print("4. Editar perfil")
            print("5. Logout")
            
            choice = input("Escolha uma opção: ")
            
            if choice == "1":
                self.create_character_view()
            elif choice == "2":
                self.list_characters_view()
            elif choice == "3":
                self.edit_character_view()
            elif choice == "4":
                self.edit_profile_view()
            elif choice == "5":
                self.controller.logout(self.token)
                self.token = None
                self.current_user = None
                print("Logout realizado com sucesso!")
                break
            else:
                print("Opção inválida!")

    def create_character_view(self):
        print("\n--- CRIAR PERSONAGEM ---")
        name = input("Nome do personagem: ")
        
        if self.controller.create_character(self.token, name):
            print(f"Personagem {name} criado com sucesso!")
        else:
            print("Falha ao criar personagem!")

    def list_characters_view(self):
        characters = self.controller.get_user_characters(self.token)
        if characters:
            print("\n--- SEUS PERSONAGENS ---")
            for idx, char in enumerate(characters):
                print(f"{idx + 1}. {char.name} (ID: {char.character_id})")
        else:
            print("Você não tem personagens ainda!")

    def edit_character_view(self):
        self.list_characters_view()
        try:
            char_id = int(input("\nID do personagem para editar: ")) - 1
            new_name = input("Novo nome: ")
            
            if self.controller.edit_character(self.token, char_id, new_name):
                print("Personagem atualizado com sucesso!")
            else:
                print("Falha ao atualizar personagem!")
        except ValueError:
            print("ID inválido!")

    def edit_profile_view(self):
        print("\n--- EDITAR PERFIL ---")
        new_username = input("Novo nome de usuário (deixe em branco para manter): ")
        new_password = input("Nova senha (deixe em branco para manter): ")
        
        if not new_username and not new_password:
            print("Nenhuma alteração realizada.")
            return
        
        if self.controller.update_user(
            self.token,
            new_username if new_username else None,
            new_password if new_password else None
        ):
            print("Perfil atualizado com sucesso!")
        else:
            print("Falha ao atualizar perfil!")