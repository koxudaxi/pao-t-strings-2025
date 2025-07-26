#!/usr/bin/env python
"""Check if t-strings are available in current Python version"""

import sys

print(f"Python version: {sys.version}")
print(f"Python version info: {sys.version_info}")
print()

# Check if we have Python 3.14+
if sys.version_info < (3, 14):
    print("❌ Python 3.14+ is required for t-strings")
    print("   Your version:", f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    print()
    print("To install Python 3.14 with uv:")
    print("  uv python install 3.14")
    print("  uv venv --python 3.14")
    print("  source .venv/bin/activate")
    sys.exit(1)

# Try to use t-strings
try:
    # This will fail on Python < 3.14
    code = '''
name = "world"
template = t"Hello {name}"
print(f"✅ t-strings are available!")
print(f"   Template type: {type(template)}")
print(f"   Template: {template}")
'''
    exec(code)
    
except SyntaxError as e:
    print(f"❌ t-strings syntax not recognized: {e}")
    print("   Make sure you're using Python 3.14 or later")
    
except NameError as e:
    print(f"❌ Template type not found: {e}")
    print("   The string.templatelib module may not be available")
    
except Exception as e:
    print(f"❌ Unexpected error: {e}")
    print("   Please check your Python installation")