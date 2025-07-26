#!/usr/bin/env python3.14
"""Template API Overview - Working with Template objects"""

from string import templatelib

# Create a template for demonstrations
name = "Alice"
age = 30
city = "Tokyo"
template = t"Hello {name}, you are {age} years old and live in {city}!"

print("=== Template Iteration ===")
print("Iterating through template parts:")
for item in template:
    if isinstance(item, str):
        print(f"  String: {item!r}")
    else:
        print(f"  Interpolation: {item.expression} = {item.value!r}")
print()

# Quick access to values
print("=== Quick Access with .values ===")
print(f"template.values = {template.values}")
print(f"Type: {type(template.values)}")
print("Individual values:")
for i, value in enumerate(template.values):
    print(f"  [{i}]: {value!r}")
print()

# Template concatenation
print("=== Template Concatenation ===")
greeting = t"Hello "
subject = t"{name}"
punctuation = t"!"

# Valid concatenation - template + template
combined = greeting + subject + punctuation
print("Valid: t\"Hello \" + t\"{name}\" + t\"!\"")
print(f"Result type: {type(combined)}")
print(f"Combined strings: {combined.strings}")
print(f"Combined interpolations: {[i.value for i in combined.interpolations]}")
print()

# Invalid concatenation - template + string
print("Invalid concatenation examples:")
try:
    invalid = t"Hello " + "world"
except TypeError as e:
    print(f"  t\"Hello \" + \"world\" -> TypeError: {e}")

try:
    invalid = "Hello " + t"world"
except TypeError as e:
    print(f"  \"Hello \" + t\"world\" -> TypeError: {e}")
print()

# Practical iteration example
print("=== Practical Example: Building Output ===")
def simple_formatter(template):
    """A simple formatter that joins template parts"""
    result = []
    for item in template:
        if isinstance(item, str):
            result.append(item)
        else:
            # Apply simple formatting
            if item.format_spec:
                # Use format spec if provided
                formatted = format(item.value, item.format_spec)
            elif item.conversion == 'r':
                formatted = repr(item.value)
            elif item.conversion == 's':
                formatted = str(item.value)
            elif item.conversion == 'a':
                formatted = ascii(item.value)
            else:
                formatted = str(item.value)
            result.append(formatted)
    return ''.join(result)

# Test the formatter
number = 42.12345
formatted_template = t"The number is {number:.2f} and its repr is {number!r}"
print(f"Template: t\"The number is {{number:.2f}} and its repr is {{number!r}}\"")
print(f"Formatted: {simple_formatter(formatted_template)}")