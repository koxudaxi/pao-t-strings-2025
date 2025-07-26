# C-style (printf-style) formatting examples

# Basic usage
name = "Alice"
age = 30

# Single placeholder
print("%s" % name)  # "Alice"

# Multiple placeholders
print("Name: %s, Age: %d" % (name, age))  # "Name: Alice, Age: 30"

# Different format specifiers
pi = 3.14159
print("Pi: %.2f" % pi)  # "Pi: 3.14"
print("Hex: %x" % 255)  # "Hex: ff"
print("Padded: %5d" % 42)  # "Padded:    42"

# Dictionary formatting
data = {"name": "Bob", "score": 95}
print("%(name)s scored %(score)d%%" % data)  # "Bob scored 95%"

# Comparison with newer methods
print("\n=== Comparison ===")
print("%s is %d years old" % (name, age))  # C-style
print("{} is {} years old".format(name, age))  # str.format()
print(f"{name} is {age} years old")  # f-string