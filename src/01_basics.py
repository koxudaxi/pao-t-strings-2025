#!/usr/bin/env python3.14
"""Basic t-string examples - Introduction to Template Strings"""

# Basic t-string syntax
name = "world"
template = t"Hello {name}"

print("=== Basic t-string ===")
print(f"Expression: t\"Hello {{name}}\"")
print(f"Result type: {type(template)}")
print(f"Result: {template}")
print()

# Compare with f-string
fstring_result = f"Hello {name}"
print("=== f-string comparison ===")
print(f"f-string: {fstring_result!r} (type: {type(fstring_result).__name__})")
print(f"t-string: {template!r} (type: {type(template).__name__})")
print()

# What's inside a Template?
print("=== Template Structure ===")
print(f"template.strings = {template.strings}")
print(f"template.interpolations = {template.interpolations}")
print()

# Simple example with exclamation
greeting_template = t"Hello, {name}!"
print("=== Greeting Example ===")
print(f"Template: t\"Hello, {{name}}!\"")
print(f"strings: {greeting_template.strings}")
print(f"Number of static parts: {len(greeting_template.strings)}")
print(f"Number of interpolations: {len(greeting_template.interpolations)}")
print(f"Rule: len(strings) == len(interpolations) + 1")