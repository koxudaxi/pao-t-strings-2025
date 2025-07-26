#!/usr/bin/env python3.14
"""Template Type - Understanding the structure of Template objects"""

from string import templatelib

# Create a template with multiple interpolations
user = "Alice"
action = "logged in"
timestamp = "2025-01-15 10:30:00"

template = t"User {user} {action} at {timestamp}"

print("=== Template Type Structure ===")
print(f"Template: t\"User {{user}} {{action}} at {{timestamp}}\"")
print()

# Access static parts
print("Static parts (.strings):")
for i, static in enumerate(template.strings):
    print(f"  [{i}]: {static!r}")
print()

# Access interpolations
print("Dynamic parts (.interpolations):")
for i, interp in enumerate(template.interpolations):
    print(f"  [{i}]: {interp}")
    print(f"       value={interp.value!r}")
    print(f"       expression={interp.expression!r}")
print()

# Demonstrate the interleaving
print("=== How they combine ===")
print("Pattern: string[0] + interp[0] + string[1] + interp[1] + ... + string[n]")
print()

# Show the actual structure
result_parts = []
for i, static in enumerate(template.strings[:-1]):
    result_parts.append(f"'{static}'")
    result_parts.append(f"<{template.interpolations[i].expression}={template.interpolations[i].value!r}>")
result_parts.append(f"'{template.strings[-1]}'")
print("Structure: " + " + ".join(result_parts))