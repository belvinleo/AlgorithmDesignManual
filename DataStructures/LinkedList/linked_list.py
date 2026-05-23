from typing import Any, Optional

class Node:
    def __init__(self, data: Any, next: Node):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):