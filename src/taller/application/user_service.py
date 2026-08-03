from taller.domain.exceptions import EntityNotFoundException
from taller.domain.repository import Repository

class UserService:
    def __init__(self, repository: Repository):
        self.repository = repository  # Inyección de dependencia (DIP)

    def get_user(self, user_id: str):
        user = self.repository.find_by_id(user_id)
        if not user:
            raise EntityNotFoundException(f"Usuario con ID {user_id} no encontrado")
        return user