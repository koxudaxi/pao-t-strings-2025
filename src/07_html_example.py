#!/usr/bin/env python3.14
"""HTML Safety Example - Preventing XSS with t-strings"""

from string import templatelib
import html as html_module

# Mock implementation of tdom library
def html(template):
    """
    Mock html() function that demonstrates automatic HTML escaping.
    In real tdom, this would provide more sophisticated context-aware escaping.
    """
    if not isinstance(template, templatelib.Template):
        raise TypeError("html() requires a template string")
    
    result = []
    
    for item in template:
        if isinstance(item, str):
            result.append(item)
        else:
            # In a real implementation, escaping would be context-aware
            # (different for attributes vs text content)
            value = item.value
            
            # Handle different types
            if isinstance(value, dict):
                # Special handling for attributes dict
                attrs = []
                for k, v in value.items():
                    escaped_value = html_module.escape(str(v), quote=True)
                    attrs.append(f'{k}="{escaped_value}"')
                result.append(' '.join(attrs))
            else:
                # Regular HTML escaping
                escaped = html_module.escape(str(value))
                result.append(escaped)
    
    return ''.join(result)

# Demonstrate XSS prevention
print("=== XSS Prevention with HTML Templates ===")
print()

# Dangerous user input
user_input = "<script>alert('xss')</script>"
print(f"Malicious input: {user_input!r}")
print()

# Using f-string (DANGEROUS!)
print("❌ DANGEROUS - Using f-string:")
dangerous_html = f"<h1>{user_input}</h1>"
print(f"HTML: {dangerous_html}")
print("Result: XSS VULNERABILITY - Script would execute!")
print()

# Using t-string with html() function (SAFE!)
print("✅ SAFE - Using t-string with html():")
safe_html = html(t"<h1>{user_input}</h1>")
print(f"HTML: {safe_html}")
print("Result: Input safely escaped, XSS prevented!")
print()

# More examples
print("=== Various XSS Attack Vectors ===")
attacks = [
    ("<img src=x onerror='alert(1)'>", "Image XSS"),
    ("javascript:alert('xss')", "JavaScript protocol"),
    ("<iframe src='evil.com'></iframe>", "IFrame injection"),
    ("'><script>alert('xss')</script>", "Attribute breaking"),
]

for attack, description in attacks:
    safe = html(t"<div class='user-content'>{attack}</div>")
    print(f"{description}:")
    print(f"  Input: {attack!r}")
    print(f"  Safe output: {safe}")
    print()

# Attribute handling
print("=== Attribute Handling ===")
attributes = {
    "src": "image.jpg",
    "alt": "A \"nice\" image",
    "onclick": "alert('should be escaped')"
}

# Show how attributes can be safely handled
safe_img = html(t"<img {attributes} />")
print(f"Attributes dict: {attributes}")
print(f"Safe HTML: {safe_img}")
print()

# Complex HTML generation
print("=== Complex HTML Example ===")
username = "Alice <admin>"
user_bio = "I like to use <strong>HTML</strong> & \"quotes\""
profile_url = "https://example.com/user?name=alice&role=user"

profile_html = html(t"""
<div class="user-profile">
    <h2>{username}</h2>
    <p class="bio">{user_bio}</p>
    <a href="{profile_url}">View Profile</a>
</div>
""")

print("User data:")
print(f"  Username: {username!r}")
print(f"  Bio: {user_bio!r}")
print(f"  URL: {profile_url!r}")
print()
print("Generated HTML:")
print(profile_html)