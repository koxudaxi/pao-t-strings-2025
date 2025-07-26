#!/usr/bin/env python3.14
"""Various Use Cases - Email templates, config files, and simple formatting"""

from string import templatelib
from datetime import datetime

# Simple f() function for basic template formatting
def f(template):
    """Simple template formatter - converts template to string"""
    if not isinstance(template, templatelib.Template):
        return str(template)  # Fallback for non-templates
    
    result = []
    for item in template:
        if isinstance(item, str):
            result.append(item)
        else:
            if item.format_spec:
                result.append(format(item.value, item.format_spec))
            else:
                result.append(str(item.value))
    return ''.join(result)

print("=== Email Templates ===")
# Email template example
user = {
    "name": "Alice Johnson",
    "email": "alice@example.com"
}
order = {
    "id": "ORD-2025-001",
    "items": ["Python Book", "Coffee Mug", "Stickers"],
    "total": 67.99,
    "delivery_date": "January 20, 2025"
}

email_template = t"""
Dear {user['name']},

Your order #{order['id']} has been shipped!

Items in your order:
- Python Book
- Coffee Mug  
- Stickers

Total: ${order['total']:.2f}

Expected delivery: {order['delivery_date']}

Thank you for your purchase!

Best regards,
The Python Store Team
"""

print("Email content:")
print(f(email_template))
print()

print("=== Configuration Files ===")
# Config file generation
config = {
    "db_host": "localhost",
    "db_port": 5432,
    "db_name": "myapp",
    "db_user": "appuser",
    "cache_enabled": True,
    "cache_ttl": 3600,
    "api_key": "secret-key-12345",
    "debug_mode": False
}

config_template = t"""
[database]
host = {config['db_host']}
port = {config['db_port']}
name = {config['db_name']}
user = {config['db_user']}

[cache]
enabled = {str(config['cache_enabled']).lower()}
ttl = {config['cache_ttl']}

[api]
key = {config['api_key']}
debug = {str(config['debug_mode']).lower()}
"""

print("Generated config file:")
print(f(config_template))
print()

print("=== Simple Use Cases ===")
# Basic formatting
name = "World"
print(f"1. Simple greeting: {f(t'Hello {name}!')}")

# With format specifications
pi = 3.14159
print(f"2. Number formatting: {f(t'Pi is approximately {pi:.2f}')}")

# Multiple values
temp_c = 25
temp_f = temp_c * 9/5 + 32
print(f"3. Temperature: {f(t'Today is {temp_c}°C ({temp_f:.1f}°F)')}")

print()
print("=== Dynamic Content Generation ===")
# Generate markdown documentation
api_endpoints = [
    {"method": "GET", "path": "/users", "description": "List all users"},
    {"method": "POST", "path": "/users", "description": "Create a new user"},
    {"method": "GET", "path": "/users/:id", "description": "Get user by ID"},
    {"method": "PUT", "path": "/users/:id", "description": "Update user"},
    {"method": "DELETE", "path": "/users/:id", "description": "Delete user"},
]

markdown_template = t"""
# API Documentation

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Available Endpoints

{len(api_endpoints)} endpoints available:

"""

print(f(markdown_template))

# Generate endpoint documentation
for endpoint in api_endpoints:
    endpoint_template = t"- **{endpoint['method']}** `{endpoint['path']}` - {endpoint['description']}"
    print(f(endpoint_template))

print()
print("=== Benefits of Templates for These Use Cases ===")
print("1. Separation of structure from data")
print("2. Easy to validate template structure")
print("3. Can be processed by different formatters")
print("4. Type information preserved until formatting")
print("5. Format specifications work naturally")