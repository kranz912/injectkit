from app.container import injector
from app.services.user_service import UserService

def main():
    user_service = injector.get(UserService)
    print(user_service.greet_user("Kranz"))

if __name__ == "__main__":
    main()
