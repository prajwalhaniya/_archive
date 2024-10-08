class Node:
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next

def print_linked_list(head):
    while head is not None:
        print(head.data, end = " ")
        head = head.next

def insert_at_head(head, val):
    temp = Node(val, head)
    return temp

if __name__ == "__main__":
    # Sample array and value for insertion
    arr = [12, 8, 5, 7]
    val = 100
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])

    # Inserting a new node at the head of the linked list
    head = insert_at_head(head, val)

    print_linked_list(head)
