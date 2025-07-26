#!/usr/bin/env python3.14
"""Sub-language Examples - Working with multi-line templates containing SQL, HTML, etc."""

from string import templatelib
from datetime import datetime, timedelta

# Mock sql() function from earlier
def sql(template):
    """Mock SQL parameterization"""
    if not isinstance(template, templatelib.Template):
        raise TypeError("sql() requires a template string")
    
    query_parts = []
    params = []
    
    for i, static in enumerate(template.strings[:-1]):
        query_parts.append(static)
        query_parts.append("?")
        params.append(template.interpolations[i].value)
    
    query_parts.append(template.strings[-1])
    
    return {
        "query": ''.join(query_parts),
        "params": params
    }

print("=== Multi-line SQL Sub-language ===")
# Complex reporting query
start_date = datetime.now() - timedelta(days=30)
min_order_count = 5
user_status = "active"

report_query = t"""
    SELECT 
        u.name,
        COUNT(o.id) as order_count,
        SUM(o.total) as total_spent,
        AVG(o.total) as avg_order_value
    FROM users u
    LEFT JOIN orders o ON u.id = o.user_id
    WHERE u.created_at > {start_date}
      AND u.status = {user_status}
    GROUP BY u.id, u.name
    HAVING COUNT(o.id) >= {min_order_count}
    ORDER BY total_spent DESC
    LIMIT 10
"""

print("Multi-line SQL template:")
print("Template literal:")
for line in str(report_query).split('\n'):
    if line.strip():
        print(f"  {line}")

result = sql(report_query)
print("\nParameterized query:")
print(result["query"])
print(f"\nParameters: {result['params']}")
print()

print("=== Multi-line HTML Templates ===")
# Complex HTML component
products = [
    {"id": 1, "name": "Python T-Shirt", "price": 25.99, "image": "python-tee.jpg"},
    {"id": 2, "name": "Django Mug", "price": 15.99, "image": "django-mug.jpg"},
    {"id": 3, "name": "Flask Sticker Pack", "price": 5.99, "image": "flask-stickers.jpg"},
]

# Note: In real code, you'd use tdom's html() function for safety
product_grid_template = t"""
<div class="product-grid">
    <h2>Featured Products</h2>
    <div class="grid grid-cols-3 gap-4">
        <!-- In real code, this would be generated in a loop -->
        <div class="product-card">
            <img src="{products[0]['image']}" alt="{products[0]['name']}">
            <h3>{products[0]['name']}</h3>
            <p class="price">${products[0]['price']:.2f}</p>
        </div>
        <!-- More products would follow... -->
    </div>
</div>
"""

print("HTML template structure:")
print(f"Number of interpolations: {len(product_grid_template.interpolations)}")
print("Interpolated expressions:")
for i, interp in enumerate(product_grid_template.interpolations):
    print(f"  {i+1}. {interp.expression} = {interp.value}")
print()

print("=== GraphQL Query Templates ===")
# GraphQL query with variables
user_id = "user123"
include_orders = True
order_limit = 10

graphql_template = t"""
query GetUserProfile($userId: ID!) {{
    user(id: {user_id}) {{
        id
        name
        email
        created_at
        {'orders(limit: ' + str(order_limit) + ') { id total items { name price } }' if include_orders else ''}
    }}
}}
"""

print("GraphQL query template:")
print("Shows how conditional logic can be embedded")
print(f"Include orders: {include_orders}")
print(f"Result would include orders section: {'Yes' if include_orders else 'No'}")
print()

print("=== Shell Command Templates ===")
# System administration scripts
backup_dir = "/var/backups"
database_name = "production"
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
keep_days = 7

backup_script = t"""
#!/bin/bash
# Database backup script generated on {datetime.now()}

BACKUP_FILE="{backup_dir}/{database_name}_{timestamp}.sql.gz"

echo "Starting backup of {database_name}..."
pg_dump {database_name} | gzip > "$BACKUP_FILE"

echo "Cleaning up old backups..."
find {backup_dir} -name "{database_name}_*.sql.gz" -mtime +{keep_days} -delete

echo "Backup complete: $BACKUP_FILE"
"""

print("Generated shell script:")
print("Key parameters:")
print(f"  Database: {database_name}")
print(f"  Backup location: {backup_dir}")
print(f"  Retention: {keep_days} days")
print()

print("=== Why Sub-languages are Challenging ===")
print("1. Multiple syntaxes in one file")
print("2. Hard to validate visually")
print("3. Easy to make syntax errors")
print("4. Context switching between languages")
print("5. Different escaping rules")
print()
print("This is why tools like t-linter are valuable!")
print("They can provide:")
print("- Syntax highlighting for each sub-language")
print("- Validation of SQL, HTML, etc. within templates")
print("- Auto-completion for sub-language constructs")
print("- Error detection before runtime")