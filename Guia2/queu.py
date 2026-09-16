from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, value: T):
        self.value: T = value
        self.next: Optional['Node[T]'] = None

class Queue(Generic[T]):
    
    def __init__(self):
        self._front: Optional[Node[T]] = None
        self._rear: Optional[Node[T]] = None
        self._size: int = 0

    def enqueue(self, item: T) -> None:
        
        new_node = Node(item)
        if self.is_empty():
            self._front = self._rear = new_node
        else:
            self._rear.next = new_node
            self._rear = new_node
        self._size += 1

    def dequeue(self) -> Optional[T]:
        
        if self.is_empty():
            return None
        val = self._front.value
        self._front = self._front.next
        if not self._front:
            self._rear = None
        self._size -= 1
        return val

    def search(self, item: T) -> bool:
        
        curr = self._front
        while curr:
            if curr.value == item: return True
            curr = curr.next
        return False

    def is_empty(self) -> bool:
       
        return self._size == 0

    def size(self) -> int:
        
        return self._size