# Processing t-strings with pattern matching (Python 3.14+)
from string.templatelib import Template, Interpolation

def process_template(template: Template) -> str:
    """Process a template using pattern matching - reimplementing f-string behavior"""
    result = []
    
    # Iterate through template parts in order
    for part in template:
        match part:
            case str():
                # Static string part
                result.append(part)
            case Interpolation(value=val, conversion=conv, format_spec=spec):
                # Dynamic interpolation part
                # Apply conversion if specified
                if conv == "r":
                    val = repr(val)
                elif conv == "s":
                    val = str(val)
                elif conv == "a":
                    val = ascii(val)
                
                # Apply format spec if specified
                if spec:
                    val = format(val, spec)
                else:
                    val = str(val)
                
                result.append(val)
    
    return ''.join(result)

# Example usage
name = "Alice"
age = 30
pi = 3.14159

# Create templates
template1 = t"Hello, {name}!"
template2 = t"Pi is approximately {pi:.2f}"
template3 = t"Debug: name={name!r}, age={age:>5d}"

# Process templates
print("Template 1:", process_template(template1))
print("Template 2:", process_template(template2))
print("Template 3:", process_template(template3))

print("\n" + "="*50 + "\n")

# More advanced example with custom processing
def custom_processor(template: Template) -> dict:
    """Extract template structure for analysis"""
    structure = {
        "static_parts": [],
        "interpolations": []
    }
    
    for part in template:
        match part:
            case str() as s:
                structure["static_parts"].append(s)
            case Interpolation() as interp:
                structure["interpolations"].append({
                    "expression": interp.expression,
                    "value": interp.value,
                    "conversion": interp.conversion,
                    "format_spec": interp.format_spec
                })
    
    return structure

# Analyze template structure
complex_template = t"User {name!r} is {age:03d} years old"
structure = custom_processor(complex_template)

print("Template Structure Analysis:")
print(f"Static parts: {structure['static_parts']}")
print(f"Interpolations:")
for i, interp in enumerate(structure['interpolations']):
    print(f"  [{i}] expr='{interp['expression']}', "
          f"value={interp['value']!r}, "
          f"conversion={interp['conversion']!r}, "
          f"format_spec={interp['format_spec']!r}")