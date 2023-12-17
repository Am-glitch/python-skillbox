from collections.abc import Iterator


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: int) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node

    def get(self, index: int) -> int:
        if index < 0:
            raise IndexError("Index must be non-negative")
        current = self.head
        for _ in range(index):
            if not current:
                raise IndexError("Index out of range")
            current = current.next_node
        if not current:
            raise IndexError("Index out of range")
        return current.data

    def remove(self, index: int) -> None:
        if index < 0:
            raise IndexError("Index must be non-negative")
        if index == 0:
            if self.head:
                self.head = self.head.next_node
            else:
                raise IndexError("Index out of range")
        else:
            current = self.head
            for _ in range(index - 1):
                if not current or not current.next_node:
                    raise IndexError("Index out of range")
                current = current.next_node
            if not current or not current.next_node:
                raise IndexError("Index out of range")
            current.next_node = current.next_node.next_node

    def __iter__(self) -> Iterator[int]:
        current = self.head
        while current:
            yield current.data
            current = current.next_node

    def __str__(self) -> str:
        return "[" + " ".join(map(str, self)) + "]"


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
