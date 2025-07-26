# Understanding the len(strings) = len(interpolations) + 1 rule

# Example 1: Simple t-string
template = t"Hello {name}!"
print(f"strings: {template.strings}")
print(f"interpolations: {len(template.interpolations)} items")
print(f"len(strings): {len(template.strings)}")
print(f"len(interpolations): {len(template.interpolations)}")
print(f"Rule check: {len(template.strings)} = {len(template.interpolations)} + 1")

# strings: ('Hello ', '!')
# interpolations: 1 items
# Rule: 2 = 1 + 1 ✓

print("\n" + "="*50 + "\n")

# Example 2: Multiple interpolations
template2 = t"{greeting} {name}, you have {count} messages"
print(f"strings: {template2.strings}")
print(f"interpolations: {len(template2.interpolations)} items")
print(f"Rule check: {len(template2.strings)} = {len(template2.interpolations)} + 1")

# strings: ('', ' ', ', you have ', ' messages')
# interpolations: 3 items  
# Rule: 4 = 3 + 1 ✓

print("\n" + "="*50 + "\n")

# Example 3: Why this pattern?
print("Visual representation:")
print("t\"Hello {name}!\"")
print("  ↓")
print("['Hello ', name, '!']")
print("  ↓")
print("strings: ('Hello ', '!')")
print("interpolations: (name,)")
print("\nThe pattern is: string₀ + interp₀ + string₁ + interp₁ + ... + stringₙ")
print("So there's always one more string than interpolations!")

print("\n" + "="*50 + "\n")

# Example 4: Edge cases
print("Edge case - no interpolations:")
template3 = t"Just text"
print(f"strings: {template3.strings}")
print(f"interpolations: {len(template3.interpolations)} items")
print(f"Rule: {len(template3.strings)} = {len(template3.interpolations)} + 1")
# strings: ('Just text',)
# interpolations: 0 items
# Rule: 1 = 0 + 1 ✓

print("\nEdge case - starts with interpolation:")
template4 = t"{name} is here"
print(f"strings: {template4.strings}")
print(f"Note: First string is empty!")
# strings: ('', ' is here')
# Rule still holds: 2 = 1 + 1 ✓