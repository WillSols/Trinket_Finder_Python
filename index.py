import Tests.UnityTests as UnityTests
from Controllers.userController import UserController
from Views.userView import UserView

def main():
    print("Welcome to Trinket Finder!")

    controller = UserController()
    view = U1serView(controller)
    view.show_main_menu()

    UnityTests.run_user_tests()
    UnityTests.run_user_controller_tests()

if __name__ == "__main__":
    main()
