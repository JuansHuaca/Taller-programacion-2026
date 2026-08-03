from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

T = TypeVar('T')
ID = TypeVar('ID')

class Repository(ABC, Generic[T, ID]):
    @abstractmethod
    def save(self, entity: T) -> T:
        pass

    @abstractmethod
    def find_by_id(self, entity_id: ID) -> Optional[T]:
        pass