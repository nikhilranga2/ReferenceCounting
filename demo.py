"""Reference counting and cyclic garbage collection in CPython."""

import gc
import sys


class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

    def __del__(self):
        print(f"Node {self.name} cleaned up")


print("=== Part 1: Reference counting ===")
a = Node("A")
print("After a = Node('A'):", sys.getrefcount(a))  # usually 2

b = a
print("After b = a:", sys.getrefcount(a))  # usually 3

del b
print("After del b:", sys.getrefcount(a))  # usually 2

del a  # the final reference is removed; CPython cleans up Node A

print("\n=== Part 2: Circular references ===")
gc.collect()  # clear any earlier garbage
gc.disable()  # disable automatic cyclic collection for this demo

x = Node("X")
y = Node("Y")
x.next = y
y.next = x

print("X and Y now reference each other")
del x
del y
print("Deleted x and y, but the cycle still exists")

print("Calling gc.collect()...")
collected = gc.collect()  # explicitly detect and collect the cycle
print("Objects collected:", collected)
gc.enable()
