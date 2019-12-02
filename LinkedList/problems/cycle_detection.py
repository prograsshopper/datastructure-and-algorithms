# https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem

def has_cycle(head):
    node_list = list()
    node = head
    while node:
        if node in node_list:
            return True
        node_list.append(node)
        node = node.next
    return False
