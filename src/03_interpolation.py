#!/usr/bin/env python3.14
"""Interpolation Type - Understanding interpolation objects in detail"""

from string import templatelib

# Example with all interpolation features
name = "world"
pi = 3.14159
debug_obj = {"key": "value"}

# Templates with different interpolation features
simple = t"Hello {name}"
formatted = t"Pi is {pi:.2f}"
converted = t"Debug: {debug_obj!r}"
aligned = t"Hello {name:>10s}!"
complex_format = t"Value: {pi:+010.4f}"

print("=== Interpolation Type Details ===")
print()

def analyze_interpolation(template, description):
    print(f"{description}:")
    print(f"  Template: {template!r}")
    for i, interp in enumerate(template.interpolations):
        print(f"  Interpolation[{i}]:")
        print(f"    .value = {interp.value!r}")
        print(f"    .expression = {interp.expression!r}")
        print(f"    .conversion = {interp.conversion!r}")
        print(f"    .format_spec = {interp.format_spec!r}")
    print()

# Analyze each template
analyze_interpolation(simple, "Simple interpolation")
analyze_interpolation(formatted, "With format specification")
analyze_interpolation(converted, "With conversion (!r)")
analyze_interpolation(aligned, "With alignment (>10s)")
analyze_interpolation(complex_format, "Complex format spec")

# Show all possible conversions
print("=== Conversion Types ===")
obj = "Hello"
templates = {
    "None": t"{obj}",
    "!s": t"{obj!s}",
    "!r": t"{obj!r}",
    "!a": t"{obj!a}",
}

for conv_type, tmpl in templates.items():
    interp = tmpl.interpolations[0]
    print(f"{conv_type:>4}: conversion={interp.conversion!r}, value={interp.value!r}")