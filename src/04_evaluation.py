#!/usr/bin/env python3.14
"""Evaluation Model - How t-strings evaluate expressions"""

# Demonstrate eager evaluation
print("=== Eager Evaluation ===")
x = 42
template = t"Result: {x * 2 + 1}"
print(f"x = {x}")
print(f"Template: t\"Result: {{x * 2 + 1}}\"")
print(f"Interpolation value: {template.interpolations[0].value}")
print(f"Interpolation expression: {template.interpolations[0].expression!r}")
print()

# Change x after template creation - no effect
x = 100
print(f"After changing x to {x}:")
print(f"Interpolation value still: {template.interpolations[0].value}")
print("(Eager evaluation - value captured at creation time)")
print()

# Lexical scoping example
print("=== Lexical Scoping ===")
global_var = "I'm global"

def create_template():
    local_var = "I'm local"
    return t"Global: {global_var}, Local: {local_var}"

template = create_template()
print("Template created inside function:")
for interp in template.interpolations:
    print(f"  {interp.expression} = {interp.value!r}")
print()

# Full Python expressions
print("=== Full Python Expressions ===")
import math

# Complex expressions in templates
numbers = [1, 2, 3, 4, 5]
template = t"""
Math: {math.sqrt(16)}
List comprehension: {[x**2 for x in numbers if x % 2 == 0]}
Lambda: {(lambda x: x.upper())("hello")}
Ternary: {x if x > 50 else "small"}
"""

print("Complex expressions in templates:")
for i, interp in enumerate(template.interpolations):
    print(f"{i+1}. {interp.expression}")
    print(f"   => {interp.value}")
print()

# Show that it's truly eager
print("=== Proof of Eager Evaluation ===")
counter = 0

def increment():
    global counter
    counter += 1
    return counter

# Create multiple templates
t1 = t"Count: {increment()}"
t2 = t"Count: {increment()}"
t3 = t"Count: {increment()}"

print(f"Counter after creating 3 templates: {counter}")
print(f"t1 value: {t1.interpolations[0].value}")
print(f"t2 value: {t2.interpolations[0].value}")
print(f"t3 value: {t3.interpolations[0].value}")