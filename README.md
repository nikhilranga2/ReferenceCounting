# Reference Counting and Garbage Collection in Python

A short COMP 211 demonstration of how **CPython** manages memory using reference counting and a cyclic garbage collector.

## Concepts

- **Reference counting:** Each object tracks references to it. Adding a reference increases its count; removing one decreases the count. CPython ordinarily deallocates an object as soon as its count reaches zero.
- **`sys.getrefcount(obj)`:** Shows a reference count, including an extra temporary reference used to pass `obj` to the function. The counts `2 → 3 → 2` are typical for our simple example in CPython.
- **Circular references:** Two `Node` objects can reference one another through `.next`. After their external names are deleted, their reference counts remain above zero even though the objects are unreachable.
- **Cyclic garbage collector:** CPython can find and reclaim these unreachable cycles. `gc.collect()` triggers a collection manually.

## Run the demo

Use Python 3 with CPython:

```bash
python3 demo.py
```

The demo first shows the reference count increasing and decreasing as `a` and `b` reference the same `Node`. It then creates a cycle between `X` and `Y`, disables *automatic cyclic collection* temporarily, and calls `gc.collect()` to show their cleanup.

## Expected output (typical CPython)

```text
=== Part 1: Reference counting ===
After a = Node('A'): 2
After b = a: 3
After del b: 2
Node A cleaned up

=== Part 2: Circular references ===
X and Y now reference each other
Deleted x and y, but the cycle still exists
Calling gc.collect()...
Node X cleaned up
Node Y cleaned up
Objects collected: 2
```

Counts and the number of objects reported as collected can vary with the Python implementation and environment. `__del__` is used here only to show finalization; it is not required for garbage collection.

## Main takeaway

Reference counting handles most object cleanup immediately, but it cannot reclaim unreachable reference cycles on its own. CPython's separate cyclic garbage collector handles those cases.
