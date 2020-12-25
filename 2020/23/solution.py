from collections import deque

input_cups = '364297581' 
cups = list(map(int, input_cups))

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
    
    def pop_next_n(self, n):
        next_n = []

        curr = self.next
        for _ in range(n):
            next_n.append(curr)
            curr = curr.next
        
        self.next = curr

        return next_n
    
    def insert_after(self, nodes):
        prev = self
        prev_next = self.next
        for node in nodes:
            prev.next = node
            prev = node
        prev.next = prev_next
    
    def values(self):
        values = [self.value]
        curr = self.next
        while curr != self:
            values.append(curr.value)
            curr = curr.next
        return values

    def __repr__(self):
        return " ".join(map(str, self.values()))

def decrement_and_wrap(num, min, max):
    return (num - 1 - min) % max + min

def move(cups, n):
    max_cup = max(cups)
    min_cup = min(cups)

    cup_map = {}
    prev = None
    last = None
    for cup in reversed(cups):
        node = Node(cup, prev)
        cup_map[cup] = node
        if not last:
            last = node
        prev = node
    head = prev
    last.next = head

    current_cup = head

    for _ in range(n):
        pick_up = current_cup.pop_next_n(3)
        pick_up_values = {node.value for node in pick_up}

        destination_cup_value = decrement_and_wrap(current_cup.value, min_cup, max_cup)
        while destination_cup_value in pick_up_values:
            destination_cup_value = decrement_and_wrap(destination_cup_value, min_cup, max_cup)
        
        destination_cup = cup_map[destination_cup_value]
        destination_cup.insert_after(pick_up)

        current_cup = current_cup.next
    
    return head.values(), cup_map


final_order, _ = move(cups, 100)
print(final_order)

max_cup = max(cups)
more_cups = cups + [cup for cup in range(max_cup + 1, 1_000_000 + 1)]

_, cup_map = move(more_cups, 10_000_000)

cup_1 = cup_map[1]
print(cup_1.next.value * cup_1.next.next.value)
