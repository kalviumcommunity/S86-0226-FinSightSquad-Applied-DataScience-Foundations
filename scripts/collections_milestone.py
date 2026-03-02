#!/usr/bin/env python3
def demonstrate_lists():
    print("--- Lists (ordered, mutable) ---")
    fruits = ["apple", "banana", "cherry"]
    print("Original list:", fruits)
    print("Index access [1]:", fruits[1])
    fruits.append("date")
    print("After append:", fruits)
    fruits[0] = "apricot"
    print("After modify index 0:", fruits)
    removed = fruits.pop(2)
    print("Popped element:", removed)
    print("Iterate items:")
    for i, f in enumerate(fruits):
        print(f"  {i}: {f}")

def demonstrate_tuples():
    print("\n--- Tuples (ordered, immutable) ---")
    coords = (10, 20)
    print("Tuple:", coords)
    print("Index access [0]:", coords[0])
    try:
        coords[0] = 5
    except TypeError as e:
        print("Attempting to modify tuple raises:", type(e).__name__, "-", e)

def demonstrate_dicts():
    print("\n--- Dictionaries (key-value mapping) ---")
    person = {"name": "Alice", "age": 30}
    print("Original dict:", person)
    print("Access by key 'name':", person["name"])
    person["age"] = 31
    person["city"] = "New York"
    print("After modify/add:", person)
    print("Iterate keys and values:")
    for k, v in person.items():
        print(f"  {k}: {v}")

def choose_structure_examples():
    print("\n--- Choosing the right structure ---")
    print("- Use list for ordered, changeable collections (e.g., items to process)")
    print("- Use tuple for fixed data that must not change (e.g., coordinates)")
    print("- Use dict for lookup by keys or modeling entities (e.g., person record)")

def main():
    demonstrate_lists()
    demonstrate_tuples()
    demonstrate_dicts()
    choose_structure_examples()

if __name__ == "__main__":
    main()
