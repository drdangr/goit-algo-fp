class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Додає елемент у кінець списку"""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __repr__(self):
        return " -> ".join(map(str, self))

    def reverse(self):
        """Реверсує однозв'язний список in-place"""
        prev = None
        current = self.head

        while current:
            next_node = current.next   # 1. зберегли хвіст
            current.next = prev        # 2. розвернули посилання
            prev = current             # 3. зсув prev
            current = next_node        # 4. зсув current

        self.head = prev
   
    def _split(self, head):
        """Ділить список на дві половини"""
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow.next
        slow.next = None
        return head, middle

    def _merge(self, left, right):
        dummy = Node(0)
        tail = dummy
        while left and right:
            if left.value <= right.value:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        tail.next = left or right
        return dummy.next

    def _merge_sort(self, head):
        if head is None or head.next is None:
            return head
        left, right = self._split(head)
        left = self._merge_sort(left)
        right = self._merge_sort(right)

        return self._merge(left, right)

    def sort(self):
        """Сортує однозв'язний список"""
        self.head = self._merge_sort(self.head)

    def merge_with(self, other):
        """
        Об'єднує два відсортовані однозв'язні списки
        і повертає новий LinkedList
        """
        merged = LinkedList()
        merged.head = self._merge(self.head, other.head)
        return merged


if __name__ == "__main__":
    ll1 = LinkedList()
    for v in [1, 3, 5]:
        ll1.append(v)

    ll2 = LinkedList()
    for v in [2, 4, 6]:
        ll2.append(v)

    print("List 1:")
    print(ll1)

    print("List 2:")
    print(ll2)

    merged = ll1.merge_with(ll2)

    print("Merged list:")
    print(merged)
