from Models.User import User
from Models.Character import Character
from Controllers.userController import UserController

def run_user_tests():
    print("=== Executando testes de User ===")
    
    user = User(username="mario", password="senha123")

    char1 = Character(name="Luigi")
    char2 = Character(name="Peach")

    user.create_character(char1)
    user.create_character(char2)

    # Verifica os IDs automáticos
    print("\nPersonagens do usuário:")
    for idx, char in enumerate(user.characters):
        print(f"{idx + 1}. {char.name} (ID: {char.character_id})")
    
    # Exibe o dicionário completo
    print("\nDados do usuário:")
    print(user.to_dictionary())
    print("=== Testes de User concluídos ===\n")

def run_user_controller_tests():
    # Teste da UserController
    print("=== Executando testes de UserController ===")
    
    controller = UserController()

    # Registro e login
    print("\nRegistrando e logando usuário...")
    controller.register("player1", "senha123")
    token = controller.login("player1", "senha123")
    print(f"Token de sessão: {token}")

    # Criação de personagem com dados mínimos
    print("\nCriando personagem...")
    character_data = {
        'name': 'Guerreiro',
        'char_class': 'Warrior',
        'role': 'Tank'
    }
    if controller.create_character(token, character_data):
        print("Personagem criado com sucesso!")
    else:
        print("Falha ao criar personagem")

    # Listagem de personagens
    print("\nPersonagens do usuário:")
    characters = controller.get_user_characters(token)
    if characters:
        for char in characters:
            print(f"- {char.name} (ID: {char.character_id}, Classe: {char.char_class})")
    else:
        print("Nenhum personagem encontrado")

    # Atualização de usuário
    print("\nAtualizando username...")
    if controller.update_user(token, new_username="player_updated"):
        print("Username atualizado com sucesso!")
    else:
        print("Falha ao atualizar username")

    # Logout
    print("\nRealizando logout...")
    controller.logout(token)
    print("=== Testes de UserController concluídos ===")

# Executa os testes
if __name__ == "__main__":
    run_user_tests()
    run_user_controller_tests()